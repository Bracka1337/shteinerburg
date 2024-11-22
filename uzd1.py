from nltk.tokenize import word_tokenize
from collections import defaultdict

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
word_freq = defaultdict(int)

for word in words:
    word_freq[word] += 1

print("Word Frequency Analysis:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
