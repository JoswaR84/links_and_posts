from django import forms
from .models import *

class HyperlinkFolderForm(forms.ModelForm):
    class Meta:
        model = HyperlinkFolder
        fields = ('name',)

class HyperlinkForm(forms.ModelForm):
    class Meta:
        model = Hyperlink
        fields = ('name', 'link', 'folder')

class IssueItemForm(forms.ModelForm):
    class Meta:
        model = IssueItem
        fields = ('title', 'body')