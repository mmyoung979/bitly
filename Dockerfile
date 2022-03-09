FROM python:3.7.6-slim-buster
WORKDIR /usr/src

COPY requirements.txt /usr/src
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
