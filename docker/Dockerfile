# Dockerfile

FROM python:3

WORKDIR /usr/src/app

COPY ./docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD [ "python", "./main.py" ]
