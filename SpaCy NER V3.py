from spacy.training.example import Example

# prepare an empty model to train
nlp = spacy.blank('en')
#nlp.vocab.vectors.name = 'demo'
ner=nlp.create_pipe('ner')
nlp.add_pipe('ner')

labels=['DEGREE','SPECIALIZATION','DURATION','INSTITUTION NAME','GRADE']
for LABEL in labels:
    ner.add_label(LABEL)
# Add the custome NER Tags as entities into the model


optimizer = nlp.begin_training()

for iter in range(30):
  losses = {}
  for text, annotations in training_data["annotations"]:
    if len(text) > 0:
      doc = nlp.make_doc(text)
      example = Example.from_dict(doc, annotations)
      nlp.update([example],drop=0.2, sgd=optimizer, losses = losses)
      print(losses)
