# Run in a builder image so we don't have to install unnecessary dependencies to our main image
FROM python:3.6-stretch as builder

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get install git -y

# Build the front end
WORKDIR /build
RUN git clone -b 3.4.5-stable \
              --single-branch \
              --depth 1 \
              https://github.com/taigaio/taiga-front-dist taiga-front

# Build the back end (so we can serve up Django's static files)
WORKDIR /build
RUN git clone -b 3.4.5 \
              --single-branch \
              --depth 1 \
              https://github.com/taigaio/taiga-back taiga-back
WORKDIR /build/taiga-back

RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic --noinput


# Now build our main container
FROM nginx:stable-alpine

# Copy the app source
COPY --from=builder /build/taiga-front/dist /usr/src/app/taiga-front
COPY --from=builder /build/taiga-back/static /usr/src/app/taiga-back/static

# Copy the nginx config
WORKDIR /usr/src/app/taiga-front
COPY nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/*
COPY nginx/taiga.conf /etc/nginx/conf.d/taiga.conf
COPY taiga/conf.json .
COPY run.sh .

CMD ["./run.sh"]