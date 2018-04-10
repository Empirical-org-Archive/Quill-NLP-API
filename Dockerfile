FROM python:3.5.1-slim
MAINTAINER Donald McKendrick "donald@quill.org"

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN apt-get -y install nginx supervisor
RUN pip install --no-cache-dir gunicorn Flask
ENV LT_URI=http://langaugetool-env.pvmbrmtthd.us-east-1.elasticbeanstalk.com
ENV QUILL_SPACY_MODEL=en_core_web_lg

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install spacy==2.0.10
RUN python -m spacy download en_core_web_lg
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP=app.py 
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]
