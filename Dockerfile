FROM python:3.9-alpine
WORKDIR /app/
COPY ./requirements.txt ./requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r ./requirements.txt
RUN apk del .tmp
COPY ./app ./
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]