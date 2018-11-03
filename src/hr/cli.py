import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parsr.add_agrument('--path','-p',help='the path to the inventory file (JSON)')
    parser.add_agrument('--export', action='store_true', help='export current setting to inventory file')
    return parser
