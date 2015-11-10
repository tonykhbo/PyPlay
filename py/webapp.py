#!/usr/bin/env python
import bottle as bt

@bt.route('/', method = "GET")
def index():
    f = open('../index.html')
    return f.read()

bt.debug(True)

if __name__ == '__main__':    
    bt.run(host='104.131.246.240', port=80, debug=True)