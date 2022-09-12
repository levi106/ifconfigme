FROM amd64/python:3.9-slim-buster as builder

WORKDIR /src
COPY . .
RUN pip3 install setuptools wheel \
    && python3 setup.py bdist_wheel

FROM amd64/python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /src/dist/ifconfigme-*.whl ./
RUN pip3 install ifconfigme-*.whl

CMD [ "ifconfigme" ]