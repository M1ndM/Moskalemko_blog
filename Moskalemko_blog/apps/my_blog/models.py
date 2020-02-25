from django.db import models

# Create your models here.

class Keywords(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.id} {self.key_word}'


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='static\imgs', blank=True)
    is_active = models.BooleanField(default=False)
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'
    GENDER_CHOICES = [(Male,'Male'),(Female, 'Female'), (Other, 'Other')]
    gender_choices = models.CharField(max_length=100, choices=GENDER_CHOICES,default=Other)
    email = models.CharField(max_length=150)
    country  = models.CharField(max_length=150)
    author_description  = models.TextField(default='Это один из наших авторов')
    author_status = models.CharField(max_length=300, default=birth_date)

    def __str__(self):
        return f'{self.id} {self.author_name}'


class Post(models.Model):
    id = models.BigAutoField(primary_key = True)
    post_title = models.CharField(max_length=100)
    post_anatation = models.CharField(max_length=200)
    post_text = models.TextField()
    key_words = models.ManyToManyField(Keywords)
    post_foto = models.ImageField( upload_to='static\imgs', blank=True)


    def __str__(self):
        return f'{self.id} {self.post_title}'







