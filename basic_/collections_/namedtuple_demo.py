#!/usr/bin/env python3
#
import warnings
from collections import namedtuple
from dataclasses import dataclass
import json

"""warning: namedtuple is obsolete, please use dataclasses.dataclass instead"""


def cprint(args=None):
    print("-" * 79)
    print(args if args else '')
    print()


def _GetValue(_name, _type):
    def _get(kv_form: dict, ):
        return kv_form.get(_name, _type())

    return _get


def _fields_insert(_fields, _deny_insert, ):
    def _get(_kv: dict, ):
        __k_list = []
        for k, v in _kv.items():
            # 去空
            if not v:
                continue

            # 脱敏
            if k in _deny_insert:
                continue

            # 字段拼接
            if k in _fields:
                __k_list.append(k)
            else:
                continue

        return tuple(__k_list)

    return _get


# Using namedtuple is way shorter than defining a class manually:

_Field = namedtuple('_Field', ('name', 'v_type', 'get_value',))

_Table = namedtuple('_Table', (
    'TabName', 'PKName', 'MediaType', 'MediaOwner',
    'FieldsInsert',
    # 'GetV4Insert', 'GetK4Select', 'GetV4Select', 'CVT4Select', 'CVT4Update',
))

_FieldsVisitVillage = namedtuple('_FieldsVisitVillage', (
    'Fields', 'DenyInsert', 'DenySelect', 'DenyUpdate',
    'id', 'village_id', 'count_pv', 'count_uv', 'gmt_create', 'gmt_modified', 'amount',))

vv = _FieldsVisitVillage(
    Fields=('id', 'village_id', 'count_pv', 'count_pv', 'count_uv', 'gmt_create', 'gmt_modified', 'amount',),
    DenyInsert=(),
    DenySelect=('gmt_modified',),
    DenyUpdate=('gmt_modified',),
    id=_Field(name='id', v_type=int, get_value=_GetValue('id', int), ),
    village_id=_Field(name='village_id', v_type=int, get_value=_GetValue('village_id', int), ),
    count_pv=_Field(name='count_pv', v_type=int, get_value=_GetValue('count_pv', int), ),
    count_uv=_Field(name='count_uv', v_type=int, get_value=_GetValue('count_uv', int), ),
    gmt_create=_Field(name='gmt_create', v_type=str, get_value=_GetValue('gmt_create', str), ),
    gmt_modified=_Field(name='gmt_modified', v_type=str, get_value=_GetValue('gmt_modified', str), ),
    amount=_Field(name='amount', v_type=float, get_value=_GetValue('amount', float), ),
)

_village = {
    'TabName': 't_village', 'PKName': 'id', 'MediaType': 'image', 'MediaOwner': 'village',
    'Fields': ('id', 'village_id', 'count_pv', 'count_pv', 'count_uv', 'gmt_create', 'gmt_modified', 'amount',),
    'DenyInsert': (),
    'DenySelect': ('gmt_modified',),
    'DenyUpdate': ('gmt_modified',),
    'id': {'name': 'id', 'type': int, },
    'village_id': {'name': 'village_id', 'type': int, },
    'count_pv': {'name': 'count_pv', 'type': int, },
    'count_uv': {'name': 'count_uv', 'type': int, },
    'gmt_create': {'name': 'gmt_create', 'type': int, },
    'gmt_modified': {'name': 'gmt_create', 'type': int, },
    'amount': {'name': 'amount', 'type': int, },

}

village = _Table(
    TabName='t_village', PKName='id', MediaType='image', MediaOwner='village',
    FieldsInsert=_fields_insert(_village['Fields'], _village['DenyInsert']),
)

# table name
cprint(f'table name: {village.TabName}')

# pk name
cprint(f'pk name: {village.PKName}')

# media type
cprint(f'media type: {village.MediaType}')

# media owner
cprint(f'media owner: {village.MediaOwner}')

# get kv forms
kv_forms = {
    'id': 10086,
    'village_id': 10,
    'count_pv': '100',
    'count_uv': '200',
    'gmt_create': '2018-12-31 10:00:00',
    'gmt_modified': '2019-01-01 10:00:00',
    'amount': '123456.021',
}

#
cprint(f'fieldsinsert: {village.FieldsInsert(kv_forms)}')

dd = {
}

cprint(json.dumps(dd, indent=4, sort_keys=False))
