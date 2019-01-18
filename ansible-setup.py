#!/usr/bin/env python3

import os
import json
from argparse import ArgumentParser


def up():

    # @TODO if file exists in current directory execute down

    # @TODO pass net as parameter
    string = os.popen('docker network inspect docker_ansible').read()
    
    network = json.loads(string)
    
    containerIds = list(network[0]['Containers'].keys())
    
    for id in containerIds:
        
        containerIp = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + id).read()
        # @TODO add hosts directory to PWD
        os.system('echo ' + containerIp.rstrip() + ' >> ./hosts')

    # @TODO add some output
    
def down():
    os.system('rm hosts')

if __name__ == '__main__':

    options = {
        "up" : up,
        "down" : down,
    }
    
    parser = ArgumentParser()
    parser.add_argument(
        "mode",
        nargs='?',
        choices=['up', 'down'],
        help="1. up: Check network and setup hosts for ansible 2. down: Remove hosts file"
    )
    # @TODO define argument for parameter

    args = parser.parse_args()
    
    options[args.mode]()

        
