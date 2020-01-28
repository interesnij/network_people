from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class New(models.Model):
    title=models.CharField(max_length=100,verbose_name="Заголовок")
    new_slug=models.CharField(max_length=100,verbose_name="Для ссылки")
    description=models.TextField(verbose_name="Краткое содержание")
    content=RichTextUploadingField(blank=True, default='')
    posted=models.DateField(default=timezone.now,verbose_name="Опубликовано")
    views=models.IntegerField(default=0,verbose_name="Просмотры")
    image1=models.ImageField(upload_to="blog/list",verbose_name="Картинка в индес")
    image2=models.ImageField(blank=True,upload_to="blog/list",verbose_name="главная картинка в деталях")


    def get_absolute_url(self):
        return reverse('news_detail',kwargs={"pk":self.pk})

    class Meta:
        ordering=["-posted"]
        verbose_name="новость"
        verbose_name_plural="новости"

    def __str__(self):
        return self.title