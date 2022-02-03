# Agenda app for Phenux CMS

## Installation
In apps folder of phenux-cms :
```bash
git clone git@github.com:AuroreMariscal/phenux-apps-agenda.git agenda
```

Add this code in INSTALLED_APPS of settings.py of phenux-cms :
```bash
    #Apps
    ...
    'apps.agenda.plugins', # Name used in apps.py 
    'apps.agenda.event' # Name used in apps.py
```