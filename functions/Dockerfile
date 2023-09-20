FROM public.ecr.aws/lambda/python:3.9

ENV PYTHONPATH="$PYTHONPATH:${LAMBDA_TASK_ROOT}"

# Layer code
COPY . ${LAMBDA_TASK_ROOT}
