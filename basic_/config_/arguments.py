import argparse
import textwrap

# <<< default values <<<
DEFAULT_CONFIG_FILE = '/netmon/config/config.yml'
DEFAULT_ENVIRONMENT = 'DEV'
DEFAULT_VERBOSE = False
DEFAULT_CONFIG_LOGGING = '/netmon/config/logging.yml'


class Arguments:

    def __init__(self) -> None:
        self._args = self._get_args()

    @staticmethod
    def _get_args():
        dash_79 = '-' * 79

        __description = f"""\
        {dash_79}
        # <<< sixie network flow monitor <<<        
        """

        __epilog = f"""\
        © Copyright www.sixiecapital.com
        # >>> sixie network flow monitor >>>      
        {dash_79}
        """

        parser = argparse.ArgumentParser(
            prog=__file__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(__description),
            epilog=textwrap.dedent(__epilog),
        )
        parser.add_argument('-f', '--config_file', nargs='?', type=str, help='full path of config file')
        parser.add_argument('-e', '--environment', nargs='?', type=str, help='enviroment: (DEV|PROD)')
        parser.add_argument('-v', '--verbose', nargs='?', help='verbose mode which can got more detailed output')

        return parser.parse_args()

    @property
    def config_file(self):
        if self._args.config_file:
            return self._args.config_file
        else:
            return DEFAULT_CONFIG_FILE

    @property
    def environment(self):
        if self._args.environment:
            return self._args.environment.upper()
        else:
            return DEFAULT_ENVIRONMENT.upper()

    @property
    def verbose(self):
        if self._args.verbose:
            return self._args.verbose
        else:
            return DEFAULT_VERBOSE
