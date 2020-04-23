## Run

```
docker build -t serverless-python -f Dockerfile .

docker run -it -p 80:5000 serverless-python

docker run --env PORT=5000 -it -p  80:5000 serverless-python
```

## Push
#### via Docker

```
docker build -t serverless-python -f Dockerfile .

docker tag serverless-python gcr.io/cfe-project-t/serverless-python

docker push gcr.io/cfe-project-t/serverless-python
```

### via GCloud Build

```
gcloud builds submit --tag gcr.io/cfe-project-t/serverless-python .
```

## Deploy

```
gcloud run deploy serverless-python --image gcr.io/cfe-project-t/serverless-python --platform managed --region us-west1
```

```
gcloud builds submit --tag gcr.io/cfe-project-t/serverless-python .


gcloud run deploy serverless-python-v1 --image gcr.io/cfe-project-t/serverless-python:v1 --platform managed --region us-west1
```
