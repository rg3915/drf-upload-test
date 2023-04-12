from django.db import models


class Document(models.Model):
    document = models.FileField('documento', upload_to='', null=True, blank=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return f'{self.document}'
