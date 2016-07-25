from django.contrib import admin
from YaziApp.models import *

# Register your models here.
class KategorilerAdmin(admin.ModelAdmin):
	list_display = ('baslik',)
	prepopulated_fields = {"sef": ("baslik",)}
	
class EtiketlerAdmin(admin.ModelAdmin):
	list_display = ('baslik',)
	prepopulated_fields = {"sef": ("baslik",)}
	
class YazilarAdmin(admin.ModelAdmin):
	list_display = ('baslik','kategori','icerik','uye',)
	prepopulated_fields = {"sef": ("baslik",)}
	
admin.site.register(Kategoriler,KategorilerAdmin)
admin.site.register(Etiketler,EtiketlerAdmin)
admin.site.register(Yazilar,YazilarAdmin)