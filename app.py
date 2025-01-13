import gradio as gr
import sys
import os

# Add parent directory to path to import tokenizer module
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tokenizer import load_config, load_tokenizer, validate_tokenizer

# Load config and tokenizer once at startup
config = load_config()
merges = load_tokenizer(config)

def process_text(input_text):
    # Validate and get tokens
    token_len, encoded_tokens, decoded_string = validate_tokenizer(input_text, merges, config)
    return token_len, encoded_tokens, decoded_string

# Sample Marathi texts for demonstration
sample_texts = [
    "मी आज बागेत फिरायला गेलो.",
    "टाटा खुली बॅडमिंटन स्पर्धा सुरू झाली आहे.",
    "महाराष्ट्र माझा गौरवशाली राज्य आहे.",
]

# Create Gradio interface
demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(
        label="Enter Marathi Text",
        placeholder="येथे मराठी मजकूर टाइप करा...",
        lines=5
    ),
    outputs=[
        gr.Number(label="Number of Tokens", precision=0),
        gr.JSON(label="Encoded Token IDs"),
        gr.Textbox(label="Decoded Text", lines=2)
    ],
    title="Marathi Text Tokenizer",
    description="Enter Marathi text to see its tokenization results.",
    examples=sample_texts
)

if __name__ == "__main__":
    demo.launch()