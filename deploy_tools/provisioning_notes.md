Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu(16.04):

    sudo apt-get install python-software-properties
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., 39.107.104.61

## Folder structure:
Assume we have a user account at /home/username

/home/username

└── sites

        └── SITENAME
            ├── databse
            ├── source
            ├── static
            └── virtualenv

