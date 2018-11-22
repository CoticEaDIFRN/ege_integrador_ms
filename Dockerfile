FROM ifrn/ege_django_base:1.0

RUN pip install --upgrade pip

ADD startup.sh / 

WORKDIR /apps/app

COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

CMD /startup.sh

EXPOSE 8080