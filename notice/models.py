from django.db import models
from accounts.models import User
# Create your models here.
class Info(models.Model) :
	title = models.CharField(max_length=100, help_text='최대 100자 내로 입력해주세요')
	content = models.TextField()
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	available = models.IntegerField()