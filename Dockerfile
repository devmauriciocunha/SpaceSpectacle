FROM python:3.10.6
 
 
 
COPY . .
RUN pip install -r requirements.txt
 
RUN python manage.py makemigrations
RUN python manage.py migrate
 
# Criação do superusuário (substitua USERNAME, EMAIL e PASSWORD pelos valores desejados)
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@admin.com', 'admin')" | python manage.py shell
 
 
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
