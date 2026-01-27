FROM python:3.11-slim

WORKDIR /app

COPY app/ /app/
COPY tests/ /tests/

RUN pip install --no-cache-dir \
    beautifulsoup4 \
    requests \
    pytest

CMD ["python", "main.py"]