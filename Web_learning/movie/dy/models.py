from django.db import models


class CyModels(models.Model):  # 创建数据库和写入读取数据

    def __init__(self):
        super().__init__()
        self.id = models.AutoField(primary_key=True)  # 增加一个自动增长的字段
        self.title = models.CharField(max_length=100, null=False)
        self.content = models.TextField(null=False)
        self.link = models.CharField(max_length=100, null=False)
