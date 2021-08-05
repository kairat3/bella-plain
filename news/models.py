from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
