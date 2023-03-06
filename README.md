# Django-Basic-Setup-Demonstration

A basic demonstration of my abilities to setup a Django Application, utilizing Quentin Tarantino film titles, release dates, and descriptions as data.

I will be utilizing VSCODE as my environment.

I will run through this installation numbering my steps and bulleting my terminal inputs and outputs. This will assist those looking to install django in understanding what commands are required, and what responses they should expect.

For a full description, documentation, and more on the Django Framework, please visit their website sited here:
https://www.djangoproject.com/

1. First, run pip install django to install the Django.

Terminal:
Django-Basic-Setup-Demonstration git:(main) pip install django

In this case, the installation went smoothly with no issues.

2. Next, run python -m django version to verify the current Django version you are utilizing.

Django-Basic-Setup-Demonstration git:(main) ✗ python3 -m django version
4.1.7

Here we confirmed the version we are running is 4.1.7 - As of the creation of this demonstration, this IS the most up-to-date version of Django available.

3. Once this has been confirmed, I will start a django project by utilizing the django-admin command "start project"

Django-Basic-Setup-Demonstration git:(main) ✗ django-admin startproject djangodemo

Here, you will see
