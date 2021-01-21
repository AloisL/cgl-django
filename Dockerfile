# Pull the base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create server dir
RUN mkdir /mopga
WORKDIR /mopga

# Copy server files
COPY . /mopga

#Upgrade pip
RUN pip install pip -U

#Install dependencies
RUN pip install -r requirements.txt

RUN chmod +x /mopga/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "/mopga/entrypoint.sh"]