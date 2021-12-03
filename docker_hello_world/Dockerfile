# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.6

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "flask run"]
