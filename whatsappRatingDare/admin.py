from django.contrib import admin

from .models import personOwnChart , answerModel

# Register your models here.
admin.site.register(answerModel)
admin.site.register(personOwnChart)