#Pull base image
FROM python:3.7-slim

#Set ENV Variables
ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

#Set Working Dir
WORKDIR /code

#Install Dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy Project over to the working dir
COPY . /code/