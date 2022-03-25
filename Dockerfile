FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT uvicorn main:app --host=0.0.0.0 --port=6666 --workers 1