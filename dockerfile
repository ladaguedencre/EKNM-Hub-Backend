FROM python:3.9.10-alpine3.14
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=app
EXPOSE 5003
CMD ["python3", "main.py"]