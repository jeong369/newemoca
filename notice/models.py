from django.db import models
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Info(models.Model) :
	title = models.CharField(max_length=100, help_text='최대 100자 내로 입력해주세요')
	content = RichTextUploadingField()
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	available = models.CharField(max_length=1, choices=(
        ('1', '공개'),
		('0', '비공개'),
    ))
	file = models.FileField(null=True, blank=True)