# Machine Learning Code Generator
This is an experimental software providing a point and click user interface for generating python code for machine learning (ML) pipelines.
At this early stage, the features are very limited. We are actively working on building new features to get the first proof of concept
version working. The goal of this software is to allow non-programmers "write" ML pipeline code.

## Install dependencies (only one time)
The instructions below assume that python3 and pip3 refer to Python 3.x and Pip 3.x. Depending on how things are configured, you may need to use python and pip commands instead of python3 and pip3. Additionally, Windows users would benefit from installing gitbash for windows, which will allow them to run bash commands (as used in these instructions).

1. Create a virtual environment: python3 -m venv venv
2. Activate virtual environment: 
   * Mac or Linux: source venv/bin/activate
   * Windows: source venv/Scripts/activate
3. Install dependencies: pip3 install -r requirements.txt

## Virtual environment
1. Activate virtual environment each time you use this code: 
   * Mac or Linux: source venv/bin/activate
   * Windows: source venv/Scripts/activate

## Set PYTHONPATH
export PYTHONPATH=$(pwd)

## Run the code at command line:
1. python3 main.py <INPUT_CSV_FILE>

This code will process the input csv file, remove rows with missing values, and will output
data summary. Generated python code will be printed to the terminal.

## Run the code via a web interface:
1. python3 flask_app/flask_main.py

If all goes well, you should see the following in your terminal:
<pre><code>
 * Serving Flask app 'flask_main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
</code></pre>
Point your web browser to http://127.0.0.1:5000 to access the user interface of this software.
## Run tests
1. pytest

## Deactivate virtual environment
1. deactivate

## Environment Variables
This application contains a "Login with Google" feature. In order for this feature to properly work, there needs to be a <code>flask_app/api/.env</code> file defining two variables: GOOGLE_CLIENT_SECRET and GOOGLE_CLIENT_ID. These variables come from Google Cloud credentials configuration (google developer console). This file is intentionally part of the code repository, because those values must be kept secret.
