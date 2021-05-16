from django.contrib import admin
from api.models import Branch

# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display = ('ifsc', 'bank_id')

admin.site.register(Branch, BranchAdmin)