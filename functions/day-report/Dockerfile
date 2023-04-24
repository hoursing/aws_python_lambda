FROM public.ecr.aws/lambda/python:3.7

# Install the function's dependencies using file requirements.txt
# from your project folder.

# Layer code
WORKDIR ${LAMBDA_TASK_ROOT}

COPY ./../layer/ .
COPY ./../requirements.txt .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}