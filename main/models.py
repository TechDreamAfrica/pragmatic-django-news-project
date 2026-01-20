from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    mission = models.TextField()
    vision = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to='about_us/logos/')

    def __str__(self):
        return self.title
    

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email
    

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='site_settings/logos/')
    favicon = models.ImageField(upload_to='site_settings/favicons/')

    def __str__(self):
        return self.site_name