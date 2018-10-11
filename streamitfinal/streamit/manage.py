#!/usr/bin/env python
import os
import sys

<<<<<<< HEAD
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'streamit.settings')
=======
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 8935810849324b57984e87c60775a2e2df527e69
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
