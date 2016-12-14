from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    weather_parameters = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    location_id = models.CharField(
        ("location ID"),
        max_length=20,
        )
    
    class Meta:
        verbose_name=_("location")
        verbose_name_plural=_("locations")
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Weather(models.Model):
    location = models.ForeignKey(Post, verbose_name=("location"))
    Tmean = models.FloatField()
    Rainfall = models.FloatField()
    Tmin = models.FloatField()
    Tmax = models.FloatField()
    Sunshine = models.FloatField()
    
    class Meta:
        verbose_name=("weather log")
        verbose_name_plural=("weather logs")
    
    def __unicode__(self):
        return "%s @ %s" % (
            self.location.name,
            self.timestamp.strftime("%Y-%m-%dT%H:%M"),
            )

