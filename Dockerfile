FROM python:3.7

ADD . .

CMD ["python", "-m", "unittest", "discover", "-s","Tests"]