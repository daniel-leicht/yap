FROM golang:1.12-buster

RUN apt update && apt install -y bzip2

RUN mkdir -p /yap/src
COPY . /yap/src/yap

ENV GOPATH=/yap
WORKDIR /yap/src/yap

RUN bunzip2 data/*.bz2

ENV GIT_SSL_NO_VERIFY=1
RUN go get .
RUN go build .

EXPOSE 8000

ENTRYPOINT ["/yap/src/yap/yap", "api"]

