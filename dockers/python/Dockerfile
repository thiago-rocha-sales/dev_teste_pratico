FROM python:3.6-alpine as builder

RUN apk update && \
    apk add --no-cache \
    postgresql-dev \
    gcc \ 
    python3-dev \ 
    musl-dev

RUN pip install --upgrade pip && \
    pip wheel -w /requirements/whl \
    Django==1.11 \
    djangorestframework \
    django-extensions==2.0.7 \
    psycopg2-binary \
    gunicorn \
    whitenoise


FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache \
    libpq

COPY --from=builder /requirements/whl /requirements/whl
RUN pip install /requirements/whl/* && rm -rf /requirements

# RUN set -x ; \
#     addgroup -g 82 -S www-data ; \
#     adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

RUN set -x ; \
    addgroup -g 1000 -S nginx ; \
    adduser -u 1000 -D -S -G nginx nginx ; exit 0

COPY --chown=nginx:nginx ./source /source

USER nginx

WORKDIR /source