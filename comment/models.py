from django.db import models

# Create your models here.
class Comments(models.Model):

    
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comentss'