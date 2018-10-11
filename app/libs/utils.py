#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

__all__ = ['echo']


def echo(message, fg=None, bg=None):
    color = dict(text=message)
    if fg:
        color['fg'] = fg
    if bg:
        color['bg'] = bg

    click.echo(click.style(**color))
