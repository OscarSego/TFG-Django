FROM python:3.12.0

WORKDIR /app

# Instalar Vim
RUN apt-get update && apt-get install -y vim

COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
