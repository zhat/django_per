from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('姓名', max_length=64)
    age = models.SmallIntegerField('年龄')
    choices = (
        (1, '男'),
        (2, '女'),
        (3, '未知')
    )
    sex = models.SmallIntegerField('性别', choices=choices)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='学生表'
        verbose_name_plural='学生表'

class Permission(models.Model):
    name=models.CharField("权限名称",max_length=64)
    url=models.CharField("URL名称",max_length=255)
    choices=((1,'GET'),(2,'POST'))
    per_method=models.SmallIntegerField('请求方法',choices=choices,default=1)
    argument_list=models.CharField('参数列表',max_length=255,help_text='多个参数之间用英文半角逗号隔开',blank=True,null=True)
    describe=models.CharField('描述',max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='权限表'
        verbose_name_plural='权限表'
        permissions=(
            ('views_student_list','查看学员信息表'),
            ('views_student_info','查看学员详细信息'),
        )
