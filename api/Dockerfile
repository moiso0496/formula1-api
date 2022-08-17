FROM python:3
WORKDIR /usr/scr/app
COPY requirements.txt .
RUN pip install  --no-cache-dir -r requirements.txt
COPY . ./api 
ENV PYTHONPATH "/usr/scr/app"
CMD ["python", "api/app.py"]