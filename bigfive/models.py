from django.db import models
from accounts.models import User

# Create your models here.
class OTest(models.Model) :
   	CHOICES_SCORE = (
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		)
   	question = models.TextField()
   	label = models.CharField(max_length=1)
   	facet = models.CharField(max_length=20)
   	score = models.CharField(max_length=1, choices=CHOICES_SCORE)
   	user = models.ForeignKey(User, on_delete=models.CASCADE)

class CTest(models.Model) :
   	CHOICES_SCORE = (
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		)
   	question = models.TextField()
   	label = models.CharField(max_length=1)
   	facet = models.CharField(max_length=20)
   	score = models.CharField(max_length=1, choices=CHOICES_SCORE)
   	user = models.ForeignKey(User, on_delete=models.CASCADE)


class ETest(models.Model) :
   	CHOICES_SCORE = (
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		)
   	question = models.TextField()
   	label = models.CharField(max_length=1)
   	facet = models.CharField(max_length=20)
   	score = models.CharField(max_length=1, choices=CHOICES_SCORE)
   	user = models.ForeignKey(User, on_delete=models.CASCADE)


class ATest(models.Model) :
   	CHOICES_SCORE = (
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		)
   	question = models.TextField()
   	label = models.CharField(max_length=1)
   	facet = models.CharField(max_length=20)
   	score = models.CharField(max_length=1, choices=CHOICES_SCORE)
   	user = models.ForeignKey(User, on_delete=models.CASCADE)


class NTest(models.Model) :
   	CHOICES_SCORE = (
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		)
   	question = models.TextField()
   	label = models.CharField(max_length=1)
   	facet = models.CharField(max_length=20)
   	score = models.CharField(max_length=1, choices=CHOICES_SCORE)
   	user = models.ForeignKey(User, on_delete=models.CASCADE)