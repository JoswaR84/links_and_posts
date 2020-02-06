from django.contrib import admin
from .models import *

class HyperlinkFolderAdmin(admin.ModelAdmin):
    list_display = ('name',)    

class HyperlinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'folder')    

class IssueItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

admin.site.register(HyperlinkFolder, HyperlinkFolderAdmin)
admin.site.register(Hyperlink, HyperlinkAdmin)
admin.site.register(IssueItem, IssueItemAdmin)