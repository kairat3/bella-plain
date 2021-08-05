from django.db import models


class About(models.Model):
    logo = models.CharField(max_length=250, default='Bella', blank=False)
    description = models.TextField()
    description2 = models.TextField()

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

    def __str__(self):
        return self.logo


class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return "Image" + str(random.randint(1, 99999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} --> {self.about}"
