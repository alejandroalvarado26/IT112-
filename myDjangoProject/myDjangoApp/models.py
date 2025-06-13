from django.db import models

# Create your models here.
class Bands(models.Model):
    # Django automatically creates: id = models.AutoField(primary_key=True, **options)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    formation_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/banddetail/{self.id}/"