import re
import string

def clean_text(text):
    # Check if text is a string; if it's NaN or None, return an empty string
    if not isinstance(text, str):
        return ""
    
    # Now safe to lowercase
    text = text.lower()
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Optional: Remove extra whitespace
    text = text.strip()
    
    return text