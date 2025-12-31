from django.contrib import admin
from .models import LegalDocument, Clause

@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'risk_level')
    list_filter = ('risk_level',)

@admin.register(Clause)
class ClauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_template')
    list_filter = ('category', 'is_template')

