import argparse
import logging, sys
import socket
from  dnsPacket import DNSPacket
from dnsPacketModifier import DNSPacketModifier

import pickle

DNS_UDP_PORT = 53
BUFFERSIZE = 1024

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-rServer', help='the DNS server to forward recursive queries to')
    parser.add_argument('-local-ip', help='IP addr of the host running this server')
    args = parser.parse_args()


    #Setup UDP socket that will  receice DNS request
    sock_DNS_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_DNS_in.bind((args.local_ip, DNS_UDP_PORT))

    #New instance of the Modifier
    modifier = DNSPacketModifier(args.rServer, DNS_UDP_PORT, BUFFERSIZE)
    #import pudb; pudb.set_trace()
    with open('packet_dump.obj', 'rb') as fi:
        dummy_pack = pickle.load(fi)
        print("Dummy packet loaded")
    while True:
        '''
        data, addr = sock_DNS_in.recvfrom(BUFFERSIZE) # buffer size is 1024 bytes
        logging.info('DNS Server State: %s', 'started and recieved first packet', extra={'bufferSize': BUFFERSIZE})
        dnsPacket = DNSPacket(data)
        print("----------------Packet Recieved------------\n " + str(dnsPacket))
        dnsPacketModified = modifier.modify(dnsPacket)
        print("----------------Packet Sent--------------\n " + str(dnsPacketModified))
        sock_DNS_in.sendto(dnsPacketModified.serializePacket(), addr)
        '''
        data, addr = sock_DNS_in.recvfrom(BUFFERSIZE) # buffer size is 1024 bytes
        logging.info('DNS Server State: %s', 'started and recieved first packet', extra={'bufferSize': BUFFERSIZE})
        dnsPacket = DNSPacket(data)
        sock_DNS_in.sendto(dummy_pack.serializePacket(), addr)

main()
