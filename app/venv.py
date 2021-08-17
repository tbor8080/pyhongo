import os,sys,datetime,subprocess,platform
# venv_name=sys.arg[0]
platform=platform.platform().lower()
#subprocess.call('python -m venv %s' % venv_name, shell=True)

#activate=f'source ./{venv_name}/bin/activate'
    
#if 'windows' in platform:
    #activate=f'./{venv_name}/Scripts/activate'

#subprocess.call(f'{activate}', shell=True)
ret=subprocess.check_output('python --version',shell=True)
print(str(ret).replace("b'",'').replace("\n",''))

# flask install
ret=subprocess.check_output(f'pip list | grep Flask', shell=True)
_flask='flask' in str(ret).lower()
if _flask is not True:
    subprocess.call('pip install Flask', shell=True)
else:
    print('flask install:' in str(ret).lower())

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
