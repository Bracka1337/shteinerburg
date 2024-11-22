import spacy

nlp = spacy.load("xx_ent_wiki_sm")
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
doc = nlp(text)
persons = []
organizations = []

for ent in doc.ents:
    if ent.label_ == "PER":
        persons.append(ent.text)
    elif ent.label_ == "ORG":
        organizations.append(ent.text)

print("Personvārdi:", persons)
print("Organizācijas:", organizations) 
