FROM ifrn/ege_django_base:1.0

RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

# ADD startup.sh / 
# CMD /startup.sh

CMD python3 manage.py runserver 0.0.0.0:8080

EXPOSE 8080