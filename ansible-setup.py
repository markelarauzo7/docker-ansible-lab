#!/usr/bin/env python3

import os
import json
from argparse import ArgumentParser


def check(network):

    exists = os.path.isfile('hosts')
    
    if exists:
        clean()

    print("Checking " + network + " docker network...")

    string = os.popen('docker network inspect ' + network).read()
    
    network = json.loads(string)
    
    containerIds = list(network[0]['Containers'].keys())
    
    for id in containerIds:
        
        containerIp = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + id).read()
        print("Creating a inventory in current working directory...")
        os.system('echo ' + containerIp.rstrip() + ' >> $PWD/inventory')

    print("Created hosts file.")
    
def clean():
    os.system('rm inventory')

if __name__ == '__main__':

    options = {
        "check" : check,
    }
    
    parser = ArgumentParser()
    parser.add_argument(
        "mode",
        nargs='?',
        choices=['check'],
        help="Check network and setup hosts for ansible"
    )
    parser.add_argument(
        "network",
        nargs='?',
        help="Docker network name to be checked"
    )

    args = parser.parse_args()
    
    options[args.mode](args.network)

        
