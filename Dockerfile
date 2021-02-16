FROM python:3.9.0
ENV PYTHONUNBUFFERED=1
WORKDIR /UKS
COPY . /UKS
RUN pip install -r requirements.txt
CMD ["python", "github/manage.py", "runserver"]