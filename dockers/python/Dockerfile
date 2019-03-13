FROM python:3.6-alpine as builder

# RUN apk update && \
#     apk add --no-cache \
#     linux-headers \
#     python-dev

RUN pip install --upgrade pip && \
    pip wheel -w /requirements/whl \
    Django==1.11 \
    django-extensions==2.0.7 \
    gunicorn


FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
COPY --from=builder /requirements/whl /requirements/whl
RUN pip install /requirements/whl/* && rm -rf /requirements

RUN set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

COPY --chown=www-data:www-data ./source /source

USER www-data

WORKDIR /source
