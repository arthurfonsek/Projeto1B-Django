from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        note = Note.objects.create(title=title, content=content, tag='#'+tag)
        note.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all() # <-------- TROQUEI AQUI .ALL() PRA LAST()
    return render(request, 'C:/Users/FONSECA CERTO/Desktop/INSPER/4 SEMESTRE/TECWEB/Projeto1B-Django/notes/templates/notes/index.html', {'notes': all_notes})
        

def delete(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('index')

def updatehtml(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Note.objects.get(id=id)
        return render(request, 'C:/Users/FONSECA CERTO/Desktop/INSPER/4 SEMESTRE/TECWEB/Django/notes/templates/notes/edit.html', {'note': note})
    else:
        return redirect('index')

def updatehtml2(request):
    if request.method == 'POST':
        all_notes = Note.objects.all()
        tags = []
        for note in all_notes:
            if note.tag not in tags:
                tags.append(note.tag)
        return render(request, 'C:/Users/FONSECA CERTO/Desktop/INSPER/4 SEMESTRE/TECWEB/Django/notes/templates/notes/tags.html', {'tags': tags, "notes": all_notes})
    else:
        return redirect('index')

def updatehtml3(request):
    if request.method == 'POST':
        tag = request.POST.get('tag')
        note = Note.objects.get_queryset()
        all_notes = Note.objects.all().filter(tag=tag)
        # listanotas = []
        # for nota in all_notes:
        #     if nota.tag == note.tag:
        #         listanotas.append(nota)
        return render(request, 'C:/Users/FONSECA CERTO/Desktop/INSPER/4 SEMESTRE/TECWEB/Django/notes/templates/notes/tagsin.html', {'notes': all_notes})

def update(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.tag = "#" + request.POST.get('tag')
        note.save()
        return redirect('index')
    else:
        return redirect('index')