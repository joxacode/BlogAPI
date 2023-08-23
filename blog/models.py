from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Title(BaseModel):
    title = models.CharField(max_length=40)


class Author(BaseModel):
    full_name = models.CharField(max_length=120, verbose_name='Full Name')
    profession = models.CharField(max_length=255, verbose_name='Profession')
    image = models.ImageField(upload_to='media/author_image')


class SocialLinks(BaseModel):
    name = models.CharField(max_length=30, verbose_name='Name')
    url = models.URLField(max_length=255, verbose_name='Url')
    order = models.PositiveIntegerField(default=1)
    icon = models.CharField(max_length=255, verbose_name='Icon')

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return f'{self.id}{self.name}'


class Blog(BaseModel):
    title = models.CharField(max_length=120, verbose_name='Title')
    description = RichTextField()


class Technologies(BaseModel):
    title = models.CharField(max_length=40, verbose_name='Title')
    image = models.ImageField(upload_to='media/technologies')


class Talks(BaseModel):
    image = models.ImageField(upload_to='media/author_image')
    title = models.CharField(max_length=40, verbose_name='Title')
    project_url = models.URLField(max_length=255, verbose_name='Url')
    tools = models.ManyToManyField(Technologies)


class Channel(BaseModel):
    url = models.URLField(max_length=255, verbose_name='Url')





