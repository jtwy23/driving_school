from django.contrib import admin
from .models import EmailConfirmed, Categories, products, customer_more_information

# Register your models here.

class EmailConfirmedAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'activation_key', 'email_confirmed']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(EmailConfirmed, EmailConfirmedAdmin)
admin.site.register(Categories)
admin.site.register(products)
admin.site.register(customer_more_information)

