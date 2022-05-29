#!/bin/bash
set -e 

podman exec python bash -c 'gunicorn wsgi:application' -D &
podmon exec python run_chucknorris -D &
