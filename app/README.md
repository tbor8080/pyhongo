# Readme.md

	+ Automamtion Web Application Code
		- Now > CLI

#### [ Update ]:

    Update: 2021.08.23
    < Next Update to 2021.08.28 >

## Quick Start Application

    - Access Github Repository:
        - https://github.com/tbor8080/

        + [https] 
            > git clone https://github.com/tbor8080/pyhongo.git
        + [github CLI] 
            > gh repo clone tbor8080/pyhongo
        
    - Open the "Terminal(Linux/OSX) | Command Prompt(Windows)"

### [ How to Install ]:

    > python -m venv <VENV Directory Name>
    > pip -r requirements.txt
    > python ./installer.py

### [ Change Document Root ( doc_root ) ]:

    Open Editor(VsCode etc...) > installer.py
    Edit to variable < doc_root > is Your Enviroment.
    Save and File Close installer.py.

    command to.

    > python ./installer.py

    wait a little bit, ... install ....
    Success the Project File in installer.sh [directory]
        > [first_flask_app] 
            - install directory

    Coding Python File
        - install directory(document_root)

    run the [ Flask Application(WSGI)]
        + default:
            $ python [./first_flask_app]/main.py
        + go to browser:
            default: http://127.0.0.1:5000/

    run the [ Gunicorn ]
        + default:
            $ cd [./first_flask_app/]
            $ ./gunicorn_start
        + go to browser:
            default: http://127.0.0.1:8080/

    Go to access, Web browser!!

***

##### Cloned Thanx :) 
