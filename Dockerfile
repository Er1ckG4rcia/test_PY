FROM python:3.9-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask

# Cria o diretório para o volume persistente
RUN mkdir -p /data

VOLUME /data

EXPOSE 8080

CMD ["python", "app.py"]
