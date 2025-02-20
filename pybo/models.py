from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('제목', max_length=200,
                               help_text='질문의 제목을 한 줄로 작성하세요.')
    content = models.TextField('내용', help_text='질문의 내용을 상세히 작성하세요.')
    create_date = models.DateTimeField('생성일')
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.subject}'


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField('답변 내용')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.content