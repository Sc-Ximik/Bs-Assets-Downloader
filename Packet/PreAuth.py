# -*- coding: utf-8 -*-
import os
import sys
import json
import ctypes

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
        major = config['major']
        minor = config['minor']
        print(major)
        print(minor)


from Packet.Writer import Writer


class PreAuth(Writer):

    def __init__(self):
        self.Id = 10100

    def process(self):
        self.putInt(0)
        self.putInt(0)
        self.putInt(int(major))
        self.putInt(0)
        self.putInt(int(minor))
        self.putString('')
        self.putInt(2)
        self.putInt(2)
