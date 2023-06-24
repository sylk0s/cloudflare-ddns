FROM python:3.11.4-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

#ENV TOKEN
#ENV ZONE
ENV FREQ=1
ENV TYPE=A
#ENV DOMAIN

CMD ["python", "./src/main.py"]