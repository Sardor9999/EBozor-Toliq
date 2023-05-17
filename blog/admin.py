from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Address)
# admin.site.register(Product)
admin.site.register(TGUser)
# admin.site.register(Category)

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    search_fields = ('title',)
    inlines = [ProductInline]
    prepopulated_fields = {"slug": ('title',)}
# Register your models here.
