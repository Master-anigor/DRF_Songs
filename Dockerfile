FROM python:3.10-buster

WORKDIR /usr/src/app
COPY requirements.txt ./
ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DB_ENGINE=django.db.backends.postgresql_psycopg2
ENV DB_NAME=drf
ENV DB_USER=drf_user
ENV DB_PASS=pgpwd4habr
ENV DB_SERVICE=postgres
ENV DB_PORT=5432


