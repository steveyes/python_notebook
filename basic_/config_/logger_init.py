import logging
import logging.config
from pathlib import Path

import yaml

from basic_.config_.arguments import DEFAULT_CONFIG_LOGGING
from basic_.config_.arguments import Arguments


def setup_logger(_file_path=None):
    if _file_path:
        file_path = Path(_file_path)
    else:
        file_path = Path(DEFAULT_CONFIG_LOGGING).resolve()

    if not file_path.exists():
        raise Exception(f'failed to locate file: {file_path}.')

    with open(file_path, 'r') as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception as e:
            print(e)
            raise Exception(f'Error in setup config: {file_path}.')


setup_logger()


def get_logger(is_verbose=Arguments().verbose, format_name=None, file_name=None):
    if is_verbose:
        return logging.getLogger('verbose')
    elif format_name:
        return logging.getLogger(format_name)
    elif file_name:
        return logging.getLogger(Path(file_name).stem)
    else:
        raise Exception('warning: logger setting error!')


class Logger:
    standard = get_logger(format_name='standard')
    detailed = get_logger(format_name='detailed')
