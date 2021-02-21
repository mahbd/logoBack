from django.contrib import admin
from django import forms
from django_admin_json_editor import JSONEditorWidget

from .models import SiteData, Message, NewsletterSubscriber, Work


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


admin.site.register(Message)
admin.site.register(NewsletterSubscriber)
admin.site.register(Work)
