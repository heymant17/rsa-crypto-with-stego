from django.db import models

# Create your models here.
class Room(models.Model):
 roomname = models.CharField(max_length=1000)

class Message(models.Model):
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    content = models.TextField(blank=True, null=True)
    length = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
    

class KeyDetails(models.Model):
    cipher_text = models.TextField(blank=True, null=True)
    prime_multiple = models.TextField(blank=True, null=True)
    phi = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    stego_image = models.ImageField(null=True,blank=True,upload_to="images/")
