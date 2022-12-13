from django.contrib import admin

from .models import Category,Product,User, Hotel,Review, Item
from .models import User

#admin.site.register(User)
#admin.site.register(Category)
#admin.site.register(Product)
admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Item)