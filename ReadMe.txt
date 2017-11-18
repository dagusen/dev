Getting started 7:50

Start app 41:00

Rendering HTML 45:16

Render a Django Template 50:03

Context in Django Templates 59:19

Template inheritance 1:08:40

Include Template Tag 1:22:42

Reactivate Virtualenv 1:28:49

Class Based Views 1:30:03

Template View 1:38:32








# create virtualenv
mkdir name_of_VirEnv && cd name_of_VirEnv
virtualenv -p python3 .

# activate virtual env
source bin/activate

#install django and start project
pip install django==1.11.3

#start project
mkdir src && cd src
django-admin.py startproject name_of_project .

# create new settings
cd name_of_project
mkdir settings && cd settings

#creating __init__.py
echo "from .base import *

from .production import *

try:
   from .local import *
except:
   pass
" > __init__.py

#copy setting.py to dir settings then change base_dir to 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#create local settings (local.py) and make new (base.py & production.py) 

#some other common installations
pip install psycopg2
pip install gunicorn dj-database-url
pip install django-crispy-forms
pip install pillow
pip install django-mathfilters

# create requirements.txt 
pip freeze > requirements.txt

# run migration & create superuser
python manage.py migrate
python manage.py 

#github
echo "# dev" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/dagusen/dev.git
git push -u origin master