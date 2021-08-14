#FROM python:3.8.9
#FROM python:3.8-alpine3.13
FROM public.ecr.aws/sam/build-python3.8:latest
LABEL maintainer="Walid Shaari"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

#USER 1001001
# command to run on container start
CMD [ "python", "app.py" ]
