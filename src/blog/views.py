from django.shortcuts import render, get_object_or_404
from .models import Person
import json


def person_detail(request, person_id):
    obj = get_object_or_404(Person, id=person_id)
    template_name = "person_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def create_person(request):
    payload = json.loads(request.body)
    p = Person(first_name=payload["first_name"], last_name=payload["last_name"], age=payload["age"])
    p.save()
    template_name = "person_detail.html"
    context = {"object": p}
    return render(request, template_name, context)


def update_person(request, person_id):
    payload = json.loads(request.body)
    person = Person.objects.filter(id=person_id)
    person.update(**payload)
    person = Person.objects.get(id=person_id)
    template_name = "update_person.html"
    context = {"object": person}
    return render(request, template_name, context)


def delete_person(request, person_id):
    obj = get_object_or_404(Person, id=person_id)
    obj.delete()
    template_name = "delete_person.html"
    context = {"object": obj}
    return render(request, template_name, context)
