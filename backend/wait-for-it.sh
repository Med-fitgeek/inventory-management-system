#!/usr/bin/env bash

host="$1"
port="$2"
shift 2
cmd="$@"

if [ -z "$host" ] || [ -z "$port" ]; then
  echo "Usage: $0 host port [cmd]"
  exit 1
fi

until nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 1
done

>&2 echo "$host:$port is available!"
exec $cmd
