FROM python:3.9.0
ENV PYTHONUNBUFFERED=1
WORKDIR /UKS
COPY . /UKS
RUN pip install -r requirements.txt
CMD ["python", "github/manage.py", "migrate"]
CMD ["python", "github/manage.py", "runserver","0.0.0.0:8081"]