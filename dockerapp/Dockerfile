FROM python:alpine

COPY requirements.txt .

EXPOSE 5000

RUN pip install -r requirements.txt

ENV redishost="projectcache.dgmfid.0001.use1.cache.amazonaws.com"

COPY main.py .

ENTRYPOINT ["python3" , "main.py"]
CMD ["python3" , "main.py"]