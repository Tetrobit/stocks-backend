FROM python:3.12-alpine

WORKDIR /app
COPY "requirements.txt" .
RUN ["pip3", "install", "-r", "requirements.txt"]

COPY . .
RUN ["python3", "manage.py", "migrate"]
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000