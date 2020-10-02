FROM confluentinc/cp-ksqldb-cli:5.5.1

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip

WORKDIR /polkadot-profit-transformer
COPY transformerTests transformerTests

WORKDIR /polkadot-profit-transformer/transformerTests
RUN pip3 install -r requirements.txt
RUN ls -al
ENV DISPLAY=:99
ENV KSQL_CONFIG_DIR=/etc/ksqldb


ENTRYPOINT [ "./entrypoint.sh" ]