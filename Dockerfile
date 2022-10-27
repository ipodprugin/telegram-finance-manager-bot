FROM python:3.8

WORKDIR /home

ENV TELEGRAM_API_TOKEN="5560662656:AAF-aqZ1gDEFYx1opVBtRqByyKsLQIAHcDk"

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip aiogram
COPY src/ ./src/
COPY *.py ./

ENTRYPOINT ["python", "bot.py"]