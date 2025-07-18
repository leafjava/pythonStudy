from django.db import models
from account.models import User
from utils.initialmodels import initialModel

# Create your models here.
# class Article(models.Model):
#   id = models.IntegerField(primary_key=True)
#   title = models.CharField(max_length=120)
#   content = models.TextField()
#   publish_date = models.DateTimeField()
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

#   class Meta:
#     db_table = 'article'
#     verbose_name = '文章信息'
#     ordering = ['-publish_date']

class Article(initialModel):
  id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=120)
  content = models.TextField()
  publish_date = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'article'
    verbose_name = '文章信息'
    ordering = ['-publish_date']


