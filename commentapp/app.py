from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')


# def run(host='0.0.0.0', port=80, debug=True):
#     app.run(host, port, debug)
