"""Testing CRUD Operations on the database tables."""
# ruff: noqa: E402, T201

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from datetime import date

from crud.models import Course, Enrollment, Instructor, Learner, Lesson, User


# Your code starts from here:
def write_instructors() -> None:
    """Create and save several Instructor objects with associated user data.

    This function performs the following actions:
    - Creates a User instance for John Doe and saves it.
    - Creates an Instructor instance for John, associates it with the created User, and saves it.
    - Creates and saves Instructor instances for Yan Luo, Joy Li, and Peter Chen with their
    respective attributes.
    - Prints a confirmation message after all Instructor objects are saved.

    Note:
        Assumes that the User and Instructor models are already imported and that the Instructor
        model can accept user, first_name, last_name, dob, full_time, and total_learners as
        attributes.

    """
    # Add instructors
    # Create a user
    user_john = User(first_name="John", last_name="Doe", dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john  # pyright: ignore[reportAttributeAccessIssue]
    instructor_john.save()

    instructor_yan = Instructor(
        first_name="Yan",
        last_name="Luo",
        dob=date(1962, 7, 16),
        full_time=True,
        total_learners=30050,
    )
    instructor_yan.save()

    instructor_joy = Instructor(
        first_name="Joy",
        last_name="Li",
        dob=date(1992, 1, 2),
        full_time=False,
        total_learners=10040,
    )
    instructor_joy.save()
    instructor_peter = Instructor(
        first_name="Peter",
        last_name="Chen",
        dob=date(1982, 5, 2),
        full_time=True,
        total_learners=2002,
    )
    instructor_peter.save()
    print("Instructor objects all saved... ")


def write_courses() -> None:
    """Create and save Course objects for predefined courses.

    This function instantiates Course objects with specific names and descriptions,
    saves them to the database, and prints a confirmation message upon completion.
    """
    # Add Courses
    course_cloud_app = Course(
        name="Cloud Application Development with Database",
        description="Develop and deploy application on cloud",
    )
    course_cloud_app.save()
    course_python = Course(
        name="Introduction to Python",
        description="Learn core concepts of Python and obtain hands-on "
        "experience via a capstone project",
    )
    course_python.save()

    print("Course objects all saved... ")


def write_lessons() -> None:
    """Create and save Lesson objects for predefined lessons.

    This function instantiates Lesson objects with specific titles and content,
    saves them to the database, and prints a confirmation message upon completion.
    """
    # Add lessons
    lesson1 = Lesson(title="Lesson 1", content="Object-relational mapping project")
    lesson1.save()
    lesson2 = Lesson(title="Lesson 2", content="Django full stack project")
    lesson2.save()
    print("Lesson objects all saved... ")


def write_learners() -> None:
    """Create and save multiple Learner objects with predefined attributes to the database.

    This function instantiates several Learner instances with specific first names, last names,
    dates of birth, occupations, and social links, then saves each instance to the database.
    Intended for populating the database with initial or sample learner data.
    """
    # Add Learners
    learner_james = Learner(
        first_name="James",
        last_name="Smith",
        dob=date(1982, 7, 16),
        occupation="data_scientist",
        social_link="https://www.linkedin.com/james/",
    )
    learner_james.save()
    learner_mary = Learner(
        first_name="Mary",
        last_name="Smith",
        dob=date(1991, 6, 12),
        occupation="dba",
        social_link="https://www.facebook.com/mary/",
    )
    learner_mary.save()
    learner_robert = Learner(
        first_name="Robert",
        last_name="Lee",
        dob=date(1999, 1, 2),
        occupation="student",
        social_link="https://www.facebook.com/robert/",
    )
    learner_robert.save()
    learner_david = Learner(
        first_name="David",
        last_name="Smith",
        dob=date(1983, 7, 16),
        occupation="developer",
        social_link="https://www.linkedin.com/david/",
    )
    learner_david.save()
    learner_john = Learner(
        first_name="John",
        last_name="Smith",
        dob=date(1986, 3, 16),
        occupation="developer",
        social_link="https://www.linkedin.com/john/",
    )
    learner_john.save()

    learner_harry = Learner(
        first_name="Harry",
        last_name="Potter",
        dob=date(1990, 7, 31),
        occupation="student",
        social_link="https://www.linkedin.com/harry/",
    )
    learner_harry.save()

    learner_hermione = Learner(
        first_name="Hermione",
        last_name="Granger",
        dob=date(1990, 9, 19),
        occupation="student",
        social_link="https://www.linkedin.com/hermione/",
    )
    learner_hermione.save()

    print("Learner objects all saved... ")


def clean_data() -> None:
    """Delete all data to start from fresh."""
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


# Clean any existing data first
clean_data()

write_courses()
write_instructors()
write_lessons()
write_learners()
