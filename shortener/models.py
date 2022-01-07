from django.db import models

# Create your models here.
class PayPlan(models.Model):
  name = models.TextField(max_length=20)
  price = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  