# Run in Debian Jessie so we don't have to install unnecessary dependencies to our main image
FROM debian:jessie as builder

WORKDIR /build

RUN apt-get update \
 && apt-get install git -y

RUN git clone -b 3.4.5-stable \
              --single-branch \
              --depth 1 \
              https://github.com/taigaio/taiga-front-dist taiga-front

FROM nginx:stable-alpine

WORKDIR /usr/src/app/taiga-front

# Copy the app source
COPY --from=builder /build/taiga-front/dist .

# Copy the nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/*
COPY nginx/taiga.conf /etc/nginx/conf.d/taiga.conf
COPY taiga/conf.json .
COPY run.sh .

CMD ["./run.sh"]