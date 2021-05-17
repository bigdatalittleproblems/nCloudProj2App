FROM python:alpine

COPY requirements.txt .

EXPOSE 5000

ENV redishost="projectcache.dgmfid.0001.use1.cache.amazonaws.com"
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3" , "main.py"]

# CMD ['python3','flask.py']