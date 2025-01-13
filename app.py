import gradio as gr
import sys
import os

# Add parent directory to path to import tokenizer module
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tokenizer import load_config, load_tokenizer, validate_tokenizer, decode

# Load config and tokenizer once at startup
config = load_config()
merges = load_tokenizer(config)

def process_text(input_text):
    # Validate and get tokens
    token_len, encoded_tokens, decoded_string = validate_tokenizer(input_text, merges, config)
    return token_len, encoded_tokens, decoded_string

def decode_token_array(token_array_str):
    try:
        # Convert string input to list of tokens
        tokens = [token.strip() for token in token_array_str.strip('[]').split(',') if token.strip()]
        # Convert string tokens to integers
        token_ids = [int(token) for token in tokens]
        # Decode using config
        #decoded_text = config.decode(token_ids)
        # print("token_ids: ", token_ids)

        decoded_string = decode(token_ids, merges)

        return decoded_string
    except Exception as e:
        return f"Error: Please enter valid token IDs in format [1,2,3]. Error: {str(e)}"

# Sample Marathi texts for demonstration
sample_texts = [
    "मी आज बागेत फिरायला गेलो.",
    "टाटा खुली बॅडमिंटन स्पर्धा सुरू झाली आहे.",
    "महाराष्ट्र माझा गौरवशाली राज्य आहे.",
]

# Create Gradio interface with multiple components
with gr.Blocks(title="Marathi Text Tokenizer") as demo:
    gr.Markdown("# Marathi Text Tokenizer")
    
    with gr.Tab("Encoder"):
        # First row - Text to Tokens
        gr.Markdown("### Encode Text to Tokens")
        with gr.Row():
            input_text = gr.Textbox(
                label="Enter Marathi Text",
                placeholder="येथे मराठी मजकूर टाइप करा...",
                lines=5
            )
        with gr.Row():
            token_count = gr.Number(label="Number of Tokens", precision=0)
            token_ids = gr.Textbox(label="Encoded Token IDs", lines=5)
            decoded_verify = gr.Textbox(label="Decoded Text Verification", lines=2)
        encode_btn = gr.Button("Encode Text")
        encode_btn.click(
            fn=process_text,
            inputs=[input_text],
            outputs=[token_count, token_ids, decoded_verify]
        )
        
        # Examples
        gr.Examples(
            examples=sample_texts,
            inputs=input_text,
            outputs=[token_count, token_ids, decoded_verify],
            fn=process_text
        )

    with gr.Tab("Decoder"):
        
        # Second row - Tokens to Text
        gr.Markdown("### Decode Tokens to Text")
        with gr.Row():
            token_array_input = gr.Textbox(
                label="Enter Token Array",
                placeholder="Enter tokens as [1,2,3,4,5]",
                lines=2
            )
            decoded_output = gr.Textbox(
                label="Decoded Text",
                lines=2
            )
        decode_btn = gr.Button("Decode Tokens")
        decode_btn.click(
            fn=decode_token_array,
            inputs=[token_array_input],
            outputs=[decoded_output]
        )

if __name__ == "__main__":
    demo.launch()