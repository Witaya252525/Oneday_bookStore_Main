


from django.db import models
from django.utils.html import format_html


BOOK_LEVEL_CHOICE = (
('Evaluation','Evaluation'),
('Design','Design'),
('Implementation','Implementation'),
('ECN under review','ECN under review'),

)






class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'ผู้เเต่ง'

    def __str__(self) -> str:
        """Return a string representation of the author's name."""
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'หมวดหมู่'

    def __str__(self):
        return self.name


class Book(models.Model):
    code = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    # Category is one but book is many
    category = models.ForeignKey (Category , null=True ,blank = True ,on_delete=models.CASCADE)
    # need only blank = True  , null noneed because it is many to many
    author = models.ManyToManyField (Author ,blank = True)
    level = models.CharField (max_length=20 ,null=True ,blank = True , choices=BOOK_LEVEL_CHOICE)
    image = models.FileField(upload_to = 'upload', null=True ,blank = True)
    # image2 = models.FileField(upload_to = 'upload', null=True ,blank = True)
    price = models.FloatField(default=0)
    # status = models.CharField (max_length=10 ,null=True ,blank = True , choices=BOOK_STATUS)
    published = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = 'หนังสือ'
        ordering = ['-create']

    def __str__(self):
        return self.name

    def show_image(self):
        if self.image:
            return format_html ( '<img src= "%s"   +  height ="50px">'   %self.image.url )
        return ''
    show_image.allow_tags = True
    show_image.short_descripttion = 'Image'




class BookComment(models.Model):
    book = models.ForeignKey (Book  ,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name_plural = 'BookComment'
        ordering = ['id']


    def __str__(self):
        return self.comment








