FROM python:3.6

WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


ENTRYPOINT [ "python" ]
CMD ["app.py"]
