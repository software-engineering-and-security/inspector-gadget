FROM python:3.7.3-slim-stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
        g++ \
        libgomp1 \
    && pip3 install \
        pyvex==8.19.4.5 \
        dill==0.3.0 \
        capstone==4.0.1 \
        pyelftools==0.25 \
        pefile==2019.4.18 \
        z3-solver==4.8.5.0 \
    && apt-get -y remove g++ \
    && apt-get purge -y --autoremove \
    && rm -rf /var/lib/apt/lists/* /root/.cache

WORKDIR /app/
COPY inspectorgadget inspectorgadget
COPY ig.sh .

ENTRYPOINT ["/app/ig.sh", "-o", "/app/output"]
CMD ["-h"]