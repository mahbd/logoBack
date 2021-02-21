from django.contrib import admin
from django import forms
from django_admin_json_editor import JSONEditorWidget

from api.models import SiteData


class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = SiteData
        fields = '__all__'
        widgets = {
            'data': JSONEditorWidget({}, collapsed=False),
        }


@admin.register(SiteData)
class JSONModelAdmin(admin.ModelAdmin):
    list_display = ('category', )
    form = JSONModelAdminForm
