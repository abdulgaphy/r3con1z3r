FROM alpine:3.9
LABEL MAINTAINER furkan.sayim@yandex.com

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add git
RUN git clone https://github.com/abdulgaphy/r3con1z3r.git /tmp/r3con1z3r

WORKDIR /tmp/r3con1z3r
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "r3con1z3r.py"]
