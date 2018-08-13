# coding=utf-8

import markdown

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags


@python_2_unicode_compatible
class Smms(models.Model):

    hash = models.CharField(max_length=255)
    ip = models.CharField(max_length=30)
    height = models.IntegerField()
    width = models.IntegerField()
    size = models.IntegerField()
    path = models.CharField(max_length=255)
    storename = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    filename = models.CharField(max_length=50)
    timestamp = models.IntegerField()
    delete = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'smms'


@python_2_unicode_compatible
class Category(models.Model):

    name = models.CharField(max_length=100, help_text='分类名')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=100, help_text='标签名')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):

    title = models.CharField(max_length=70, help_text='文章标题')
    body = models.TextField(help_text='文章正文')
    created_time = models.DateTimeField(help_text='创建时间')
    modified_time = models.DateTimeField(help_text='最后一次修改时间')
    excerpt = models.CharField(max_length=200, blank=True, help_text='文章摘要')
    views = models.PositiveIntegerField(default=0, help_text='阅读量')
    category = models.ForeignKey(Category, help_text='分类')
    tags = models.ManyToManyField(Tag, blank=True, help_text='标签')
    author = models.ForeignKey(User, help_text='作者')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']
