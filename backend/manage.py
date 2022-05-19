#! /usr/bin/env python

import signal
import subprocess

import click
import pytest


@click.group()
def cli():
    pass


@cli.command(context_settings={'ignore_unknown_options': True})
@click.argument('subcommand', nargs=-1, type=click.Path())
def flask(subcommand):
    cmdline = ['flask'] + list(subcommand)
    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


@cli.command()
@click.argument('filenames', nargs=-1)
def test(filenames):
    args = ['-svv', '--cov=app', '--cov-report=term-missing'] + list(filenames)
    return pytest.main(args)


if __name__ == '__main__':
    cli()
