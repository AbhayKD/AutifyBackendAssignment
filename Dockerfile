# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .
RUN pip install pipenv

RUN pipenv install

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "pipenv", "run", "python", "./main.py", "https://www.google.com", "https://duckduckgo.com" ]