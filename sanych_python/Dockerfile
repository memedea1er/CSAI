FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py .
RUN pip install -r requirements.txt
EXPOSE 8088
CMD ["python", "main.py"]