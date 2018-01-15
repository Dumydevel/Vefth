from bottle import *
import os

@route('/')
def index():
    return "Virkar"

run(host='0.0.0.0', port=os.environ.get('PORT'))
#run(host='localhost', port=8080, debug=True)


