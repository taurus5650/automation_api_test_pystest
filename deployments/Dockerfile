FROM python:3.11-slim
COPY . /autmation_api_test_pytest
WORKDIR /autmation_api_test_pytest
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null