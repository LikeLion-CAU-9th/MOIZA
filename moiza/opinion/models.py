from django.db import models
from account.models import User_info

class Group_info(models.Model):
  group_seq = models.AutoField(primary_key=True)
  owner = models.ForeignKey(User_info, related_name="Group", on_delete=models.CASCADE, db_column="owner")
  name = models.TextField(null=False)
  create_date = models.DateField(auto_now_add=True, verbose_name="create_date")
  
class Membership(models.Model):
  group = models.ForeignKey(Group_info, related_name="Membership", on_delete=models.CASCADE, db_column="group_seq")
  user = models.ForeignKey(User_info, related_name="Membership", on_delete=models.CASCADE, db_column="user_seq")
  join_date = models.DateField(auto_now_add=True, verbose_name="create_date")
  auth = models.CharField(max_length=3, null=True, default=None)

class Response(models.Model):
  response_seq = models.AutoField(primary_key=True)
  writer = models.ForeignKey()