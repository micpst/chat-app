#!/bin/bash

docker compose -p development -f compose/docker-compose-development.yml --env-file env/.env.development run --rm backend ./manage.py test
