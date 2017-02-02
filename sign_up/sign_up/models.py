import uuid
from django.db import models


class signupModel(models.Model):
    first_name= models.CharField(max_length=120, null=False, blank=False)
    last_name= models.CharField(max_length=120, null=False, blank=False)
    email_address= models.EmailField(max_length=120, null=False, blank=False)
    tech256_username = models.CharField(max_length=120, null=True, blank=True)
    webste_url= models.URLField(max_length=200, null=True, blank=True)
    # Define variables for option
    newsletter_no= 'NO'
    newsletter_yes= 'YES'
    newsletter_options= ((newsletter_no, 'No -I hate junk email'),(newsletter_yes, 'Yes -Send it to my spam account'),)
    # Default database column/type and reference variables defined above
    newsletter_preference= models.CharField(max_length=4, choices=newsletter_options, default=newsletter_yes)
    talk_description= models.TextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    sid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
def __str__(self):
    return self.sid