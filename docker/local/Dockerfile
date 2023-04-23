FROM public.ecr.aws/lambda/python:3.9

ARG REQUIREMENTS_FILE='var/tmp/requirements.txt'

COPY requirements.txt ${REQUIREMENTS_FILE}
RUN pip install --upgrade pip && pip install -r ${REQUIREMENTS_FILE}

CMD ["lambda_function.lambda_hundler"]