FROM public.ecr.aws/lambda/python:3.7

# Install the function's dependencies using file requirements.txt
# from your project folder.

# Layer code
WORKDIR /opt

COPY ./layers/test-utils/layer/* .
COPY ./layers/test-utils/requirements.txt .
RUN  pip3 install -r requirements.txt --target "/opt/extensions/lib"


# Copy lambda
WORKDIR ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}