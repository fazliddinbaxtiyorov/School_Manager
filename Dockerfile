FROM ubuntu:latest
LABEL authors="acer"

ENTRYPOINT ["top", "-b"]