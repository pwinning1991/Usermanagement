import pytest

from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_fails_wothout_arguements(parser):
    """
    Without a path, the parser should exit with an error.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_succeeds_with_a_path(parser):
    """
    With a path, the parser should exit with an error
    """
    args = parser.parse_args(['/some/path'])
    assert arg.path == '/some/path'

def test_parser_export_flag(parser):
    """
    The `export` value should default to flase, but set
    to True when passed to the parser
    """
    args = parser.parse_args(['/some/path'])
    assert args.export == False

    args = parser.parse_args(['--export', '/some/path'])
    assert args.export == True



