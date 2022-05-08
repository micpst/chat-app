# Chat Application

A simple chat application written using Flask API with Socket.io.

## Quick start

### Install requirements
```
$ pip install -r requirements.txt
```

### Spin up containers
```
$ py manage.py compose up -d
```

### Create application database
```
$ py manage.py create-initial-db
```

### Apply migration
```
$ py manage.py flask db upgrade
```

### Terminate all running containers
```
$ py manage.py compose down
```

## License
All my code is MIT licensed. Libraries follow their respective licenses.