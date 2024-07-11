import spacy
import sys, fitz
nlp = spacy.load('./model-best')
resume_data = nlp('my name is Kunal Tiwari. I worked at Microsoft. I havee 5 years of experience. I am skilled in machine learning and natural language processing.')
for ent in resume_data.ents:
     print(ent.text, "   ->>>>>>", ent.label_)
dictionaryTuple = {ent.label_: ent.text for ent in resume_data.ents}
print("ggggggggggggggggg  ",type(resume_data))
#print(resume_data['Name'])
if 'Name' in dictionaryTuple:
    print(dictionaryTuple['Name'], "  CHICKEN BUTT")

if 'Companies worked at' in dictionaryTuple:
    print(dictionaryTuple['Companies worked at'], "  CHICKEN BUTT")


if 'Skills' in dictionaryTuple:
    print(dictionaryTuple['Skills'], "  FAGGOT")

print("HI")



fname = './Uploaded_Resumes/Alice Clark CV.pdf'
doc = fitz.open(fname)
text = " "
for page in doc:
  text = text + str(page.get_text())
#print(text)
text = text.strip()
text = ' '.join(text.split())
doc = nlp(text)
for ent in doc.ents:
  print(ent.text, " ->>>>" , ent.label_)

dictionaryTuple = {ent.label_: ent.text for ent in doc.ents}


print(dictionaryTuple['Skills'], "  FAGGOT")