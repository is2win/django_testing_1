from django.db import models


class DocCheck(models.Model):
    title = models.CharField(max_length=25)
    file_mssp = models.FileField(upload_to='documents/mssp/')
    file_quotes = models.FileField(upload_to='documents/quotes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CheckerFiles(models.Model):
    title = models.CharField(max_length=25)
    dock_check = models.ForeignKey(DocCheck,
                                   on_delete=models.CASCADE,
                                   related_name='check_files')
    result = models.CharField(max_length=25)
    checked_at = models.DateTimeField(auto_now_add=True)
