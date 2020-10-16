# www.srini.tech simple template project with Docker, Gunicorn, Swagger (OpenApi), Flask and GoogleCloud Logging
www.srini.tech simple template project with Docker, Gunicorn, Swagger (OpenApi), Flask and GoogleCloud Logging
If you haven't yet configured (GCP) google cloud logging , it also prints to console


## Requirements

* Docker Compose 1.21.2+
* Python 3.6 +

## Run with Docker Compose

```bash
# building the container
sudo docker-compose build

# starting up a container
sudo docker-compose up
```

## Build the virtual environment

```bash
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test-requirements.txt
```

## Simple Get api Health Check

```http
http://localhost:8082/ping
```

## swagger UI

```http
http://localhost:8081/v1/basic/ui/
```

## Swagger definition

```http
http://localhost:8081/v1/basic/openapi.json
```

## To Integrate with Google Cloud Logging

Put your Google cloud credntials *.json file in <project root> folder
and specify path in /basic/config/__init__.py file

Ex.os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './xyz.json'

