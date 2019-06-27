FROM python

RUN pip install boto3 awscli

CMD ['python']