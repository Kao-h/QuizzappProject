This is the code of a web site which presents a quizz about microscopy image identification & biological subject
  
The user has the choice to select the desired quiz (recognize types of microscopy - several levels, recognize the
levels, recognizing the presented cell type, presented organelles).

The user can also pick a random quizz and get detailled information about the images.
The user can also create a profile and login.
The information for the images is retrieved from the Cell Image Library website.  

To start :
Open a terminal.  
Place yourself in the location of the quizz folder   

#Requirement  
![Python 3.9.5](https://img.shields.io/badge/Python-3.9.5-blue.svg) 
## 1. Create conda environement
```bash
conda create --name djangoenv python=3.9
conda install --name djangoenv django
conda install --name djangoenv sqlparse
```
##2. Open conda environement named djangoenv
```bash
conda activate djangoenv
```
##3. Launch server
```bash
python manage.py runserver
```
##4. open HTML page at this adress or click [here](http://127.0.0.1:8000/)
```
http://127.0.0.1:8000/
```
###Here you have several options while navigating in the website  
### You can follow this :
1. Create an account
   1. Menu
   2. Register
2. Login with your name and password
3. Try a random quizz : we will surprise you 
4. Choose one type of quizz : 

   1. Menu
   2. Choose Quizz
   3. Microcopy / Biological context
   4. Have fun
5. Explore all the images and their description:
   1. Menu
   2. Choose Quizz
   3. Menu
   4. Explore
   
