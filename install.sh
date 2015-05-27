#!/bin/bash

# Install Python
sudo apt-get install --yes python-pip
sudo apt-get install --yes python-dev

# Install InfluxDB
wget -O /tmp/influxdb_latest_amd64.deb https://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
sudo dpkg -i /tmp/influxdb_latest_amd64.deb
sudo pip install influxdb

# Install Grafana
wget -O /tmp/grafana_2.0.2_amd64.deb https://grafanarel.s3.amazonaws.com/builds/grafana_2.0.2_amd64.deb
sudo apt-get install -y adduser libfontconfig
sudo dpkg -i /tmp/grafana_2.0.2_amd64.deb

# Install PyEZ
sudo apt-get install --yes libxml2-dev
sudo apt-get install --yes libxslt1-dev
sudo pip install junos-eznc

# Install Google Protocol Buffers (GPB)
sudo apt-get install --yes python-protobuf

# Compile .proto file
protoc --python_out=. analytics.proto
