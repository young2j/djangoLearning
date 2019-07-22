from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = [(STATUS_NORMAL, '正常'),
                    (STATUS_DELETE, '删除')]

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(
        choices=STATUS_ITEMS,
        default=STATUS_NORMAL,
        verbose_name='状态'
    )
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = [(STATUS_NORMAL, '正常'),
                    (STATUS_DELETE, '删除')]
    name = models.CharField(max_length=50, verbose_name='名称')

    status = models.PositiveIntegerField(
        choices=STATUS_ITEMS,
        default=STATUS_NORMAL,
        verbose_name='状态'
    )
    owner = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    '''
    django2.0版本中,models.OneToOneField()/models.ForeignKey()中的on_delete参数不再为默认值。

    on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选择的值
    CASCADE：此值设置，是级联删除。
    PROTECT：此值设置，是会报完整性错误。
    SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
    SET_DEFAULT：此值设置，会把设置为外键的默认值。
    SET()：此值设置，会调用外面的值，可以是一个函数。
    一般情况下使用CASCADE就可以了。
    '''
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = [
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿')]
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(help_text='正文必须为Markdown格式', verbose_name='正文')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # 　类属性－用于配置Model属性
    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']