FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

CMD pip freeze
CMD uvicorn --host=0.0.0.0 main:app