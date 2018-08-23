# Example model for the SWAG leaderboard powered by Beaker

# usage a base image that has python 3.6
FROM library/python:3.6

# set the working directory
WORKDIR /code

# install python packages
ADD ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# add more files from the git repo into the docker image
ADD configs/ .
ADD models/ .
ADD swagexample/ .
ADD Dockerfile .
ADD setup.py .
ADD readme.md .

# install the swagexample package inside the Docker image
RUN pip install .

# define the default command

# if you need to run a long-lived process, use `docker run --init`
CMD ["/bin/bash"]
