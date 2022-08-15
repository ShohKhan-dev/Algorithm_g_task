from django.contrib import admin


# Register your models here.

from .models import Customer, Order, Product, OrderItem

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)


class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        print(request.user)
        super().save_model(request, obj, form, change)
