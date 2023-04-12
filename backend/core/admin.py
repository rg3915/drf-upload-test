from django.contrib import admin

from backend.core.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    exclude = ()
