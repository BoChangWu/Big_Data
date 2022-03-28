FROM python:3.7 as final
ENV PYTHONUNBUFFERED 1
WORKDIR /SERVER
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update -y \
    && apt-get install -y vim \
    && rm -rf /var/lib/apt/lists/* /tmp/*

COPY . .
EXPOSE 8000
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]