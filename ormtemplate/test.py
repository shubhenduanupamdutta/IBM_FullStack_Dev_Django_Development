# Django specific settings

# ruff: noqa: S101, T201
import inspect
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
from django.db import connection

application = get_wsgi_application()
# Your application specific imports
from standalone.models import Test  # noqa: E402


# Delete all data
def clean_data() -> None:
    """Delete all data from the Test model."""
    Test.objects.all().delete()


# Test Django Model Setup
def test_setup() -> None:
    """Tests the setup of ORM.

    Sets up and tests the Django model by cleaning existing data, creating a new Test instance,
    and verifying that the Test table is not empty. Prints the result of the setup process.

    Raises AssertionError if the setup fails, and handles unexpected errors gracefully.
    """
    try:
        clean_data()
        test = Test(name="Harry Potter", age=11)
        test.save()

        hermione = Test(name="Hermione Granger", age=12)
        hermione.save()

        # Check test table is not empty
        assert Test.objects.count() > 0
        print("Django Model setup completed.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise (exception)
    except Exception as exception:
        print("Unexpected error:", exception)


test_setup()
