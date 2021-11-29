FROM python:3.6.9

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python /app/playground/manage.py runserver" ]