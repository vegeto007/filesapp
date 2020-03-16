Flask app to read file and display contents.

This app is tested with python 3.7 in windows

Go to project directory and run following commands
* *install dependencies*\
pip install -r requirements.txt
* *set flask environment variable to development to get debug messages*\
set FLASK_ENV=development
* *run app*\
python app.py

Usage:

http://127.0.0.1:5000/show_file/?file_name=file1.txt&start=1&end=5
