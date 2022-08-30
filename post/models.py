from django.contrib.auth.models import User
from django.db import models


class PostTag(models.Model):
    P_tag = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table='t_tg'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.P_tag


class PostState(models.Model):
    state = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 't_st'
        verbose_name = '状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.state


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,unique=True)
    content = models.TextField()
    desc = models.CharField(max_length=100, unique=True)
    isdelete = models.BooleanField(default=False)
    createdate = models.DateField(auto_now_add=True)
    updatedate = models.DateField(auto_now=True)
    state = models.ManyToManyField(PostState)
    tag = models.ManyToManyField(PostTag)

    class Meta:
        db_table = 't_post'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
