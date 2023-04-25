FROM public.ecr.aws/lambda/python:3.9


# Layer code
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY ./layer/* ${LAMBDA_TASK_ROOT}
COPY day-app-report.py ${LAMBDA_TASK_ROOT}
