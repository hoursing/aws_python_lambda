From cimg/python:3.9.16

ENV PROJECT_HOME /home/circleci/project

RUN pip install awscli aws-mfa --upgrade

COPY . ${PROJECT_HOME}


# install serverless
RUN sudo apt-get update && \
    sudo apt-get install -y curl nodejs npm && \
    sudo npm install n -g && \
    sudo n 14.21.1 && \
    sudo apt purge -y nodejs npm && \
    sudo npm i -g serverless@2.72.3 && \
    sudo chmod +x /usr/local/bin/sls

RUN sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
RUN sudo service docker start

# install node modules
RUN sudo npm install --prefix ${PROJECT_HOME}