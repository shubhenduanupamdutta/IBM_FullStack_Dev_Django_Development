"""Reading courses."""

# ruff: noqa: E402, T201

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from crud.models import Course

# Your code starts from here:
# Find all courses
courses = Course.objects.all()
print(courses)

