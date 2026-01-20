from django.db import models

# Create your models here.
class Reporters(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='reporters/profile_pictures/')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Articles(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(Reporters, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='articles/featured_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Images(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='articles/images/')

    def __str__(self):
        return f"Image for {self.article.headline}"
    

class Videos(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()

    def __str__(self):
        return f"Video for {self.article.headline}"
