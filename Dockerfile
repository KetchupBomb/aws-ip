FROM python:3-slim

WORKDIR /app/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY __init__.py aws.py ./

ENTRYPOINT ["python", "aws.py"]
