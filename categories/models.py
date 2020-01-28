from django.db import models


class Category(models.Model):
	name=models.CharField(max_length=100,db_index=True,unique=True,verbose_name="Название")
    slug=models.CharField(max_length=100,db_index=True,unique=True,verbose_name="Название для url")
	image=models.ImageField(null=True,blank=True,upload_to="blog_subcategories/list")
	order=models.PositiveSmallIntegerField(default=0,db_index=True,verbose_name="Порядковый номер")
	def __str__(self):
		return self.name
	class Meta:
		ordering=["order","name"]
		verbose_name="категория людей"
		verbose_name_plural="категории людей"

	def __str__(self):
		return self.name