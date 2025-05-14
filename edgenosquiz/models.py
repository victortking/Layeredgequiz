from django.db import models

# Create your models here.
class Question(models.Model):
  text = models.CharField(max_length=500)
  def __str__(self):
    return self.text
    
class Choice(models.Model):
  question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
  text = models.CharField(max_length=200)
  is_correct = models.BooleanField(default=False)
  def __str__(self):
    return self.text