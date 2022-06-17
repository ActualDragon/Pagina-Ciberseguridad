FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install --upgrade pip
RUN mkdir Credentials
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app /app
RUN pip install -r /var/www/requirements.txt
