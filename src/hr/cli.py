import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path','-p',help='the path to the inventory file (JSON)')
    parser.add_argument('--export', action='store_true', help='export current setting to inventory file')
    return parser
