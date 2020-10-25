from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["pk", "btitle", "bpub_data"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["pk", "hname", "hgender", "hcontent"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

