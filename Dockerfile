FROM python

RUN mkdir /data_service
COPY data_service/ /data_service

WORKDIR /data_service

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN python seed.py

EXPOSE 50051

ENTRYPOINT [ "python", "server.py" ]
