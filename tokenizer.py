import yaml
import regex as re
from tqdm import tqdm
import gc
import json

def load_config(config_file_path: str = "resources/config.yml"):
    with open(config_file_path, "r") as f:
        config = yaml.safe_load(f)
    print("configs: ", config)
    return config

def get_input_text(config: dict):
    with open(config["input"]["file_path"], 'r', encoding='utf-8') as _f:
        input_text = _f.read() #[line.strip() for line in _f.readlines()]

    print("input_text_char_length:", len(input_text))

    return input_text

def get_limited_input_text(input_text):
    input_text = input_text[:int(config["input"]["lines_to_read"])]
    #input_text = '\n'.join(input_text)

    return input_text


def convert_string_to_tokens(input_text, config):
    if config["token_regex"] and len(config["token_regex"]) > 0:
        print("token regex:", config["token_regex"])
        # TODO: Implement regex-based tokenization
        tokens =  re.findall(config["token_regex"], input_text)
        return [b for token in tokens for b in token.encode('utf-8')]
    else:
        # Default to character-level tokenization
        #return list(input_text)
        return [b for ch in input_text for b in ch.encode('utf-8')]

def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]): # Pythonic way to iterate consecutive elements
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids, pair, idx):
    # in the list of ints (ids), replace all consecutive occurences of pair with the new token idx
    newids = []
    i = 0
    while i < len(ids):
        # if we are not at the very last position AND the pair matches, replace it
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

def encode(text, merges, config: dict):
    """
    Encode text into tokens using the learned merges
    """
    ids = convert_string_to_tokens(text, config)
    
    sorted_merges = sorted(merges.items(), key=lambda x: x[1])
    for (p1, p2), idx in sorted_merges:
        ids = merge(ids, (p1, p2), idx)
    
    return ids

def decode(ids, merges):
    """
    Decode tokens back to text using the learned merges
    """
    # Create reverse mapping from token to pair
    reverse_merges = {idx: pair for pair, idx in merges.items()}
    
    # Expand all tokens recursively
    def expand_token(token):
        if token < 256:  # Base case: token is a byte
            return bytes([token])
        
        # Recursive case: expand the token into its constituent pair
        pair = reverse_merges[token]
        return expand_token(pair[0]) + expand_token(pair[1])
    
    # Expand all tokens and concatenate
    bytes_list = [expand_token(id) for id in ids]
    bytes_data = b''.join(bytes_list)
    
    # Convert bytes back to text
    try:
        return bytes_data.decode('utf-8')
    except UnicodeDecodeError:
        return "[DECODE_ERROR]"

def tokenizer(config: dict):
    # get text from imput file
    input_text = get_input_text(config)
    print("input_text_char_length:", len(input_text))

    limited_input_text = get_limited_input_text(input_text)
    limited_input_text = "aaabdaabdaacd"
    print("limited_input_text_char_length:", len(limited_input_text))

    # here are all the unique characters that occur in this text
    chars = sorted(list(set(input_text)))
    vocab_size = len(chars)
    print(''.join(chars))
    print(f"vocab_size: {vocab_size}")


    stoi = { ch:i for i,ch in enumerate(chars) }
    print("char To Integer: ", stoi)
    itos = { i:ch for i,ch in enumerate(chars) }
    print("Integer to char: ", itos)

    print("limited_input_text: ", limited_input_text)
    #Convert string to tokens
    tokens = convert_string_to_tokens(input_text, config)

    #print("tokens: ", tokens)

    initial_token_len = len(tokens)
    print("Initial token length", initial_token_len)
    print("unique tokens ", len(set(tokens)))

    print("Example tokens: ", ord('क'), chr(2325), ord("।"), chr(2404))

    print("Train the tokenizer")

    vocab_size = int(config["vocab_size"]) # the desired final vocabulary size
    num_merges =  vocab_size - 256 if vocab_size > 256 else vocab_size

    print("num_merges:", num_merges)

    merges = {} # (int, int) -> int
    pbar = tqdm(range(num_merges), desc="Training tokenizer")

    merged_tokens = list(tokens)

    for i in pbar:
        # Get statistics of the tokens
        stats = get_stats(merged_tokens)
        #print("byter-pair: ", stats)
        top_pair = max(stats, key=stats.get)
        idx = 256 + i
        merged_tokens = merge(merged_tokens, top_pair, idx)
        #print(i,":after merge ids: ", merged_tokens)
        merges[top_pair] = idx
        if (i + 1) % 100 == 0:
            current_ratio = initial_token_len / len(merged_tokens)
            pbar.write(f"Iteration {i+1}: compression ratio: {current_ratio:.2f}X")

    print("tokens length:", len(tokens))
    print("ids length:", len(merged_tokens))
    print(f"compression ratio: {len(tokens) / len(merged_tokens):.2f}X")

    return merges

def validate_tokenizer(test_string, merges, config):
    encoded_tokens = encode(test_string, merges, config)
    decoded_string = decode(encoded_tokens, merges)
    print("test_string: ", test_string)
    print("encoded-token-size: ", len(encoded_tokens))
    print("encoded-token-ids: ", encoded_tokens)
    print("decoded_string: ", decoded_string)

    return len(encoded_tokens), encoded_tokens, decoded_string


def save(merges, config):
    serializable_merges = {f"{k[0]},{k[1]}": v for k, v in merges.items()}
    with open(config["output"]["file_path"], 'w', encoding='utf-8') as f:
            json.dump(serializable_merges, f)

def load_tokenizer(config):
    with open(config["output"]["file_path"], 'r', encoding='utf-8') as f:
        serialized_merges = json.load(f)
        # Convert string keys back to tuples
        merges = {tuple(map(int, k.split(','))): v 
                        for k, v in serialized_merges.items()}
    
    return merges

if __name__ == "__main__":

    # TRAIN TOKENIZER
    config = load_config()
    print(f"configs: {config}")

    merges = tokenizer(config)
    print("Vocabulary size: ", len(merges))
    save(merges, config)

    validate_tokenizer("खालील आवृत्ती पहाण्यासाठी त्याच्या तारखेची कळ दाबावी. अधिक माहितीसाठी पहा", load_tokenizer(config), config)