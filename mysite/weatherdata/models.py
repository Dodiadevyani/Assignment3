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

class WeatherLog(models.Model):
    location = models.ForeignKey(Location, verbose_name=_("location"))
    timestamp = models.DateTimeField(_("timestamp"))
    mean_temperature = models.IntegerField(_("temperature (C°)"))
    rainfall = models.IntegerField(_("rainfall (mm)"))
    min_temperature = models.IntegerField(_("temperature (C°)"))
    max_temperature = models.IntegerField(_("temperature (C°)"))
    sunshine = models.IntegerField(_("sunshine (hrs)"))
    
    class Meta:
        verbose_name=_("weather log")
        verbose_name_plural=_("weather logs")
        ordering = ("-timestamp",)
    
    def __unicode__(self):
        return "%s @ %s" % (
            self.location.name,
            self.timestamp.strftime("%Y-%m-%dT%H:%M"),
            )

