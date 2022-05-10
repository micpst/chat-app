import os
import signal
import subprocess

import click
import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


os.environ['APPLICATION_CONFIG'] = 'development'


def get_env_file(config):
    return os.path.join('env', f'.env.{config}')


def get_docker_compose_file(config):
    return os.path.join('docker', f'{config}.yml')


def load_env_file(config):
    load_dotenv(get_env_file(config))


def get_docker_compose_cmdline():
    config = os.getenv('APPLICATION_CONFIG')
    compose_file = get_docker_compose_file(config)
    env_file = get_env_file(config)

    load_env_file(config)

    return [
        'docker', 'compose',
        '-p', config,
        '-f', compose_file,
        '--env-file', env_file
    ]


def run_sql(statements):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOSTNAME'),
        port=os.getenv('POSTGRES_PORT')
    )

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    for statement in statements:
        cursor.execute(statement)

    cursor.close()
    conn.close()


@click.group()
def cli():
    pass


@cli.command(context_settings={'ignore_unknown_options': True})
@click.argument('subcommand', nargs=-1, type=click.Path())
def flask(subcommand):
    load_env_file(os.getenv('APPLICATION_CONFIG'))
    cmdline = ['flask'] + list(subcommand)
    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


@cli.command(context_settings={'ignore_unknown_options': True})
@click.argument('subcommand', nargs=-1, type=click.Path())
def compose(subcommand):
    cmdline = get_docker_compose_cmdline() + list(subcommand)
    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


@cli.command()
def create_initial_db():
    load_env_file(os.getenv('APPLICATION_CONFIG'))
    database = os.getenv('APPLICATION_DB')
    try:
        run_sql([f'CREATE DATABASE {database}'])
    except psycopg2.errors.DuplicateDatabase:
        print(f'The database {database} already exists and will not be recreated')


@cli.command()
@click.argument('filenames', nargs=-1)
def test(filenames):
    os.environ['APPLICATION_CONFIG'] = 'testing'
    load_env_file(os.getenv('APPLICATION_CONFIG'))

    cmdline = get_docker_compose_cmdline() + ['up', '-d']
    subprocess.call(cmdline)

    while True:
        try:
            run_sql([f"CREATE DATABASE {os.getenv('APPLICATION_DB')}"])
            break
        except psycopg2.OperationalError:
            pass

    cmdline = ['pytest', '-svv', '--cov=app', '--cov-report=term-missing'] + list(filenames)
    subprocess.call(cmdline)

    cmdline = get_docker_compose_cmdline() + ['down']
    subprocess.call(cmdline)


if __name__ == '__main__':
    cli()
