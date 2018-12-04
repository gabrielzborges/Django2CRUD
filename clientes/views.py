from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .form import PessoaForm

# Create your views here.
def persons_list(req):
    persons = Pessoa.objects.all()
    return render(req, 'person.html', {'persons': persons})

def person_new(req):
    form = PessoaForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(req, 'person_form.html', {'form': form})

def person_update(req, id):
    person = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(req.POST or None, req.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(req, 'person_form.html', {'form': form})

def person_delete(req, id):
    person = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(req.POST or None, req.FILES or None, instance=person)
    if req.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(req, 'person_delete_confirm.html', {'person':person})