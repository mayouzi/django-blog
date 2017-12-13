# coding=utf-8

from django.db import models

from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100, help_text='姓名')
    email = models.EmailField(max_length=255, help_text='邮箱')
    url = models.URLField(blank=True, help_text='个人网址')
    text = models.TextField(help_text='内容')
    created_time = models.DateTimeField(auto_now_add=True, help_text='评论时间')
    post = models.ForeignKey('blog.Post', help_text='评论的文章')

    def __str__(self):
        return self.text[:20]
