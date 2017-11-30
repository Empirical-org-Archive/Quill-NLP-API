import spacy
nlp = spacy.load('en')

def get_POS(sentence):
  doc = nlp(sentence)
  pos_array = []
  for token in doc: 
    pos_array.append(token.pos_)
  return pos_array