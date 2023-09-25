#!/usr/bin/env python3

import os
import sys
import argparse
import json
import mfalcon.r2d2


def main(arguments):

    parser = argparse.ArgumentParser(
        description="A Python script to compute the odds of survival of the Millenium Falcon.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('falcon_config', help="'Millenium Falcon config file'", type=argparse.FileType('r'))
    parser.add_argument('empire_leaks', help="'Empire leaks file'", type=argparse.FileType('r'))
    parser.add_argument('-v', '--output_best_route', help="Give best routes", action='store_true')

    args = parser.parse_args(arguments)

    with open(args.falcon_config.name) as f_falcon:
        falcon_config = json.load(f_falcon)
    with open(args.empire_leaks.name) as f_empire:
        empire_leaks = json.load(f_empire)

    r2 = mfalcon.r2d2.R2D2(falcon_config,empire_leaks)
    if args.output_best_route:
        r2.print_routes()
    print(r2.give_odds())

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))