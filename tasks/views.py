from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

tasks = ["foo", "bar", "baz"]

def index(request):

    # Verifique se já existe uma chave "tasks" em nossa sessão

    if "tasks" not in request.session:
        
        # Se não estiver, cria uma nova lista

        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks":tasks
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def add(request):

    # Verificd se o método é POST

    if request.method == "POST":
        
        # Pegue os dados que o usuário enviou e salve-os como formulário

        form = NewTaskForm(request.POST)

        # Verifique se os dados do formulário são válidos (do lado do servidor)

        if form.is_valid():

            # Isole a tarefa da versão 'limpa' dos dados do formulário

            task = form.cleaned_data["task"]

            # Adicione a nova tarefa à nossa lista de tarefas

            tasks.append(task)

            # Redirect user to list of tasks

            return HttpResponseRedirect(reverse("index_tasks"))

        else:

            # Se o formulário for inválido, renderize novamente a página com as informações existentes

            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
