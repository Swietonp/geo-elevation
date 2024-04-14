import warnings
import argparse

from src.nmpt import get_nmpt

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument('--x', type=float, required=True)
parser.add_argument('--y', type=float, required=True)
args = parser.parse_args()

resp = get_nmpt(x=args.x, y=args.y)
print(resp[1][0].__dict__['url'])
