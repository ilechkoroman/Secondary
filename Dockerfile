FROM python:3.7

ENV FLASK_CONFIG production

RUN mkdir secondary
WORKDIR /home/secondary

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
RUN pip install uvicorn

COPY app app
COPY logs logs
COPY manage.py general_config.py logger_config.py logger_tools.py ./
