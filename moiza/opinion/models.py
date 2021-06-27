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

class Suggestion(models.Model) :
    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY')
    ]
    
    group_sequence = models.ForeignKey(Group_info, on_delete = models.CASCADE, null=False,related_name='group_seq2')
    topic = models.CharField(max_length = 80, null=True, help_text="제목")
    other_selection = models.BooleanField(default=True)
    no_selection= models.BooleanField(default=True)

class Selection(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete = models.CASCADE, null=False, related_name='suggestions')
    selection_content = models.CharField(max_length=100)

class Response(models.Model):
  response_seq = models.AutoField(primary_key=True)
  suggestion = models.ForeignKey(Suggestion, on_delete = models.CASCADE, null=False)
  writer = models.ForeignKey(User_info, null=False, on_delete=models.CASCADE)
  selection_seq = models.ForeignKey(Selection, on_delete = models.CASCADE, null=False)
  content = models.TextField(null=False, help_text = "이유 및 의견")