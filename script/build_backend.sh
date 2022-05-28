#!/usr/bin/env bash
set -e

log() {
    echo "[SCRIPT] $1"
}

# Override python binary with first parameter: ./script/build_backend.sh /usr/local/bin/python3.9
PYTHON_BIN="${1:-python3}"
log "Using python: $PYTHON_BIN"

# Go into backend folder
log "cd into ./backend"

# Make sure we have python 3.5 or newer
log "Make sure we use python 3.5 or newer"
$PYTHON_BIN -c "import sys; assert sys.version_info >= (3, 5), 'Python 3.5 or newer is required to build. Currently using: {}'.format(sys.version_info)"

# Clear files in dist
log "Clear dist folder"
rm -rf dist/* || true

# rm venv
log "rm venv"
rm -rf venv/ || true

# Create venv
log "Creating venv"
cd /home/oh856/TO_TASK
virtualenv --python $PYTHON_BIN venv

# Update package tools in venv
log "Update package tools in venv"
venv/bin/pip install -U pip setuptools wheel build

# Build wheel dist for backend
log "Building wheel"
# "do not isolate the build in a virtual environment" because we are already in a venv
# "build a wheel" what we want to build

venv/bin/python -m build --no-isolation --wheel

# Copy wheel to expected location
log "Copy wheels to: ../ansible/roles/backend/files/"
cp dist/*.whl ansible/roles/backend/files/


log "######################################################### NEW BUILD CREATED, AND COPIED TO ANSIBLE FILES DIRECTORY IN ORDER TO BE DEPLOYED   ################################################"