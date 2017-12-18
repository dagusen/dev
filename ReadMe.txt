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

Remembering Things with Models 1:46:05

More on Model Fields 1:57:11

Displaying Saved Data 2:06:12

Understanding Querysets 2:16:03

Generic List View 2:25:20

Restaurant Profile Detail 2:34:21

SlugField & the Unique Slug Generator 2:44:39

Signal for Unique Slugs 2:51:44

Slugs as URL Params 2:58:23

Get single Items from the database 3:00:48

Saving Data the Hard + Wrong Way 3:12:09

The Power of Django Forms 3:30:51

The Extra Power of Django Model Forms 3:40:00

Simple + Effective Validation 3:47:37

Letting Users Own Data 3:59:58

Associate User to Form data in FBV 4:18:05

Associate User to Data in Class Based View 4:23:34

Login Required to View 4:28:17

Login View 4:34:20

Using Reverse to Shortcut URL's 4:43:35

Menu items App 4:56:51

Menu Item Views 5:07:55




------------------- Python Shell -------------------

-import table from database
from restaurants.models import RestaurantLocation

-show all data from database
RestaurantLocation.objects.all()

-iterate data from database
for obj in RestaurantLocation.objects.all():
	print(obj.name)

-making a qs and filter
qs = RestaurantLocation.objects.all()
qs.filter(category__iexact='mexican')

-update data from database
qs.update(category='American')
qs
qs.filter(category__iexact='mexican')


-adding data in the database
obj = RestaurantLocation()
obj.name = "Pei Wei"
obj.location = "Newport Beach"
obj.category = "Asian Fusion"
obj.save

or

obj = RestaurantLocation.objects.create(name='Chronic Tacos', location='Corona Del Mar', category='Mexican')
obj
obj.timestamp

-show obj
obj
obj.name ...

-showing qs
qs2 = RestaurantLocation.objects.filter(category__iexact='mexican')
qs2
qs2.exists()
qs2.count()

-another qs exclude
qs = RestaurantLocation.objects.filter(category__iexact='mexican').exclude(name__icontains='Tacos')
qs

-slug
from restaurants.models import RestaurantLocation
obj = RestaurantLocation.objects.get(id=1)
from restaurants.utils import unique_slug_generator
print(unique_slug_generator(obj))


-Get single Items from the database
from restaurants.models import RestaurantLocation
qs = RestaurantLocation.objects.all()
qs
qs.first()
qs.last()
qs.[position of the data]
qs = RestaurantLocation.objects.filter(category__iexact='mexican')
qs.first()
qs.last()

from django.shortcuts import get_object_or_404
obj = RestaurantLocation.objects.get(pk=12000)

exception

try:
	obj = RestaurantLocation.objects.get(pk=12000)
except:
	print("Not found")


qs = RestaurantLocation.objects.filter(slug='baja-fist-tacos')
if qs.exists():
	print(qs.first())

View owners data | user model

from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all()
admin = User.objects.get(id=1)
admin.username
instance = admin
instance
instance.restaurantlocation_set.all()
instance.restaurantlocation_set.filter(category__iexact='Mexican')

from restaurant.models import RestaurantLocation
RestaurantLocation.objects.filter(owner__id=1)
RestaurantLocation.objects.filter(owner__username__iexact='admin')

qs = RestaurantLocation.objects.filter(owner__username__iexact='admin')
obj = qs.first()
obj.owner
User = obj.owner.__class__
User
User.objects.all() 
admin = User.objects.all().first()
admin = User.objects.all()
new_qs = admin.restaurantlocation_set.all()
new _obj = new_qs.first()
new_obj
RK = new_obj.__class__
RK.objects.all()



-----------------------------------------------------------



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