from django.db import models
from accounts.models import User
from courses.models import Course


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.quiz_name)


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_description = models.TextField(null=True)
    choice_1 = models.CharField(max_length=200, null=True)
    choice_2 = models.CharField(max_length=200, null=True)
    choice_3 = models.CharField(max_length=200, null=True)
    choice_4 = models.CharField(max_length=200, null=True)
    correct_choice = models.IntegerField()
    question_image_address = models.ImageField(
        upload_to="images/", blank=True, null=True
    )

    def __str__(self):
        return str(self.question_description)


class Quiz_Questions(models.Model):
    quiz_id = models.ForeignKey("Quiz", on_delete=models.CASCADE)
    question_id = models.ForeignKey("Questions", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quiz_id)


class Results(models.Model):
    quiz_id = models.ForeignKey("Quiz", on_delete=models.CASCADE)
    results_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    score = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
