from django.db import models


class Group_info(models.Model):
  group_seq = models.AutoField(primary_key=True)
  owner_seq = models.ForeignKey("User_info", related_name="Group", on_delete=models.CASCADE, db_column="owner")
  name = models.TextField(null=False)
  create_date = models.DateField(auto_now_add=True, verbose_name="create_date")
  

class Membership(models.Model):
  group_seq = models.ForeignKey("Group_seq", related_name="Membership", on_delete=models.CASCADE, db_column="group_seq")
  user_seq = models.ForeignKey("User_seq", related_name="Membership", on_delete=models.CASCADE, db_column="user_seq")
  join_date = models.DateField(auto_now_add=True, verbose_name="create_date")
  auth = models.CharField(max_length=3, null=True, default=None)