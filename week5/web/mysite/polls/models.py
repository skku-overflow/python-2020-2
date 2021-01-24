from django.db import models

# Create your models here.


class Question(models.Model):
    # 왼쪽: 데이터베이스 column 이름
    # 오른쪽: 데이터베이스 column의 타입
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # ForeignKey: 외래 키. 두 데이터를 연결할 때 쓰임.
    # on_delete=models.CASCADE => Question 삭제하면 Choice도 삭제됨
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # default = 0: 별도로 설정 안 한 경우 0 사용
    votes = models.IntegerField(default=0)
