from django.db import models

class LegalDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='legal_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    risk_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low')

    def __str__(self):
        return self.title

class Clause(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    content = models.TextField()
    is_template = models.BooleanField(default=False)

    def __str__(self):
        return self.title

