import spacy
from scipy.spatial.distance import cosine

nlp = spacy.load("xx_ent_wiki_sm")
words = ["māja", "dzīvoklis", "jūra"]
vectors = [nlp(word).vector for word in words]
similarities = {}

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        sim = 1 - cosine(vectors[i], vectors[j])
        similarities[(words[i], words[j])] = sim

for pair, similarity in similarities.items():
    print(f"Similarity between '{pair[0]}' and '{pair[1]}': {similarity:.4f}")
