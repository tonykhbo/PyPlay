#!/usr/bin/env python
import bottle as bt

@bt.route('/<filename>')
def index(filename):
    return bt.static_file(filename, root='/PyPlay/')

#run(host='104.131.246.240', port=8083, debug=True)
bt.debug(True)

if __name__ == '__main__':    
    bt.run()