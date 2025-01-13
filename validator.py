from tokenizer import load_config, load_tokenizer, validate_tokenizer

# Load config first
config = load_config()

# Now use the loaded config to load tokenizer and validate
validate_tokenizer(
    "टाटा खुली बॅडमिंटन स्पर्धा टाटा खुल्या बॅडमिंटन", 
    load_tokenizer(config), 
    config
)