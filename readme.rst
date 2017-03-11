ChamberlinSax Project

About

ChamberlinSax is intended for the personal use of Michael Chamberlin as a vlog/audiosample sharing site
for networking purposes.

Prerequisites

Python 3.5
pip
virtualenv (virtualenvwrapper is recommended)

Installation

To setup a local development environment:

virtualenv {{environment name}}
source {{environment name}}/bin/activate

pip install -r requirements.txt
edit settings.py to meet your local development requirements

./manage.py makemigrations home listen blog
./manage.py migrate
./manage.py runserver