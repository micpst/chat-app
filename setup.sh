#!/bin/bash

env=$1
env_file="env/.env."$env
compose_file="compose/"$env".yml"

if [ ! -f "$env_file" ]; then
  echo "File" "$env_file" "does not exist."
  exit 1
fi

if [ ! -f "$compose_file" ]; then
  echo "File" "$compose_file" "does not exist."
  exit 1
fi

docker compose -p "$env" -f "$compose_file" --env-file "$env_file" up -d
