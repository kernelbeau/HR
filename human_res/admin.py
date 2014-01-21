from django.contrib import admin

from human_res.models import *


class EmployeeAdmin(admin.ModelAdmin):
    fields = (('name_first', 'name_last'),)


class AddressAdmin(admin.ModelAdmin):
    fields = ('employee', 'address', ('city', 'state', 'zip_code'), 'address_type')
    ordering = ['employee', 'address_type']


class EmailAdmin(admin.ModelAdmin):
    fields = ('employee', 'email')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Address, AddressAdmin)
