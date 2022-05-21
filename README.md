# Chat Application

A simple chat application written using Flask API with Socket.io.

## Quick start

### Spin up containers
```
$ ./scripts/compose.sh development up -d
```

### Apply migration
```
$ ./scripts/migrate.sh development
```

### Terminate all running containers
```
$ ./scripts/compose.sh development down
```

### Run tests
```
$ ./scripts/test.sh
```

## License
All my code is MIT licensed. Libraries follow their respective licenses.