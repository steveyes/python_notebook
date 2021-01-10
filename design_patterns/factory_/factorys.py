#!/usr/bin/env python3
#

from design_patterns.factory_.Connectors import JSONConnector, XMLConnector


def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connector_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory
