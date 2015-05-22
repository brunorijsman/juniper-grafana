# What is this?

This is a set of python scripts that allows you to visualize telemetry from [Juniper Networks](http://juniper.net) devices.

Because we use [NETCONF](http://www.juniper.net/documentation/en_US/junos13.2/information-products/pathway-pages/netconf-guide/netconf.html) to gather telemetry from the device, this should work with any Juniper device including [SRX](http://juniper.net/srx) firewalls, [MX](http://juniper.net/mx), [PTX](http://www.juniper.net/us/en/products-services/routing/ptx-series/), and [ACX](http://www.juniper.net/us/en/products-services/security/srx-series/vsrx/) routers, [EX](http://juniper.net/ex), [QFX](http://www.juniper.net/us/en/products-services/switching/qfx-series/), and [OCX](http://www.juniper.net/us/en/products-services/switching/ocx1100/) switches, including virtual devices such as the [vSRX](http://www.juniper.net/us/en/products-services/security/srx-series/vsrx/) virtual firewall and the [vMX](http://www.juniper.net/us/en/products-services/routing/mx-series/vmx/) virtual router.  We only tested with vSRX.

Currently the following statistics are supported:

* Interfaces statistics: bytes sent, bytes received, packets sent, packets received for every interface.
 
It is implemented using:

* [PyEZ](http://techwiki.juniper.net/Automation_Scripting/010_Getting_Started_and_Reference/Junos_PyEZ) to implement the NETCONF interface to Juniper devices and gather operational state such as interface counters.
* [InfluxDB](http://influxdb.com/) as the time-series database.
* [Grafana](http://grafana.org/) for visualization.

All examples and scripts below are written for 64-bit Ubuntu 15.04.

# Installation

## Installation script

The install.sh script installs all external dependencies.  The following sections describe the manual installation steps if you don't want to use the script.

## Install InfluxDB

Install [InfluxDB](http://influxdb.com/) for storing the collected telemetry:
```
wget https://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
sudo dpkg -i influxdb_latest_amd64.deb
```

## Install vSRX

## Install Grafana:

Install [Grafana](http://grafana.org/) for visualization:
```
```

## Install PyEZ

Install [PyEZ](https://techwiki.juniper.net/Automation_Scripting/010_Getting_Started_and_Reference/Junos_PyEZ) ...


# Startup

The...

# Graphical User Interface (GUI)

## Script

The gui.sh script opens a firefox browser with tabs for the InfluxDB and Grafana.  The default user names and passwords are:

| Component | Default user name | Default password |
| --------- | ----------------- | ---------------- |
| InfluxDB  | root              | root             |
| Grafana   | admin             | admin            |

The following sections provide more detail for each interface.