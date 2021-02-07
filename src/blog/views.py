from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Person


def person_detail(request, person_id):
    # obj = Person.objects.get(id=person_id)
    obj = get_object_or_404(Person, id=person_id)
    template_name = "person_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)
