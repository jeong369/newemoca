from django.db import models
from accounts.models import User

# Create your models here.
class Test(models.Model) :
	question = models.TextField(null=False, blank=False)
	question_ko = models.TextField(null=True, blank=True)
	# label : N 
	label = models.CharField(max_length=1, null=False, blank=False)
	# facet : 6가지 특징
	facet = models.CharField(max_length=20, blank=True)
	# test number (12, 50, 100, ...)
	testname = models.IntegerField(null=True)
	# key : 1 or -1
	key = models.IntegerField(blank=False)
	score_users = models.ManyToManyField(User, through='Score', related_name='score_tests')

class Score(models.Model) :
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	users = models.ForeignKey(User, on_delete=models.CASCADE)
	grade = models.IntegerField(choices=(
   		(1, '전혀 그렇지 않다.'),
   		(2, '그렇지 않다.'),
   		(3, '보통이다.'),
   		(4, '약간 그렇다.'),
   		(5, '매우 그렇다.'),
   		))

class Adjective(models.Model) :
	label = models.CharField(max_length=1, blank=False)
	word = models.CharField(max_length=100, blank=False)