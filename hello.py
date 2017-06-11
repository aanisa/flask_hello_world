from flask import Flask
app = Flask(__name__)

# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

# If URL localhost:5000/hello/May will render Hello May
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run()

app.run(host='0.0.0.0', port=5000, debug=False)
