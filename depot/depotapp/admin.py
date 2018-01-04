from django.contrib import admin
from .models import Product,User,Store
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
# Register your models here.
#class UserProfileInline(admin.StackedInline):
#	model = UserProfile
#	fk_name = 'user'
#	max_num =1
#class UserProfileAdmin(UserAdmin):
#	inlines = [UserProfileInline,]
admin.site.register(Product)

#admin.site.unregister(User)
#admin.site.register(User,UserProfileAdmin)
admin.site.register(User)
admin.site.register(Store)