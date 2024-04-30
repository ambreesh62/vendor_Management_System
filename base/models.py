from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_created=False)

    class Meta:
        abstract = True