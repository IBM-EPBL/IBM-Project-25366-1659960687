FROM python:3.8.10
WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python3", "./app.py"]