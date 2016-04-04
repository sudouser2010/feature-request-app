#base image
FROM ubuntu:14.04

#maintainer
MAINTAINER Herbert Dawkins

#install pip
RUN apt-get update && apt-get -y upgrade\
    && apt-get install -y python python-pip

#export port 8100 of container to host
EXPOSE 8100

#copy everything in this directory into container
COPY . /opt/feature-request-app

#install project requirements
RUN pip install -r /opt/feature-request-app/requirements.txt

#specify entrypoint script
ENTRYPOINT ["/opt/feature-request-app/entrypoint.sh"]

#specify the directory entrypoint script will run in
WORKDIR /opt/feature-request-app/feature_request_app/

