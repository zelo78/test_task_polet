FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
#RUN apk update && \
#    apk add --no-cache \
#    python3-dev \
#    gcc \
#    musl-dev
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -Ur requirements.txt
COPY . /app