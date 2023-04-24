FROM public.ecr.aws/lambda/python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.

# Layer code
WORKDIR ${LAMBDA_TASK_ROOT}

# COPY ./../layer/ .
# COPY ./../requirements.txt .

COPY . ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"