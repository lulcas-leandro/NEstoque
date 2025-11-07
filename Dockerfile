FROM python:3.11-slim

LABEL maintainer='lucasleandro.cdev@gmail.com'
LABEL description='NEstoque- Sistema simples de estoque'

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "run:app"]