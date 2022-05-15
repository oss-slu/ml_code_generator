# ml_code_generator

## Install dependencies (only one time)
The instructions below assume that python3 and pip3 refer to Python 3.x and Pip 3.x. Depending on how things are configured, you may need to use python and pip commands instead of python3 and pip3.
1. Create a virtual environment: python3 -m venv venv
2. Activate virtual environment: 
   * Mac or Linux: source venv/bin/activate
   * Windows: source venv/Scripts/activate
3. Install dependencies: pip3 install -r requirements.txt

## Virtual environment
1. Activate virtual environment each time you use this code: source venv/bin/activate

## Set PYTHONPATH
export PYTHONPATH=$(pwd)

## Run the code at command line:
1. python3 driver.py <INPUT_CSV_FILE>

This code will process the input csv file, remove rows with missing values, and will output
data summary. Generated python code will be printed to the terminal.

## Run the code via a web interface:
1. python3 flask_app/flask_main.py

## Run tests
1. pytest

## Deactivate virtual environment
1. deactivate
