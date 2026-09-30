from django.db import models
from django.utils import timezone

class timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        abstract = True

class BaseModel(timestamp):
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        abstract = True

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام نویسنده')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان کتاب')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نویسنده')

    def __str__(self):
        return self.title 

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='کتاب')
    rating = models.IntegerField(verbose_name='امتیاز')
    comment = models.TextField(verbose_name='نظر')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده') 

    def __str__(self):
        return self.book.title + ' - ' + str(self.rating)

    def delete(self):
        self.is_deleted = True
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128 , unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    slug = models.SlugField(max_length=128, unique=True)
    price = models.PositiveIntegerField()

    STATUS_CHOICES = (
        ('0', 'پیش‌نویس'),
        ('1', 'منتشر شده'),
        ('2', 'آرشیو شده')
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    class Meta:
        ordering = ['price']

    def __str__(self):
        return str(self.price)


    