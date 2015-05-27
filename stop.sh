#!/bin/bash

# Stop Grafana
sudo service grafana-server stop

# Stop InfluxDB
sudo /etc/init.d/influxdb stop

