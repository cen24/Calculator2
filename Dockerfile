FROM python:3.7

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["/Database/create_model.py"]
CMD ["/Database/populate_model.py"]
CMD ["/Database/query_builder.py"]