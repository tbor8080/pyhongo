# Readme.md

	+ Automamtion Web Application Code
		- Now > CLI

#### [ Update ]:

    Update: 2021.09.05
    - base class update.
    - cli installer custom.
    - flask & gunicorn setup.
    
    < Next Update to 2021.09.12 >

    I would like to ...
    
    + sqlite gui window
    + postgre sql gui window.
    + nginx & python fast cgi update.
    + deploy && service.
        - docker
        - github action
    + web service automation
        - shopping cart
        - ledge management

## [ Quick Start ]

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
    > python -m installer

### [ Change Document Root ( doc_root ) ]:

    change env no open file.  
    to command line.

    > python -m installer

    - install success,
    - browser open(auto),
    - serve flask application
    - stop(abort) applicatoion > ctrl+c

    Success the Project File in installer.sh [directory]
        > [first_flask_app] 
            - install directory

    Coding Python & Template File

        - install directory = document_root
            
            - main.py
            - templates/main.html
            - static/css
            - static/img
            - static/javascript

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

            default: http://127.0.0.1:5001/
        
        + log:
            [./first_flask_app/]
                - manage/logs/
                    - gunicorn_access_log
                    - gunicorn_error_log

    Go to access, Web browser!!

***

##### Cloned Thanx :) 
