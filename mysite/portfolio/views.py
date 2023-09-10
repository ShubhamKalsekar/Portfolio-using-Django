from django.shortcuts import render
from .models import About
from .models import Skills
from .models import Testinomial
from .models import Portfolio
from .models import Contact

# Create your views here.
def index(request):
    About_obj = About.objects.all()
    Skills_obj = Skills.objects.all()
    Testinomial_obj = Testinomial.objects.all()
    Portfolio_obj2 = Portfolio.objects.filter(year=2)
    Portfolio_obj3 = Portfolio.objects.filter(year=3)
    Portfolio_obj4 = Portfolio.objects.filter(year=4)

    return render(request,"index.html",{"about":About_obj,"skill":Skills_obj,"Testinomial":Testinomial_obj, "Portfolioobj2":Portfolio_obj2, "Portfolioobj3":Portfolio_obj3, "Portfolioobj4":Portfolio_obj4})

def contact(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    c_obj = Contact(name=name,email=email,subject=subject,message=message)
    c_obj.save()

    return render(request,"index.html", {"msg": "Thank You! I will contact you soon"})
