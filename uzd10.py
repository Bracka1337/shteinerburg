from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt.lv-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(text, model, tokenizer):
    encoded_text = tokenizer.encode(text, return_tensors="pt", padding=True)
    translated = model.generate(encoded_text, max_length=512, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

lv_sentences = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

for sentence in lv_sentences:
    translated_sentence = translate_text(sentence, model, tokenizer)
    print(f"Latviešu: {sentence}")
    print(f"Tulkojums angļu valodā: {translated_sentence}")
    print("-" * 50)
