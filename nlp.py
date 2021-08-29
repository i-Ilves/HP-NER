import spacy

nlp = spacy.load("NER_1.0")


def getEntities(text):
  text_document = nlp(text['text'])
  cleaned_text = [token.text for token in text_document if not token.is_punct]
  cleaned_text = nlp(' '.join(cleaned_text))

  entities = []
  



  for entity in text_document.ents:
    if entity.label_ == text['type']:
       if entity.text not in entities:
        entities.append(entity.text)


  return entities

'''   for entity in text_document.ents:
    print(entity.text, entity.label_)
    entities.append(entity.text)
      
  return entities '''
'''     for entity in text_document.ents:      
      if text['type'] == 'ALL':
        entities.append(entity.text, entity.label_) '''