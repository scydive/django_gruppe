FROM python:3.11-rc-bullseye

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations mysite
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]