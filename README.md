# Olympics2024-Dashboard

## Setting up backend
```
$ cd .\django\
$ py -m venv venv
$ cd .\venv\
$ .\venv\Scripts\activate
$ pip install -r .\requirements.txt
```

## Setting up frontend
```
$ cd .\frontend\
$ npm install
$ npm start
```

## Database migration
```
$ cd .\django\
$ .\venv\Scripts\activate
$ python .\manage.py makemigration
$ python .\manage.py migrate
```