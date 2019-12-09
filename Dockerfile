FROM python:3.7

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["/Database/sqlite_data.py"]
CMD ["/Database/sqlite_model.py"]
CMD ["/Database/sqlite_query.py"]