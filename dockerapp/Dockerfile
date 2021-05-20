FROM python:alpine

COPY requirements.txt .

EXPOSE 5000

ENV redishost="projectcache.dgmfid.0001.use1.cache.amazonaws.com"
RUN pip install -r requirements.txt

COPY main.py .
COPY requirements.txt .

ENTRYPOINT ["python3" , "main.py"]