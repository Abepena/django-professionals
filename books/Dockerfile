#Base image
FROM python:3.7-slim

#Set Environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

#Set working directory
WORKDIR /code

#Install Dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project into working dir
COPY . /code/