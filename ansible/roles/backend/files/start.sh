#!/bin/bash
set -e 

podman exec python run_web -D &
podman exec python run_chucknorris -D &
