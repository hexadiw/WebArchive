from django.db import models

# Create your models here.
class Archive(models.Model):
    file_name = models.CharField(max_length=255)
    file_number = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return self.file_name