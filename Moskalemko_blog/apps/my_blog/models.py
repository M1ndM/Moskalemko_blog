from django.db import models

# Create your models here.

class Keywords(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.id} {self.key_word}'

class Post(models.Model):
    id = models.BigAutoField(primary_key = True)
    post_title = models.CharField(max_length=100)
    post_anatation = models.CharField(max_length=200)
    post_text = models.TextField()
    key_words = models.ManyToManyField(Keywords)
    def __str__(self):
        return f'{self.id} {self.post_title}'

