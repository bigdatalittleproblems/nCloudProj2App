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
    redis = Redis(host="projectcache.dgmfid.0001.use1.cache.amazonaws.com", port=6379)
    @app.route('/')
    def hello():
        # redis.incr('hits')
        output="<!DOCTYPE html><html><body><h1>Christian Ramirez Test Page</h1><p>got to /test to check the output of redis </p></body></html>"
        return output
    @app.route('/test')
    def test():
        redis.incr('hits')
        output="<!DOCTYPE html><html><body><h1>Christian Ramirez Test Page</h1><h2>Redis Backend Test Page</h2><p>This page has been viewed {} times</p></body></html>".format(int(redis.get('hits')))
        return output
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port='5000')