device_ip = "192.168.229.185"
user_name = "test"
password = "test!!"

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from time import sleep
from influxdb.influxdb08 import client
 
device = Device(host=device_ip, port=22, user=user_name, passwd=password)
device.open()
switch_name = device.facts['fqdn']
print 'Connected to', switch_name, '(', device.facts['model'], 'running', device.facts['version'], ')'
ports_table = EthPortTable(device)
 
db = client.InfluxDBClient('localhost', 8086, 'root', 'root', 'network')
print 'Connected to InfluxDB'
 
print 'Collecting metrics...'
columns = ['rx_packets', 'rx_bytes', 'tx_packets', 'tx_bytes']
while True:
  ports = ports_table.get()
  for port in ports:
    point = {'name': switch_name + '.' + port['name'],
             'columns': columns,
             'points': [[int(port['rx_packets']), int(port['rx_bytes']), int(port['tx_packets']), int(port['tx_bytes'])]]}
    db.write_points([point])
  sleep(1) 
