#!/bin/sh
# YF Server install script

apt-get install -y python-pil python-twisted-core python-mysqldb

DEST_DIR=bin
REDIS_VER=2.6.16


mkdir -p $DEST_DIR/redis/rdb
mkdir -p $DEST_DIR/redis/bin
wget --no-check-certificate http://download.redis.io/releases/redis-$REDIS_VER.tar.gz
tar zxf redis-$REDIS_VER.tar.gz
cd redis-$REDIS_VER
make
cd ..
cp redis-$REDIS_VER/src/redis-server $DEST_DIR/redis/bin
cp redis-$REDIS_VER/src/redis-cli $DEST_DIR/redis/bin
cp redis-$REDIS_VER/src/redis-sentinel $DEST_DIR/redis/bin
cp redis-$REDIS_VER/src/redis-benchmark $DEST_DIR/redis/bin
cp redis-$REDIS_VER/src/redis-check-aof $DEST_DIR/redis/bin
cp redis-$REDIS_VER/src/redis-check-dump $DEST_DIR/redis/bin
cp redis-$REDIS_VER/redis.conf $DEST_DIR/redis/bin/conf