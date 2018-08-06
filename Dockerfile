# Example model for the SWAG leaderboard powered by beaker

FROM library/python:3.6


# set the working directory

WORKDIR /code


# install python packages

ADD ./requirements.txt .

RUN pip3.6 install --upgrade pip \
 && pip3.6 install -r requirements.txt


# add files in addition to requirements.txt

ADD configs/ .
ADD models/ .
ADD swagexample/ .
ADD Dockerfile .
ADD setup.py .
ADD readme.md .

# pip install the swagexample package

RUN pip3.6 install .


# define the default command

# if you need to run a long-lived process, use `docker run --init`
CMD ["/bin/bash"]
