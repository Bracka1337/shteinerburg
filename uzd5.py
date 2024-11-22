import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_text_properly(text):
    text = re.sub(r"@(\w+):", r"\1:", text)
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"!+", "!", text)
    text = re.sub(r"\?+", "?", text)
    text = re.sub(r"[^\w\s.,!?āčēģīķļņōŗšūžĀČĒĢĪĶĻŅŌŖŠŪŽ:]", "", text)
    text = re.sub(r"\s+", " ", text).strip() 

    return text

cleaned_text = clean_text_properly(raw_text)
print(f"Cleaned Text: \"{cleaned_text}\"")
