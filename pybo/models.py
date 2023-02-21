from django.db import models


class Question(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일')

    def __str__(self):
        return f'{self.id} {self.subject}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content