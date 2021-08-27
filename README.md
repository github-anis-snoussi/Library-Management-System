# Library Management System
A Library Management System made with Python & PyQt5

![](demo.gif)

## Is this app good to use ?
this app has 
 - no controls over input
 - poor database management 
 - some serious security vulnerabilities
so NO, this app is not good to use, but only to be taken as an example.

## Why  did I make it then
Good question ! very good question indeed ! <br /> 
this app was made during the quarantine caused by the COVID-19 outbreak ! <br /> 
it was a way for me to learn new stuff (obviously I'm not talking about good coding practices xD), I'm talking about GUIs in python, and how to make it into an exe and install it on a client machine. (it can also export data to exel file..... just saying.....) <br /> 
that's why I'm going to repeat this one last time: this app is EXTREMELY stupid and vulnerable! so don't judge me !!!!

# The Important Stuff that I should remember :

here I explain how to install the database on a client machine and how to export this project to an exe file:

## install database on client machine

- Install MYSQL server on client machine
- export database from my machine and copy sql file and run on client machine


## Convert Project to exe

to not mess with my existing project files, I copied the one I'll work on to ready_for_exe folder

- install cx_Freeze ($pip install cx_Freeze)
- convert ui files to python files ($pyuic5 library.ui -o library.py)
- change ui imports in index.py (from library import Ui_MainWindow)
- remove these 2 line: (ui,_ = loadUiType('library.ui')  login,_ = loadUiType('login.ui'))
- make necessary changes in classes definition index.py (class Login(QWidget , login):) becomes : (class Login(QWidget , Ui_Form):)
- use the setup file given in the repo like so: ($python setup.py build)
- VOILA ! a new build folder will apear with working app inside

NOW, how to convert those file to an exe:

- download Inno Setup (https://jrsoftware.org/isinfo.php) and install it ..
- Create a new script using the script wizard
- fill necessary details
- for main executable file choose index.exe (DUH !!!!)
- click add files and choose all the files / add folders and choose all folders



### Some random stuff I wrote to keep track... 

Library System :
    - add new book
    - aditing book
    - deleting book
    - catagories
    - search
    - users , login , signup
    - settings [catagories , author , publisher]
    - day to day operations
    - reports [exel files]

book :
    - book code
    - title
    - desc
    - catagory
    - price
    - author
    - publisher

users :
    - username
    - password
    - email address

day_to_day :
    - book
    - retreive / rent
    - days

catagory :
    - name
author :
    - name
publisher :
    - name
