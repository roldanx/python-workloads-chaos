FROM python:alpine
WORKDIR .
ADD main.py /opt
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "kubernetes"] 
ENTRYPOINT ["sh", "-c", "python /opt/main.py"]
