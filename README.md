##
# Django Learning Repo
##
### INSTALLATION & SETUP <br/>
__Environment Variables: py = '[path to python here]/python.exe'__
> py -m ensure pip --upgrade  
> py -m venv venv  
> Activate ENV: https://virtualenv.pypa.io/en/legacy/userguide.html#activate-script  
> py -m pip install --upgrade pip  

__Once pip is in your venv there is no need to reference the 'py' env var path__  
> pip install django  
> django-admin startproject '[project-name-here]'
> python manage.py migrate
> python manage.py createsuperuser
> 


##
### Python Best Practices
> * use source control, I prefer git  
> * .gitignore to prevent secret information leakage and excess clutter in source control program  
> * place "secret" values in .env, AND add .env to .gitignore  
> * add all packages to requirements.txt (https://stackoverflow.com/questions/41457612/how-to-fix-error-with-freetype-while-installing-all-packages-from-a-requirements/41458329#41458329)  
