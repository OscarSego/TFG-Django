build:
                docker build -f Dockerfile -t nebrija/api-django:latest .

run:
                docker run -p 8000:8000 nebrija/api-django:latest