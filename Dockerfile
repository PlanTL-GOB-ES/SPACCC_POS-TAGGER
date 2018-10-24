FROM ubuntu:12.04

RUN locale-gen en_US.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libboost-all-dev wget && \
    apt-get clean && \
    wget -O /tmp/freeling-3.1.tar.gz http://devel.cpl.upc.edu/freeling/downloads/32 && \
    cd /tmp && \
    tar -zxf freeling-3.1.tar.gz && \
    cd /tmp/freeling-3.1 && \
    ./configure && \
    make && \
    make install && \
    rm -rf /tmp/freeling-3.1.tar.gz /tmp/freeling-3.1

ENV FREELINGSHARE /usr/local/share/freeling

COPY . /config

ENTRYPOINT [ "analyze", "--flush", "-f /config/config.cfg", "--ftok /config/tokenizer.dat", "--fsplit /config/splitter.dat", "--floc /config/singlewords.dat", "--usr --fmap /config/usermap.dat", "--noquant" ]

