FROM golang:1.21 AS builder
WORKDIR /app
ENV CGO_ENABLED=0
ENV GOOS=linux
RUN go install -ldflags '-extldflags "-static"' github.com/rakyll/hey@latest

FROM debian:buster-slim
COPY --from=builder /go/bin/hey /usr/bin/hey
ENTRYPOINT ["hey"]
