import dataclasses
from pathlib import Path
from typing import List

import dataclasses_json
from dataclasses_json import DataClassJsonMixin
from yamldataclassconfig.config import YamlDataClassConfig

from basic_.config_.arguments import Arguments

DEFAULT_CONFIG_PATH = '/netmon/config/config.yml'


class ConfigUtil:

    @staticmethod
    def field_factory(_mm_field):
        return dataclasses.field(
            default=None,
            metadata=dataclasses_json.config(mm_field=_mm_field),
        )

    @classmethod
    def auto_locate(cls, _file_path=None):

        if _file_path:
            file_path = Path(_file_path)
        else:
            file_path = DEFAULT_CONFIG_PATH

        if not file_path.exists():
            return None

        return file_path


@dataclasses.dataclass
class Database(DataClassJsonMixin):
    host: str = None
    port: str = None
    user: str = None
    password: str = None
    database: str = None


@dataclasses.dataclass
class Nets(DataClassJsonMixin):
    without_payload: List[str] = None
    with_payload: List[str] = None


@dataclasses.dataclass
class Hosts(DataClassJsonMixin):
    without_payload: List[str] = None
    with_payload: List[str] = None


@dataclasses.dataclass
class Captures(DataClassJsonMixin):
    separator: str = None
    interface: str = None
    tcp_fields: List[str] = None
    udp_fields: List[str] = None


@dataclasses.dataclass
class Paths(DataClassJsonMixin):
    dir_root: str = None
    dir_config: str = None
    dir_log: str = None
    dir_tcp_payload: str = None
    dir_udp_payload: str = None
    dir_ddl: str = None
    dir_rotate_database: str = None
    dir_rotate_tcp: str = None
    dir_rotate_udp: str = None
    file_config_config: str = None
    file_config_logging: str = None


@dataclasses.dataclass
class Config(YamlDataClassConfig):
    database: Database = ConfigUtil.field_factory(Database)
    nets: Nets = ConfigUtil.field_factory(Nets)
    hosts: Hosts = ConfigUtil.field_factory(Hosts)
    captures: Captures = ConfigUtil.field_factory(Captures)
    paths: Paths = ConfigUtil.field_factory(Paths)


# netmon_args : argument variables loads from command line
arguments = Arguments()

# netmon_config : config variables loads from config file
configs = Config()
configs.load(ConfigUtil.auto_locate(Arguments().config_file))
