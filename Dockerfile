FROM python:3.11-rc-bullseye

ENV PYTHONBUFFERED 1

WORKDIR /app/mysite

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations mysite
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
