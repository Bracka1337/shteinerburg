from langdetect import detect

texts = [
    "Šodien ir saulaina diena.", 
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    lang = detect(text)
    print(f"Text: \"{text}\" -> Detected Language: {lang}")
