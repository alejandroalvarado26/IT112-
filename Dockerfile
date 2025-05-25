FROM python
WORKDIR /myflaskapp/
ADD . /myflaskapp/
RUN apt-get update && apt-get install -y ca-certificates
RUN pip install -r requirements.txt
CMD ["python","app.py"]