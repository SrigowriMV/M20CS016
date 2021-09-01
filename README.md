# Author Srigowri M V (M20CS016)

# PodcastApp

<u> About the app</u>

A flask web application to keep track of the Podcast episodes that I have want to listen or have already listened to.
The app uses MongoDB atlas to store the data

<u> Features</u>
- Add new podcast episode with host name, description, date and duration
- View all the podcasts that you have listened to or yet to listen to
- View the podcasts that you are done listening to
- View the podcasts that you have not listened to
- Update the status to Finished or yet to listen to
- Delete the podcast entry itself

## Building the flask application

- Create a workspace folder for the application
```bash
cd /path/to/podcast-app
pip3 install Flask, pymongo[srv], requests, pymongo
pip3 freeze > requirements.txt
```
- Write the application logic and place the required templates and static folder in the workspace folder
- Test the application by running

```bash
python3 -m flask run
```
## Dockerfile

A a text document named "Dockerfile" has instructions to assemble a Docker image. 
Docker reads and executes the instructions in Dockerfile when the build command is issued, it then creates a Docker image as a result.


The first line is a parser directive that specifies the Docker ensure compatability of syntax. I have used the python base image.
```bash
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```


## Building docker image from this repositary
- Clone the git repo 
- The Dockerfile has necessary commands to build the docker image
- Open command prompt from the folder and type
```bash
docker build . -t [tagname]
```
List the images, and notice a newly created image with the name "tagname"

```bash
docker images
```

## Running docker image

- Type the following to start the container
```bash
docker run tagname
```
List containers using the following command

```bash
docker ps -a
```


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

