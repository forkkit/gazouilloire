#!/usr/bin/env python
import click
from gazouilloire.config_format import create_conf_example, load_conf
from gazouilloire import run


@click.group()
def main():
    pass


@main.command()
@click.argument('path', type=click.Path(exists=True), default=".")
def init(path):
    create_conf_example(path)


@main.command()
@click.argument('path', type=click.Path(exists=True), default=".")
def start(path):
    conf = load_conf(path)
    run.main(conf)


@main.command()
def resolve():
    click.echo("resolve")
    raise NotImplementedError
