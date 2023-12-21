from django.contrib import admin
from portfolio.models import About 
from portfolio.models import Skills 
from portfolio.models import Testinomial
from portfolio.models import Portfolio
from portfolio.models import Contact

# Register your models here.

admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Testinomial)
admin.site.register(Portfolio)
admin.site.register(Contact)
