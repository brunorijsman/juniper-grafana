#!/bin/bash

# Start InfluxDB
sudo /etc/init.d/influxdb start

# Start Grafana
sudo service grafana-server start
