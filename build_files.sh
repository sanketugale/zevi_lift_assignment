#!/bin/bash

# Use the Python and pip binaries provided by the @vercel/python builder
PYTHON_BIN="/opt/python3.9/bin/python3.9"
PIP_BIN="/opt/python3.9/bin/pip3.9"

# Install Django and the requirements
$PIP_BIN install django
$PIP_BIN install -r requirements.txt