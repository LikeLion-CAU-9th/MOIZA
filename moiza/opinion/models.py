from django.db import models

class Suggestion(models.Model) :
    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY')
    ]
    topic = models.CharField(max_length = 80, null=True, help_text="제목")
    other_opinion = models.BooleanField(default=True)
    no_opinion= models.BooleanField(default=True)

class Opinion(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete = models.CASCADE, null=False, related_name='suggestions')
    opinion_contents = models.CharField(max_length=100)