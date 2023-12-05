FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /api

COPY . .

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN python -m venv venv

ENV PATH="/api/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PORT=8000

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]