from flask import Flask
from flask import render_template


#initialize global variables
#create flask APP global variable and direct it to the templates/static folders
APP = Flask(__name__, template_folder='templates', static_folder='static')


#create main page based on the index.html file in templates
@APP.route('/')
def main():
    return render_template('index.html')


#turn on debugging to allow for `some` dynamic updates
if __name__ == '__main__':
    APP.run(debug=True)


#to start run
#export FLASK_APP=name_of_flask_file
#flask run