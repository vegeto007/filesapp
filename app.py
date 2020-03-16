from flask import Flask, render_template
from flask import request
import os
from tools import process_file


APP_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_REPO_PATH = os.path.join(APP_PATH, 'file_repo')
app = Flask(__name__)


@app.route('/show_file/')
def show_file():
    """Show file.

    This api shows contents of file.
    By default it shows file1.txt contents
    Following query parameters can be passed,
    file_name: File that needs to be read
    start: Start position of line
    end: End position of line

    e.g
    /show_file/?file_name=file1.txt&start=1&end=5
    """
    file_name = request.args.get('file_name', 'file1.txt')
    # start position set to 1 by default
    start_position = int(request.args.get('start', 1))
    # default maximum lines is set to 10000
    end_position = int(request.args.get('end', 10000))

    file_path = os.path.join(FILE_REPO_PATH, file_name)
    content = process_file(file_path, start_position, end_position)
    return render_template('display_file.html', content=content)


if __name__ == '__main__':
    app.run()
