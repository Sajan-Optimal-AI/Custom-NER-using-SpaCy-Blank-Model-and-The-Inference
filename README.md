# Custom-NER-using-SpaCy-Blank-Model-and-The-Inference

# Training Data Sample:
{'annotations': [['Completed B. TECH in the stream of Computer science and Engineering in 2015.',
   {'entities': [[10, 17, 'DEGREE'],
     [35, 67, 'SPECIALIZATION'],
     [71, 75, 'DURATION']]}],
  ['B.Tech in duration between July 2007 to June 2011 in Marudhar Engg College',
   {'entities': [[0, 9, 'DEGREE'],
     [27, 50, 'DURATION'],
     [54, 76, 'INSTITUTION NAME']]}],
  ['Graduated from University in Computer Science & Engineering.',
   {'entities': [[16, 26, 'INSTITUTION NAME'], [30, 60, 'SPECIALIZATION']]}],
  ['Bachelor of Technology in Electronics and Communication Engineering at Amrita University',
   {'entities': [[0, 22, 'DEGREE'],
     [26, 67, 'SPECIALIZATION'],
     [72, 89, 'INSTITUTION NAME']]}]
  'classes': ['DEGREE',
  'SPECIALIZATION',
  'DURATION',
  'INSTITUTION NAME',
  'GRADE']}
  
# Training Data Preparation:
https://arunmozhi.in/2020/12/19/ner-annotator-ner-tagger-for-spacy/
![image](https://user-images.githubusercontent.com/82649993/140767533-f06d28d5-ec56-4919-8944-d926be9adbeb.png)
>>>>Follow these link to produce Training Data.More instances wil result more performance.
# Inference:
my_list = ['Bachelor of Technology in Information Technology from Bengal College of Engineering and Technology affiliated to University and  passed out in the year 2016 with 75 percentage.','B.Sc in Computer Sceince at Sundaram College of technology.']

The Entities are;
[{'DEGREE': 'Bachelor of Technology',
  'DURATION': '2016',
  'GRADE': '75 percentage',
  'INSTITUTION NAME': 'Bengal College of Engineering and Technology',
  'SPECIALIZATION': 'Information Technology'},
 {'DEGREE': 'B.Sc',
  'INSTITUTION NAME': 'Sundaram College of technology',
  'SPECIALIZATION': 'Computer Sceince'}]
