Estudos baseados em https://www.udemy.com/course/python-3-na-web-com-django-basico-intermediario

# Install pip first

`sudo apt-get install python3-pip`

# to install package

`pip3 install package_name`

# setup few more packages and development tools

`sudo apt-get install build-essential libssl-dev libffi-dev python-dev`

# Then install virtualenv

`sudo apt-get install -y python3-venv`

# Now create a virtual environment

`python3 -m venv venv`

# Activate venv
`source ./venv/bin/activate`

# Install DJANGO
`pip install django`

# Create a project
```
python
    import django
    django.get_version()
    exit()
django-admin.py startproject <myproject>
```

# Run server
`
cd <myproject>
python manage.ý runserver`
