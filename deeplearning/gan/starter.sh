#!/bin/bash

# if there is no existing virtual environment, create one

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# activate the virtual environment
source venv/bin/activate

# install the required packages
pip install -r requirements.txt