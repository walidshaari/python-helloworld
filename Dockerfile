FROM public.ecr.aws/sam/build-python3.8:latest
LABEL maintainer="Walid Shaari"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080
# command to run on container start
CMD [ "python", "app.py" ]
