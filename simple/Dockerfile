FROM python:3
WORKDIR /usr/src/app/

RUN git clone https://github.com/duosecurity/duo_python.git

WORKDIR /usr/src/app/duo_python/demos/simple/
RUN pip install --requirement requirements.txt
RUN rm -R duo.conf

COPY *.conf ./
CMD [ "python", "-i", "./server.py" ]
