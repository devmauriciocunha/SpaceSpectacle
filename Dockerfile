FROM python:3.10.6
 
RUN apt-get update
 
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
 
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]