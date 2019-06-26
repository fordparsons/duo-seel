FROM python:3
WORKDIR /usr/src/app/

RUN git clone https://github.com/duosecurity/duo_client_python.git

WORKDIR /usr/src/app/duo_client_python/
RUN pip install --requirement requirements.txt

COPY *.py ./
CMD [ "python", "-i", "./api.py" ]
