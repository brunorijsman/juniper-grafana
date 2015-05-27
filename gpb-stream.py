# In this example we only monitor queue depth and latency for interfaces

from influxdb.influxdb08 import client
import analytics_pb2
import socket

INFLUX_DB_PORT = 8086
ANALYTICS_PORT = 9999
HEADER_SIZE = 8
VERSION = 1

def main():
    db = client.InfluxDBClient('localhost', INFLUX_DB_PORT, 'root', 'root', 'network')
    print 'Connected to InfluxDB'
    server(db)
    
def server(db):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', ANALYTICS_PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    print 'Accepted incoming TCP connection from', addr
    while receive_record(db, conn):
        pass
    conn.close()

def receive_record(db, conn):
    data = conn.recv(HEADER_SIZE)
    if not data:
        print 'Connection closed'
        return False
    length = ord(data[0]) + (ord(data[1]) << 8) + (ord(data[2]) << 16) + (ord(data[3]) << 24)
    version = ord(data[4])
    if version != VERSION:
        print 'Wrong version ', version
        return False
    data = conn.recv(length)
    if not data:
        print 'Connection closed'
        return False
    record = analytics_pb2.AnRecord()
    record.ParseFromString(data)
    process_record(db, record)
    return True
    
def process_record(db, record):
    if record.HasField('timestamp'):
        record_timestamp = record.timestamp
    else:
        record_timestamp = ''
    for interface in record.interface:
        process_interface(db, record_timestamp, interface)
            
def process_interface(db, record_timestamp, interface):
    if interface.HasField('stats'):
        process_interface_stats(db, record_timestamp, interface.name, interface.stats)

def process_interface_stats(db, record_timestamp, interface_name, interface_stats):
    if interface_stats.HasField('queue_stats'):
        process_queue_stats(db, record_timestamp, interface_name, interface_stats.queue_stats)

def process_queue_stats(db, record_timestamp, interface_name, queue_stats):
    columns = []
    points = []
    have_data = False
    if queue_stats.HasField('timestamp'):
        columns += ['timestamp']
        points += [queue_stats.timestamp]
    elif record_timestamp:
        columns += ['timestamp']
        points += [record_timestamp]
    if queue_stats.HasField('queue_depth'):
        columns += ['queue-depth']
        points += [queue_stats.queue_depth]
        have_data = True
    if queue_stats.HasField('latency'):
        columns += ['latency']
        points += [queue_stats.latency]
        have_data = True
    if have_data:
        # TODO: replace : with . in name
        point = {'name': interface_name, 'columns': columns, 'points': [points]}
        print point
        db.write_points([point])

main()
        
