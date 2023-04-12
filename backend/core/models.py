from django.db import models


class Document(models.Model):
    document = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.document}"

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
