from io import BytesIO
from PIL import Image


from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):

    user_age= models.IntegerField(null=True)
    user_sallary= models.IntegerField(null=True)
    user_sex= models.IntegerField( null=True)
    
    REQUIRED_FIELDS = ['user_age', 'user_sallary','user_sex']
    
    class Meta:
     ordering = ('id',)
       
    def __str__(self):
           return str(self.id)



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.id}/'

    #def get_absolute_url(self):
        #return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

# class User (models.Model):
#     name = models.CharField(max_length=255)
#     old  = models.DecimalField(max_digits=3, decimal_places=2)
#     salarry = models.DecimalField(max_digits=6, decimal_places=2)
#     slug = models.SlugField()
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='uploads/', blank=True, null=True)
#     thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#      ordering = ('id',)
       
#     def __str__(self):
#            return str(self.id)
       
#     def get_absolute_url(self):
#            return f'/{self.slug}/'


class Hotel (models.Model):
    user_id = models.ForeignKey(User, related_name='hotels', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=0,default='500' )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    phoneNumber = models.DecimalField(max_digits=9,decimal_places=0, default='043534512')
    class Meta:
        ordering = ('id',)
    
    def __str__(self):
           return str(self.id)
    
    def get_absolute_url(self):
        return f'/{self.id}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Review (models.Model):
    hotel_id =  models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mark = models.DecimalField(max_digits=1, decimal_places=0)
    description = models.CharField(max_length=2000, blank=True, null=True)
    class Meta:
     ordering = ('id',)

    def __str__(self):
           return str(self.id)

class Item (models.Model):
    user_id = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, db_constraint=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=0,default='500')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    mse = models.TextField(blank=True, null=True)
    rmse = models.TextField(blank=True, null=True)
    minprice = models.TextField(blank=True, null=True)
    mindate = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    plot = models.ImageField(upload_to='uploads/', blank=True, null=True)
    class Meta:
        ordering = ('id',)
    
    def __str__(self):
           return str(self.id)
    
    def get_absolute_url(self):
        return f'/{self.id}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_plot(self):
     if self.plot:
         return 'http://127.0.0.1:8000' + self.plot.url
     return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail           
   

   