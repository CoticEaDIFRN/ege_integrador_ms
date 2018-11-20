FROM ifrn/ege_django_base:1.0

RUN pip install --upgrade pip

ADD startup.sh / 

WORKDIR /apps/app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD /startup.sh

EXPOSE 8080