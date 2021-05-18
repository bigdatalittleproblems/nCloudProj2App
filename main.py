# compose_flask/app.py
from flask import Flask
from redis import Redis
import os
redishost = os.environ['redishost']
app = Flask(__name__)

testbool=False
if testbool:
    @app.route('/')
    def hello():
        # redis.incr('hits')
        return 'This Compose/Flask demo has been viewed {} time(s). Created by Christian Ramirez'.format(123)
    @app.route('/test')
    def test():
        # redis.incr('hits')
        return 'This is the path "/test" and it has been viewed {} time(s). Created by Christian Ramirez'.format(123)
else:
    redis = Redis(host=redishost, port=6379)
    @app.route('/')
    def hello():
        redis.incr('hits')
        return 'This Compose/Flask demo has been viewed {} time(s). Created by Christian Ramirez'.format(redis.get('hits'))

    @app.route('/test')
    def test():
        redis.incr('hits')
        return 'This is the path "/test" and it has been viewed {} time(s). Created by Christian Ramirez'.format(redis.get('hits'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port='5000')


# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/test")
# def test():
#     return "Hello test World!"

# if __name__ == "__main__":
#     app.run(host='0.0.0.0',port=6000)
    