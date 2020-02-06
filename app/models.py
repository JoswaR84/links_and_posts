from django.db import models

class HyperlinkFolder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Hyperlink(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=2000)
    folder = models.ForeignKey(HyperlinkFolder, related_name="links_for_folder", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class IssueItem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)

    def __str__(self):
        return self.title