FROM python

RUN mkdir /data_service
COPY . /data_service

WORKDIR /data_service

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 50051

ENTRYPOINT [ "python", "server.py" ]
