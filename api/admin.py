from django.contrib import admin
from api.models import Branch, Bank

# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display = ('ifsc', 'bank_id')

class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Branch, BranchAdmin)
admin.site.register(Bank, BankAdmin)