"""Models for the application."""

from typing import ClassVar

from django.db import models
from django.utils.timezone import now

# Define your models from here:


# User model
class User(models.Model):
    """Represents a user with first name, last name, and date of birth.

    Attributes
    ----------
    first_name : str
        The user's first name.
    last_name : str
        The user's last name.
    dob : date
        The user's date of birth.

    """

    first_name = models.CharField(null=False, max_length=30, default="john")
    last_name = models.CharField(null=False, max_length=30, default="doe")
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self) -> str:
        """Return a string representation of the object, combining the first and last name.

        Returns:
            str: The full name of the object in the format 'first_name last_name'.

        """
        return self.first_name + " " + self.last_name


# Instructor model
class Instructor(User):
    """Represents an instructor, inheriting from User.

    Attributes
    ----------
    full_time : bool
        Indicates if the instructor is full-time.
    total_learners : int
        The total number of learners taught by the instructor.

    """

    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self) -> str:
        """Return a string representation of the object.

        That including the first name, last name, full-time status, and total number of learners.

        Returns:
            str: A formatted string with the object's first name, last name, full-time status, and
            total learners.

        """
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Is full time: {self.full_time}, "
            f"Total Learners: {self.total_learners}"
        )


# Learner model
class Learner(User):
    """Learner model extending the User model with additional fields.

    Fields:
        occupation (CharField): The occupation of the learner, with choices including
            'Student', 'Developer', 'Data Scientist', and 'Database Admin'.
        social_link (URLField): A URL to the learner's social media or professional profile.

    Methods:
        __str__(): Returns a string representation of the learner, including first name,
            last name, date of birth, occupation, and social link.

    """

    STUDENT = "student"
    DEVELOPER = "developer"
    DATA_SCIENTIST = "data_scientist"
    DATABASE_ADMIN = "dba"
    OCCUPATION_CHOICES: ClassVar[list[tuple[str, str]]] = [
        (STUDENT, "Student"),
        (DEVELOPER, "Developer"),
        (DATA_SCIENTIST, "Data Scientist"),
        (DATABASE_ADMIN, "Database Admin"),
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT,
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)

    # Create a toString method for object string representation
    def __str__(self) -> str:
        """Return a string representation of the object.

        This includes the first name, last name, date of birth, occupation, and social link.

        Returns:
            str: A formatted string containing the object's details.

        """
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Date of Birth: {self.dob}, "
            f"Occupation: {self.occupation}, "
            f"Social Link: {self.social_link}"
        )


# Course model
class Course(models.Model):
    """Represent a course with a name, description, and instructors.

    Attributes
    ----------
    name : str
        The name of the course.
    description : str
        The description of the course.
    instructors : ManyToManyField
        The instructors associated with the course.

    """

    name = models.CharField(null=False, max_length=100, default="online course")
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner
    learners = models.ManyToManyField(Learner, through="Enrollment")

    # Create a toString method for object string representation
    def __str__(self) -> str:
        """Return a string representation of the object, including its name and description.

        Returns:
            str: A formatted string containing the object's name and description.

        """
        return f"Name: {self.name}, Description: {self.description}"


# Lesson
class Lesson(models.Model):
    """Represent a lesson within a course.

    Attributes
    ----------
    title : str
        The title of the lesson.
    course : ForeignKey
        The course to which the lesson belongs.
    content : str
        The content of the lesson.

    """

    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        """Return a string representation of the lesson, showing its title and course.

        Returns:
            str: The lesson's title and associated course name.

        """
        return f"Lesson: {self.title}, Course: {self.course.name if self.course else 'None'}"


# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    """Represents the enrollment of a learner in a course.

    Fields:
        learner (ForeignKey): Reference to the Learner who is enrolled.
        course (ForeignKey): Reference to the Course in which the learner is enrolled.
        date_enrolled (DateField): The date when the enrollment was created.
        mode (CharField): The enrollment mode, either 'audit' or 'honor'.
    """

    AUDIT = "audit"
    HONOR = "honor"
    COURSE_MODES: ClassVar[list[tuple[str, str]]] = [
        (AUDIT, "Audit"),
        (HONOR, "Honor"),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

    def __str__(self) -> str:
        """Return a string representation of the enrollment, showing learner and course details.

        Returns:
            str: The learner's name and the course title.

        """
        return (
            f"Enrollment: {self.learner.first_name} enrolled in {self.course.name} on "
            f"{self.date_enrolled}."
        )
