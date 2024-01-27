ARG NGINX_TAG=stable-alpine-slim
FROM python:3.12 AS python-base

FROM python-base as builder
RUN apt update && apt install libenchant-2-2 -y && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /rankade
COPY . .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir '.[docs]'
RUN ls -la
RUN make docs

# Final Image
ARG NGINX_TAG
FROM nginx:$NGINX_TAG
LABEL maintainer="Calum Crawford <c@calumcrawford.com>"
COPY --from=builder /rankade/build/docs /usr/share/nginx/html/rankadepy