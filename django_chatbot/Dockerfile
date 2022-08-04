# importing base image
FROM python:3.9

# changing current working directory to /django_chatbot
WORKDIR /django_chatbot

# copying requirement.txt file to present working directory
COPY requirements.txt ./

# installing dependency in container
RUN pip install -r requirements.txt

# copying all the files to present working directory
COPY . .

# informing Docker that the container listens on the
# specified network ports at runtime i.e 8000.
EXPOSE 8000
#docker build -t django_chatbot:version-1 .# running server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]