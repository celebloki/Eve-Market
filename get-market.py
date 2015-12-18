#!/usr/bin/env python

import zlib, zmq, simplejson

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    
    subscriber.connect('tcp://relay-us-west-1.eve-emdr.com:8050')
    
    subscriber.setsockopt(zmq.SUBSCRIBE, "")
    
    while True:
        market_json = zlib.decompress(subscriber.recv())
        
        market_data = simplejson.loads(market_json)
        
        print market_data
        
if __name__ == '__main__':
    main()
