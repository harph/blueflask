# -*- coding: utf-8 -*-
import os
import shutil

import click

import blueflask


@click.group()
def main(args=None):
    """
    BlueFlask command line.
    """


@main.command()
@click.argument('name', required=True)
@click.argument('directory', required=False, default='.')
def newapp(name, directory):
    """
    Args:
        name (str): App name.
        directory (str): Path of the directory where the project is going
            to be created. Defaults to the current directory.
    """
    # Check if the destination directory exists
    top_dir = os.path.abspath(directory)
    if not os.path.isdir(top_dir):
        raise ValueError("Destination directory '%s' does not exists, "
                         "please create it first." % top_dir)

    # Check if the app directory exist
    app_dir = os.path.join(top_dir, name)
    if os.path.isdir(app_dir):
        raise ValueError("'%s' already exist." % app_dir)

    bf_dir = blueflask.__path__[0]
    app_template_dir = os.path.join(bf_dir, 'templates', 'app_template')
    shutil.copytree(app_template_dir, app_dir)
    click.echo("Created a %s app in: %s" % (name, app_dir))


if __name__ == "__main__":
    main()
