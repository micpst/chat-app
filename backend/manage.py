#! /usr/bin/env python

import click
from flask.cli import FlaskGroup

cli = FlaskGroup()


@cli.command()
@click.argument('filenames', nargs=-1)
def test(filenames):
    import pytest
    args = ['-svv', '--cov=app', '--cov-report=term-missing'] + list(filenames)
    return pytest.main(args)


if __name__ == '__main__':
    cli()
