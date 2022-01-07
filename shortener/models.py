from django.db import models

# from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PayPlan(models.Model):
  name = models.TextField(max_length=20)
  price = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Users(AbstractUser):
  # User 데이터베이스에 column 추가
  # 현재 가지고있는 것을 추상화해서 PayPlan을 넣겠다.
  pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

# class UserDetail(models.Model):
#   user = models.OneToOneField(U, on_delete=models.CASCADE)
#   pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)