import argparse

parser = argparse.ArgumentParser()
parser.version = '1.0'
parser.add_argument('-a', action='store', metavar='ALMAK_SZAMA')
parser.add_argument('-b', action='store_const', const=42)
parser.add_argument('-c', action='store_true')
parser.add_argument('-d', '--direkt-hamis', action='store_false')
parser.add_argument('-e', action='append')
parser.add_argument('-f', action='append_const', const=42)
parser.add_argument('-g', action='count', help="Mennyire nehéz az argparse használata")
parser.add_argument('-i', action='help')
parser.add_argument('-j', action='store', default="Jaj ne")
parser.add_argument('-v', action='version')
parser.add_argument('--input', action='store', type=int, nargs=3)
parser.add_argument('-x', action='count', required=True)
parser.add_argument('-p', choices=("alma", "körte", "barack"))

my_group = parser.add_mutually_exclusive_group()

my_group.add_argument('--verbose', action='store_true')
my_group.add_argument('--silent', action='store_true')

args = parser.parse_args()
print(args)
print(vars(args))