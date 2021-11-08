from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Answer(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    text = models.TextField()
    like = models.OneToOneField('Like', on_delete=models.CASCADE)


class Profile(models.Model):
    img = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Question(models.Model):
    question_title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


class QuestionLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

class AnswerLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)