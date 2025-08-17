from typing import ClassVar

from django.db import models
from django.utils.timezone import now


# Define your models from here:
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default="john")
    last_name = models.CharField(null=False, max_length=30, default="doe")
    dob = models.DateField(null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self) -> str:
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Is full time: {self.full_time}, "
            f"Total Learners: {self.total_learners}"
        )


# Learner model
class Learner(User):
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
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT,
    )
    social_link = models.URLField(max_length=200)

    def __str__(self) -> str:
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Date of Birth: {self.dob}, "
            f"Occupation: {self.occupation}, "
            f"Social Link: {self.social_link}"
        )


# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default="online course")
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Learner
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner
    learners = models.ManyToManyField(Learner, through="Enrollment")

    def __str__(self) -> str:
        return f"Name: {self.name}, Description: {self.description}"


class Enrollment(models.Model):
    AUDIT = "audit"
    HONOR = "honor"
    COURSE_MODES: ClassVar[list[tuple[str, str]]] = [
        (AUDIT, "Audit"),
        (HONOR, "Honor"),
    ]
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
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


class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        """Return a string representation of the lesson, showing its title and course.

        Returns:
            str: The lesson's title and associated course name.

        """
        return f"Lesson: {self.title}, Course: {self.course.name if self.course else 'None'}"
