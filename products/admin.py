from django.contrib import admin
from .models import Product, TopCategory, MidCategory, BottomCategory, Follower, ProductImage


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


class AdminTopCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminMidCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminBottomCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminFollowers(admin.ModelAdmin):
    list_display = ('email',)


class AdminProductImages(admin.ModelAdmin):
    list_display = ('extra_image',)


admin.site.register(Product, AdminProduct)
admin.site.register(TopCategory, AdminTopCategory)
admin.site.register(MidCategory, AdminMidCategory)
admin.site.register(BottomCategory, AdminBottomCategory)
admin.site.register(Follower, AdminFollowers)
admin.site.register(ProductImage, AdminProductImages)



