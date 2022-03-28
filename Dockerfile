FROM python:3.7 as final
WORKDIR /SERVER
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]