#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv

def main():
    dotenv.read_dotenv()
    """Run administrative tasks."""
    env = os.getenv("ENV")
    if env == "local":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    elif env == "travis":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.travis')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
