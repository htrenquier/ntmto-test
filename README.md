# Never tell me the odds
### developer test https://github.com/lioncowlionant/developer-test

Hi Han, the Millenium Falcon is ready to save the world once again.
You will only have to meet a few requirements:
 - Nodejs
 - Python 3



### In order to boot *c3po* (frontend):
The web application is at http://localhost:3000
```
cd c3po
npm i
npm start
```

### Booting the Millenium Falcon's onboard computer *mfalcon* (backend):
```
pip install django django-cors-headers
python manage.py test (optional)
python manage.py runserver
```

### Calling R2D2 (CLI):
```
python give-me-the-odds.py examples/example1/millennium-falcon.json examples/example1/empire.json
```
The CLI can also be called with the `-v` option to display the route found.

