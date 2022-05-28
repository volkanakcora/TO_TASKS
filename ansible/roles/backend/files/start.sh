#!/bin/bash
podman exec python run_web -D &
podmon exec python run_chucknorris -D &
