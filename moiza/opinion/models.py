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
    
    group_seq = models.ForeignKey(on_delete = models.CASCADE, null=False)
    topic = models.CharField(max_length = 80, null=True, help_text="제목")
    other_selection = models.BooleanField(default=True)
    no_selection= models.BooleanField(default=True)

class Selection(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete = models.CASCADE, null=False, related_name='suggestions')
    selection_content = models.CharField(max_length=100)
