FROM public.ecr.aws/lambda/python:3.9


# Layer code
COPY . ${LAMBDA_TASK_ROOT}

COPY layer/* /opt
COPY layer/requirements.txt /opt/

RUN  pip3 install -r /opt/requirements.txt --target /opt/extensions/lib

RUN rm -rf layer