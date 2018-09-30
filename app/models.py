from transliterate import translit

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
	name=models.CharField(max_length=50)
	slug=models.SlugField(blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural='Категории'


class Brand(models.Model):
	name=models.CharField(max_length=50)
	slug=models.SlugField(blank=True)
	def __str__(self):
		return self.name

@receiver(pre_save, sender=Categories)
def pre_save_categories_slug(sender,instance, *args,**kwargs):
	slug=slugify(translit(str(instance.name), reversed=True))
	instance.slug=slug

@receiver(pre_save, sender=Brand)
def pre_save_brand_slug(sender, instance, *args, **kwargs):
	slug=slugify(str(instance.name))
	instance.slug=slug

def image_folder(instance, filename):
	filename=instance.title+'.'+filename.split('.')[-1]
	return '{0}/{1}/{2}/{3}'.format(instance.category.slug, instance.brand.slug, instance.slug,filename)

class Products(models.Model):
	title=models.CharField(max_length=50)
	category=models.ForeignKey(Categories, on_delete=models.CASCADE)
	slug=models.SlugField(blank=True)
	brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
	descriptions=models.TextField(blank=True)
	image=models.ImageField(blank=True, upload_to=image_folder)
	price=models.DecimalField(max_digits=9, decimal_places=2)
	available=models.BooleanField(default=True)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural='Products'
	def get_url(self):
		return reverse('product', kwargs={'slug':self.slug})

@receiver(pre_save, sender=Products)
def pre_save_product_slug(sender, instance, *args, **kwargs):
	slug=''
	for i in instance.title:
		if i.isupper():
			i=i.lower()
		if i==' ':
			i='-'
			slug+=i
		else:
			slug+=i
	instance.slug=slug