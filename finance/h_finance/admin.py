from django.contrib import admin

from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class CostsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Costs
        fields = '__all__'

class CostsAdmin(admin.ModelAdmin):
    form = CostsAdminForm
    save_on_top = True
    list_display = ('id', 'author', 'title', 'category', 'data', 'amount', 'place_where_spent')
    list_display_link = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)




admin.site.register(Category)
admin.site.register(Costs, CostsAdmin)


# Register your models here.
