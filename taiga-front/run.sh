#! /usr/bin/env sh

sed -i "s|API_BASE_URL|$API_PUBLIC_URL|g" /usr/src/app/taiga-front/conf.json
sed -i "s|API_BASE_URL|$API_INTERNAL_URL|g" /etc/nginx/conf.d/taiga.conf

nginx -g "daemon off;"