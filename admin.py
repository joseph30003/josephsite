from django.contrib import admin

# Register your models here.
from .models import words,references,Query,Answer,Sections,Characters,GeneSyn

admin.site.register(words)
admin.site.register(references)
admin.site.register(Query)
admin.site.register(Answer)
admin.site.register(Sections)
admin.site.register(Characters)
admin.site.register(GeneSyn)