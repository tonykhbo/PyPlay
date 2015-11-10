#!/usr/bin/env python
import bottle as bt

@bt.route('~/PyPlay/<filename>', method = "GET")
def index(filename):
    f = open('../'+filename)
    return f.read()

#run(host='104.131.246.240', port=8083, debug=True)
bt.debug(True)

if __name__ == '__main__':    
    bt.run()