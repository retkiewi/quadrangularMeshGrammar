import argparse
import sys
from examples import p2, p12

def main(args):
    # p2.show()
    p12.show()

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))
