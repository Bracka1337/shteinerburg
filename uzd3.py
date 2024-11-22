from textblob import TextBlob

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

blob1 = TextBlob(text1)
blob2 = TextBlob(text2)

words_text1 = set(word.lower() for word in blob1.words if word.isalpha())
words_text2 = set(word.lower() for word in blob2.words if word.isalpha())

common_words = words_text1.intersection(words_text2)

matching_percentage = (len(common_words) / len(words_text1.union(words_text2))) * 100

print(f"Common words: {common_words}") 
print(f"Matching percentage: {matching_percentage:.2f}%")
