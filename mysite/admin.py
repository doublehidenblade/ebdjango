from django.contrib import admin
from .models import person
from .models import subs
from .models import film
from .models import memory
# Register your models here.

admin.site.register(person)
admin.site.register(subs)
admin.site.register(film)
admin.site.register(memory)