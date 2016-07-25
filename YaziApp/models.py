from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kategoriler(models.Model):
	baslik = models.CharField(max_length=40,help_text="Kategoriye vereceğiniz başlığı giriniz.",verbose_name="Kategori adı")
	sef = models.SlugField()
	
	def __str__(self):
		return self.baslik
		
	class Meta:
		verbose_name_plural = "Kategoriler"
		
	def save(self,*args,**kwargs):
		super(Kategoriler,self).save(*args,**kwargs)
		
class Etiketler(models.Model):
	baslik = models.CharField(max_length=40,help_text="Etiketi giriniz.",verbose_name="Etiket")
	sef = models.SlugField()
	
	def __str__(self):
		return self.baslik
		
	class Meta:
		verbose_name_plural = "Etiketler"
		
	def save(self,*args,**kwargs):
		super(Etiketler,self).save(*args,**kwargs)
		
class Yazilar(models.Model):
	baslik = models.CharField(max_length=255,help_text="Yazının başlığını giriniz.",verbose_name="Yazı başlığı")
	sef = models.SlugField(max_length=255)
	kategori = models.ForeignKey(Kategoriler, on_delete=models.CASCADE,help_text="Yazının kategorisini seçiniz.",verbose_name="Yazı kategorisi")
	uye = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Yazının sahibini seçiniz.",verbose_name="Yazar")
	icerik = models.TextField(help_text="Yazının içeriğini giriniz.",verbose_name="Yazı içeriği")
	etiketler = models.ManyToManyField(Etiketler)
	
	def __str__(self):
		return self.baslik
		
	class Meta:
		verbose_name_plural = "Yazılar"
		
	def save(self,*args,**kwargs):
		super(Yazilar,self).save(*args,**kwargs)