# Docker compose yaml is to instruct the build of multi docker containers, manage ports between them, like web-app1, web-app2, database
# Dockerfile is to instruct how to build the desired container, what should be in it, what should we run when its up 

# to download python (and OS) from docker hub
FROM python:3
# create work directory in docker machine
WORKDIR /usr/src/app
# copy python requirement from local to workDir above
COPY requirements.txt .
# run the command line
RUN pip install --no-cache-dir -r requirements.txt
# copy the rest of files to workDir
COPY . .
# run command line in container to run app.py
CMD [ "python", "app.py" ]