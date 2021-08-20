import os,sys,datetime,subprocess,platform
from time import sleep
argv=sys.argv

def shell_return_code_replace(ret):
    if type(ret) is bytes:
        return str(ret).replace("b'",'').replace("\\n'",'')

if len(argv)>1:
    print('Create new VENV....')
    venv_name=argv[1]
    platform=platform.platform().lower()
    # print(venv_name)
    # ret=subprocess.check_output(f'python -m venv {venv_name}', shell=True)
    ret=subprocess.check_output('pwd', shell=True)
    # print(shell_return_code_replace(ret))
    sys.exit()
    activate=f'source ./{venv_name}/bin/activate'

    if 'windows' in platform:
        activate=f'./{venv_name}/Scripts/activate'

    subprocess.call(f'{activate}', shell=True)
    print('create venv success !!')
else:
    print('Error: Argument not founds!')
    print('> python venv.py [venv name]')
    print('program finish')
    sys.exit()

# flask install
ret=subprocess.check_output(f'pip list | grep Flask', shell=True)
_flask='flask' in str(ret).lower()
if _flask is not True:
    subprocess.call('pip install Flask', shell=True)
else:
    print('flask install:' in str(ret).lower())

sleep(3)

# selenium install / custom install
ret=subprocess.check_output(f'pip list | grep selenium', shell=True)
_selenium='selenium' in str(ret).lower()
if _selenium is not True:
    yn=input('May I Help you the pip install to selenium?[Y/n]')
    if yn.lower()=='y':
        subprocess.call('pip install selenium', shell=True)
    else:
        print('Skip the install to selenium.')
else:
    print('selenium install:' ,str(ret).lower())
