import argparse
import datetime
import textwrap


def get_epoch(nanos_since_epoch):
    seconds = int(nanos_since_epoch) / 10 ** 9
    nanos = str(int(nanos_since_epoch) % 10 ** 9).rjust(9, '0')
    dt = datetime.datetime.fromtimestamp(seconds)

    str_date = '-'.join([str(x).rjust(y, '0') for x, y in ((dt.year, 4), (dt.month, 2), (dt.day, 2))])
    str_time = ':'.join([str(x).rjust(y, '0') for x, y in {dt.hour: 2, dt.minute: 2, dt.second: 2}.items()])
    str_epoch = f"{str_date} {str_time}.{nanos}"
    return str_epoch


def main():
    desc_usage = textwrap.dedent("""
convert our timestamp format to human readable stuff    
""")

    parser = argparse.ArgumentParser()
    parser.add_argument('--usage', action='store_true', help='show help')
    parser.add_argument('nanos_since_epoch', help='epoch time in nanos')
    args = parser.parse_args()

    if args.usage:
        print(desc_usage)
        exit(0)

    print(get_epoch(args.nanos_since_epoch))


if __name__ == '__main__':
    main()
