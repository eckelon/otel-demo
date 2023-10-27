FROM ubuntu:22.04 AS build

ENV NGINX_VERSION=1.21.1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libpcre3-dev \
    pkg-config \
    libc-ares-dev \
    libc-ares2 \
    libre2-dev \
    libre2-9 \
    git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src
RUN git clone https://github.com/nginx/nginx.git

WORKDIR /src/nginx
RUN ./auto/configure --with-compat

WORKDIR /src
RUN git clone https://github.com/nginxinc/nginx-otel.git

WORKDIR /src/nginx-otel/build
RUN cmake -DNGX_OTEL_NGINX_BUILD_DIR=/src/nginx/objs .. \
    && make

WORKDIR /src/nginx
RUN make && make install

FROM ubuntu:22.04

COPY --from=build /usr/local/nginx /usr/local/nginx
COPY --from=build /src/nginx-otel/build/ngx_otel_module.so /usr/local/nginx/modules/
COPY --from=build /usr/lib/aarch64-linux-gnu/libcares.so.2.5.1 /usr/lib/aarch64-linux-gnu/libcares.so.2.5.1
COPY --from=build /usr/lib/aarch64-linux-gnu/libre2.so.9 /usr/lib/aarch64-linux-gnu/

RUN ln -s /usr/lib/aarch64-linux-gnu/libcares.so.2.5.1 /usr/lib/aarch64-linux-gnu/libcares.so.2

COPY nginx.conf /usr/local/nginx/conf/nginx.conf


EXPOSE 80

CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
