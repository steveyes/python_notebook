#!/usr/bin/env python3
#

# dict.get(key, default=None)

dict1 = {'name': 'zara', 'age': 27}

print('age: %s' % dict1.get('age'))

dict1.update({'gender': 'male'})
print('gender: %s' % dict1.get('gender'))
