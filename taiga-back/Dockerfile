FROM python:3.6-stretch

ENV DEBIAN_FRONTEND noninteractive

COPY etc/locale.gen /etc/locale.gen
COPY etc/default.locale /etc/default/locale

RUN apt-get update \
 && apt-get autoremove -y \
 && apt-get install locales curl poppler-utils apt-transport-https git gettext -y
RUN locale-gen en_US.UTF-8 \
 && dpkg-reconfigure locales

WORKDIR /usr/src/app

RUN git clone -b 3.4.5 \
              --single-branch \
              --depth 1 \
              https://github.com/taigaio/taiga-back.git taiga-back

WORKDIR /usr/src/app/taiga-back

# Install requirements
RUN pip3 install -r requirements.txt \
 && pip3 install "gunicorn>=19.7.1"

# Bundle app source
COPY taiga/local.py settings/local.py
COPY run.sh .

ENV GUNICORN_TIMEOUT 30

CMD ["./run.sh"]
