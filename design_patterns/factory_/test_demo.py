#!/usr/bin/env python3
#

from design_patterns.factory_.factorys import connect_to


def xml_parse():
    xml_factory = connect_to('person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall("./{}[{}='{}']".format('person', 'lastName', 'Liar'))
    # liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last  name: {}'.format(liar.find('lastName').text))
        [print('phone number: ({}) {}'.format(p.attrib['type'], p.text)) for p in liar.find('phoneNumbers')]


def json_parse():
    json_factory = connect_to('donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print(f"name: {donut['name']}")
        print(f"price: ${donut['ppu']}")
        [print(f"topings: \t{t['id']}\t{t['type']}") for t in donut['topping']]


if __name__ == '__main__':
    json_parse()
