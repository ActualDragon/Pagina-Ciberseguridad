FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install --upgrade pip
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app /app
COPY ./credentials.json /credentials/credentials.json
RUN pip install -r /var/www/requirements.txt
