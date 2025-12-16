FROM python:3.8-slim

WORKDIR /app

# Install curl for the healthcheck
RUN apt-get update && apt-get install -y curl

COPY . /app

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]
