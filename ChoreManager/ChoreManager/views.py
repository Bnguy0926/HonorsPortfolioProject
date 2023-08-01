from django.shortcuts import render
from .models import User, ChoreList, Chore


def index_view(request):
    return render(request, 'index.html')

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def chore_list_view(request):
    chore_lists = ChoreList.objects.all()
    return render(request, 'chore_list.html', {'chore_lists': chore_lists})

def chore_list_detail_view(request, list_id):
    chore_list = ChoreList.objects.get(pk=list_id)
    return render(request, 'chore_list_detail.html', {'chore_list': chore_list})

def chore_view(request):
    chores = Chore.objects.all()
    return render(request, 'chore.html', {'chores': chores})

def chore_detail_view(request, chore_id):
    chore = Chore.objects.get(pk=chore_id)
    return render(request, 'chore_detail.html', {'chore': chore})