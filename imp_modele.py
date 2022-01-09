#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file to implement the modes created in models
from quizzapp.models import Images
from quizzapp.models import Questions
from quizzapp.models import Answers

file_handler=open('images.csv','r')
images=[]
for line in file_handler.readlines():
    images.append(line)
file_handler.close()

for i in images[1:]:
    name=i.split(',')[1]
    desc1=i.split(',')[2:len(i.split(','))-5]
    mic=i.split(',')[len(i.split(','))-5]
    cell=i.split(',')[len(i.split(','))-4]
    comp=i.split(',')[len(i.split(','))-3]
    d=i.split(',')[len(i.split(','))-2]
    org=i.split(',')[len(i.split(','))-1]
    desc=""
    for i in desc1:
        desc=desc+i
    if desc.startswith('"')==True:
        desc=desc[1:len(desc)-1]
    line=Images(image_name=name,description=desc,microscopy=mic,cell_type=cell,component=comp,doi=d,organism=org)
    line.save()

file_handler=open('question.csv','r')
questions=[]
for line in file_handler.readlines():
    questions.append(line)
file_handler.close()

for i in questions[1:]:
    quest=i.split(',')[1]
    cat=i.split(',')[2]
    im_fi=i.split(',')[3]
    p=i.split(',')[4]
    ans=i.split(',')[6]
    im=i.split(',')[7]
    line=Questions(question=quest,category=cat,imagefield=im_fi,points=p,n_answer=ans,n_image=im)
    line.save()

file_handler=open('answer.csv','r')
answers=[]
for line in file_handler.readlines():
    answers.append(line)
file_handler.close()

for i in answers[1:]:
    quest_id=i.split(',')[1]
    answ=i.split(',')[2]
    defi1=i.split(',')[3:len(i.split(','))]
    defi=""
    for i in defi1:
        defi=defi+i
    if defi.startswith('"')==True:
        defi=defi[1:len(defi)-2]
    line=Answers(question_id=quest_id,answer=answ,definition=defi)
    line.save()




