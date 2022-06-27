FROM python:3.8-slim-buster

WORKDIR /Users/soorajbharadwaj/project-management-service/

COPY requirements.txt requirements.txt

RUN  pip3 install -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "app.main:app", "--reload"]