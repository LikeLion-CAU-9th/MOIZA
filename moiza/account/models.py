from django.db import models

class user_info(models.Model):
  user_seq = models.AutoField(primary_key=True)
  user_id = models.TextField(null=False)
  user_pw = models.TextField()
  user_email = models.EmailField(max_length=254, verbose_name="user_email", blank=False)
  register_date = models.DateField(auto_now_add=True, verbose_name="register_date")
  