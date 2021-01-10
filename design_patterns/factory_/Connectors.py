#!/usr/bin/env python3
#


import xml.etree.ElementTree as etree
import json


class Connector(object):
    def __init__(self):
        pass

    @property
    def parsed_data(self):
        return self


class JSONConnector(Connector):
    def __init__(self, filepath):
        super().__init__()
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(Connector):
    def __init__(self, filepath):
        super().__init__()
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
