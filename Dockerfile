FROM python:3.9.0
ENV PYTHONUNBUFFERED=1
WORKDIR /UKS
COPY . /UKS

ADD start.sh /
RUN pip install -r requirements.txt

RUN chmod +x /start.sh
CMD ["/start.sh"]
