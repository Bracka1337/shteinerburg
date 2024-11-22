from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs.",
    "Nah bro, sis ir ceturtais ko es meginu, es esmu done bro vins vel 5 starus dabon :sob:"
]

def map_sentiment(score):
    if score > 3: 
        return "positive"
    elif score < 3 and not score == 1:
        return "neutral"
    else:
        return "negative"

for sentence in sentences:
    result = sentiment_analysis(sentence)[0]
    stars = int(result['label'].split()[0])
    sentiment = map_sentiment(stars, sentence)
    print(f"Sentence: \"{sentence}\" -> Sentiment: {sentiment} ({stars} stars)")
