import warnings
import argparse

from src.nmpt import get_nmpt

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()

parser.add_argument('--x', type=float)
parser.add_argument('--y', type=float)
parser.add_argument('--lat', type=float)
parser.add_argument('--long', type=float)

args = parser.parse_args()
if args.x is not None and args.y is not None and args.lat is None and args.long is None:
    resp = get_nmpt(x=args.x, y=args.y)
    print(resp[1][0].__dict__['url'])
elif args.lat is not None and args.long is not None and args.x is None and args.y is None:
    resp = get_nmpt(lat=args.lat, long=args.long)
    print(resp)
    print(resp[1][0].__dict__['url'])
else:
    parser.error("You must provide either 'x' and 'y' or 'lat' and 'long' parameters.")
