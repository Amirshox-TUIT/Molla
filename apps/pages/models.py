from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class AboutModel(models.Model):
    full_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    self_photo = models.ImageField(upload_to='images/')
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    instagram_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'




