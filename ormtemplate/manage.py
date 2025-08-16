import os  # noqa: D100, INP001
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # noqa: F401
        except ImportError as e:
            msg = (
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
            raise ImportError(msg) from e
        raise
    execute_from_command_line(sys.argv)
