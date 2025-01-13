# Marathi Text Tokenizer

A web interface for tokenizing Marathi text and decoding token IDs using Gradio.

## Project Structure 
```
├── data/ # Data files (ignored by git)
├── huggingface/ # Gradio web application
│ └── app.py # Main Gradio application
├── tokenizer.py # Tokenizer implementation
├── validator.py # Tokenizer validation
├── .gitignore # Git ignore file
└── README.md # This file
```

## Requirements

Install the required packages:
```bash
pip install gradio
```

## Running the Application

1. Clone the repository:
```bash:README.md
git clone <repository-url>
cd <repository-name>
```

2. Start the Gradio web interface:
```bash
cd huggingface
python app.py
```

3. Open your web browser and navigate to:
```
http://127.0.0.1:7860
```

## Using the Interface

The application provides two main functionalities in separate tabs:

### 1. Encode Text Tab
- Enter Marathi text in the input box
- Click "Submit" to see:
  - Number of tokens
  - Encoded token IDs
  - Decoded text (verification)
- Sample Marathi texts are provided for testing

Example input:
```
टाटा खुली बॅडमिंटन स्पर्धा
```

### 2. Decode Tokens Tab
- Enter token IDs as a list
- Click "Submit" to see the decoded Marathi text

Example input:
```
[1, 2, 3, 4, 5]
```

## Sample Texts

The application includes several sample Marathi texts for testing:
- मी आज बागेत फिरायला गेलो.
- टाटा खुली बॅडमिंटन स्पर्धा सुरू झाली आहे.
- महाराष्ट्र माझा गौरवशाली राज्य आहे.

## Development

To modify the interface:
1. Edit `huggingface/app.py`
2. The application will auto-reload when running in development mode

## Deployment

The application can be deployed to Hugging Face Spaces:
1. Create a new Space on Hugging Face
2. Push the code to the Space repository
3. The application will automatically deploy

## Troubleshooting

Common issues and solutions:

1. Port already in use:
```bash
# Use a different port
python app.py --port 7861
```

2. Memory issues:
```bash
# Limit memory usage
python app.py --memory-limit 4096
```

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable]


## Logs
```
(venv) sawan.darekar@MAC-XHXW23XJ7N era_v3_assignment_11 % python tokenizer.py
configs: {'input': {'file_path': 'resources/mr-train.txt', 'lines_to_read': 10}, 'output': {'file_path': 'resources/mr-train.tokens'}, 'vocab_size': 2000, 'token_regex': ''}
input_text_char_length: 7321896
input_text_char_length: 7321896
limited_input_text_char_length: 13

 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_`abcdefghijklmnopqrstuvwxyz·×éìí÷αँंःअआइईउऊऋऍएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसह़ऽािीुूृॄॅेैॉोौ्ॐॠ।॥०१२३४५६७८९ॲ–—‘’“”•…■⦁
vocab_size: 186
char To Integer:  {'\n': 0, ' ': 1, '!': 2, '"': 3, '#': 4, '$': 5, '%': 6, '&': 7, "'": 8, '(': 9, ')': 10, '*': 11, '+': 12, ',': 13, '-': 14, '.': 15, '/': 16, '0': 17, '1': 18, '2': 19, '3': 20, '4': 21, '5': 22, '6': 23, '7': 24, '8': 25, '9': 26, ':': 27, ';': 28, '<': 29, '=': 30, '>': 31, '?': 32, '@': 33, 'A': 34, 'B': 35, 'C': 36, 'D': 37, 'E': 38, 'F': 39, 'G': 40, 'H': 41, 'I': 42, 'J': 43, 'K': 44, 'L': 45, 'M': 46, 'N': 47, 'O': 48, 'P': 49, 'Q': 50, 'R': 51, 'S': 52, 'T': 53, 'U': 54, 'V': 55, 'W': 56, 'X': 57, 'Y': 58, 'Z': 59, '_': 60, '`': 61, 'a': 62, 'b': 63, 'c': 64, 'd': 65, 'e': 66, 'f': 67, 'g': 68, 'h': 69, 'i': 70, 'j': 71, 'k': 72, 'l': 73, 'm': 74, 'n': 75, 'o': 76, 'p': 77, 'q': 78, 'r': 79, 's': 80, 't': 81, 'u': 82, 'v': 83, 'w': 84, 'x': 85, 'y': 86, 'z': 87, '·': 88, '×': 89, 'é': 90, 'ì': 91, 'í': 92, '÷': 93, 'α': 94, 'ँ': 95, 'ं': 96, 'ः': 97, 'अ': 98, 'आ': 99, 'इ': 100, 'ई': 101, 'उ': 102, 'ऊ': 103, 'ऋ': 104, 'ऍ': 105, 'ए': 106, 'ऐ': 107, 'ऑ': 108, 'ओ': 109, 'औ': 110, 'क': 111, 'ख': 112, 'ग': 113, 'घ': 114, 'ङ': 115, 'च': 116, 'छ': 117, 'ज': 118, 'झ': 119, 'ञ': 120, 'ट': 121, 'ठ': 122, 'ड': 123, 'ढ': 124, 'ण': 125, 'त': 126, 'थ': 127, 'द': 128, 'ध': 129, 'न': 130, 'प': 131, 'फ': 132, 'ब': 133, 'भ': 134, 'म': 135, 'य': 136, 'र': 137, 'ल': 138, 'ळ': 139, 'व': 140, 'श': 141, 'ष': 142, 'स': 143, 'ह': 144, '़': 145, 'ऽ': 146, 'ा': 147, 'ि': 148, 'ी': 149, 'ु': 150, 'ू': 151, 'ृ': 152, 'ॄ': 153, 'ॅ': 154, 'े': 155, 'ै': 156, 'ॉ': 157, 'ो': 158, 'ौ': 159, '्': 160, 'ॐ': 161, 'ॠ': 162, '।': 163, '॥': 164, '०': 165, '१': 166, '२': 167, '३': 168, '४': 169, '५': 170, '६': 171, '७': 172, '८': 173, '९': 174, 'ॲ': 175, '–': 176, '—': 177, '‘': 178, '’': 179, '“': 180, '”': 181, '•': 182, '…': 183, '■': 184, '⦁': 185}
Integer to char:  {0: '\n', 1: ' ', 2: '!', 3: '"', 4: '#', 5: '$', 6: '%', 7: '&', 8: "'", 9: '(', 10: ')', 11: '*', 12: '+', 13: ',', 14: '-', 15: '.', 16: '/', 17: '0', 18: '1', 19: '2', 20: '3', 21: '4', 22: '5', 23: '6', 24: '7', 25: '8', 26: '9', 27: ':', 28: ';', 29: '<', 30: '=', 31: '>', 32: '?', 33: '@', 34: 'A', 35: 'B', 36: 'C', 37: 'D', 38: 'E', 39: 'F', 40: 'G', 41: 'H', 42: 'I', 43: 'J', 44: 'K', 45: 'L', 46: 'M', 47: 'N', 48: 'O', 49: 'P', 50: 'Q', 51: 'R', 52: 'S', 53: 'T', 54: 'U', 55: 'V', 56: 'W', 57: 'X', 58: 'Y', 59: 'Z', 60: '_', 61: '`', 62: 'a', 63: 'b', 64: 'c', 65: 'd', 66: 'e', 67: 'f', 68: 'g', 69: 'h', 70: 'i', 71: 'j', 72: 'k', 73: 'l', 74: 'm', 75: 'n', 76: 'o', 77: 'p', 78: 'q', 79: 'r', 80: 's', 81: 't', 82: 'u', 83: 'v', 84: 'w', 85: 'x', 86: 'y', 87: 'z', 88: '·', 89: '×', 90: 'é', 91: 'ì', 92: 'í', 93: '÷', 94: 'α', 95: 'ँ', 96: 'ं', 97: 'ः', 98: 'अ', 99: 'आ', 100: 'इ', 101: 'ई', 102: 'उ', 103: 'ऊ', 104: 'ऋ', 105: 'ऍ', 106: 'ए', 107: 'ऐ', 108: 'ऑ', 109: 'ओ', 110: 'औ', 111: 'क', 112: 'ख', 113: 'ग', 114: 'घ', 115: 'ङ', 116: 'च', 117: 'छ', 118: 'ज', 119: 'झ', 120: 'ञ', 121: 'ट', 122: 'ठ', 123: 'ड', 124: 'ढ', 125: 'ण', 126: 'त', 127: 'थ', 128: 'द', 129: 'ध', 130: 'न', 131: 'प', 132: 'फ', 133: 'ब', 134: 'भ', 135: 'म', 136: 'य', 137: 'र', 138: 'ल', 139: 'ळ', 140: 'व', 141: 'श', 142: 'ष', 143: 'स', 144: 'ह', 145: '़', 146: 'ऽ', 147: 'ा', 148: 'ि', 149: 'ी', 150: 'ु', 151: 'ू', 152: 'ृ', 153: 'ॄ', 154: 'ॅ', 155: 'े', 156: 'ै', 157: 'ॉ', 158: 'ो', 159: 'ौ', 160: '्', 161: 'ॐ', 162: 'ॠ', 163: '।', 164: '॥', 165: '०', 166: '१', 167: '२', 168: '३', 169: '४', 170: '५', 171: '६', 172: '७', 173: '८', 174: '९', 175: 'ॲ', 176: '–', 177: '—', 178: '‘', 179: '’', 180: '“', 181: '”', 182: '•', 183: '…', 184: '■', 185: '⦁'}
limited_input_text:  aaabdaabdaacd
Initial token length 19187725
unique tokens  152
Example tokens:  2325 क 2404 ।
Train the tokenizer
num_merges: 1744
Iteration 100: compression ratio: 3.58X                                                                                                                                                                                                            
Iteration 200: compression ratio: 4. 25X                                                                                                                                                                                                            
Iteration 300: compression ratio: 4.73X                                                                                                                                                                                                            
Iteration 400: compression ratio: 5.09X                                                                                                                                                                                                            
Iteration 500: compression ratio: 5.38X                                                                                                                                                                                                            
Iteration 600: compression ratio: 5.63X                                                                                                                                                                                                            
Iteration 700: compression ratio: 5.86X                                                                                                                                                                                                            
Iteration 800: compression ratio: 6.06X                                                                                                                                                                                                            
Iteration 900: compression ratio: 6.23X                                                                                                                                                                                                            
Iteration 1000: compression ratio: 6.40X                                                                                                                                                                                                           
Iteration 1100: compression ratio: 6.55X                                                                                                                                                                                                           
Iteration 1200: compression ratio: 6.69X                                                                                                                                                                                                           
Iteration 1300: compression ratio: 6.81X                                                                                                                                                                                                           
Iteration 1400: compression ratio: 6.93X                                                                                                                                                                                                           
Iteration 1500: compression ratio: 7.04X                                                                                                                                                                                                           
Iteration 1600: compression ratio: 7.15X                                                                                                                                                                                                           
Iteration 1700: compression ratio: 7.26X                                                                                                                                                                                                           
Training tokenizer: 100%|█████████████████████████████████████████████████████████████| 1744/1744 [45:51<00:00,  1.58s/it]
tokens length: 19187725
ids length: 2628465
compression ratio: 7.30X
Vocabulary size:  1744
test_string:  खालील आवृत्ती पहाण्यासाठी त्याच्या तारखेची कळ दाबावी. अधिक माहितीसाठी पहा
encoded-token-size:  29
encoded-token-ids:  [414, 314, 348, 296, 291, 1369, 466, 287, 376, 652, 419, 609, 164, 847, 408, 349, 328, 342, 482, 316, 264, 46, 1333, 305, 848, 1959, 466, 287, 259]
decoded_string:  खालील आवृत्ती पहाण्यासाठी त्याच्या तारखेची कळ दाबावी. अधिक माहितीसाठी पहा

```