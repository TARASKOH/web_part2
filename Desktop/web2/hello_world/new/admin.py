from django.contrib import admin

# Register your models here.
from.models import Person
admin.site.register(Person)


from.models import Place
admin.site.register(Place)

from.models import Restaurant
admin.site.register(Restaurant)

from.models import Waiter
admin.site.register(Waiter)

from.models import Reporter
admin.site.register(Reporter)

from.models import Article
admin.site.register(Article)

# from.models import Meta
# admin.site.register(Meta)

from.models import Publication
admin.site.register(Publication)

from.models import Magazine
admin.site.register(Magazine)
