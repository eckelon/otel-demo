# Otel demo

This is just a super quick demo to see traces from Nginx and a Flask app in Jaeger.

build it with

```
docker-compose build
```
and run it with

```
docker-compose up -d  
```

Please mind that I wrote this in an Apple Silicon machine, so you might need to change the way you compile some of the libs in the Nginx Dockerfile. 
