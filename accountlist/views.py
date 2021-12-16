from django.shortcuts import render, redirect 

from .models import Accountlist

from .forms import AccountListForm

from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    account_items = Accountlist.objects.order_by('id')
    form = AccountListForm()
    context = {'account_items' : account_items, 'form': form}
    return render(request, 'accountlist/index.html', context)

@require_POST
def addAccount(request):
    form = AccountListForm(request.POST)

    if form.is_valid():
        new_account = Accountlist(text=request.POST['text'])
        new_account.save()

    return redirect('index')

def outdatedAccount(request, account_id):
    account = Accountlist.objects.get(pk= account_id)
    account.outdated = True
    account.save()

    return redirect('index')

def deleteOutdated(request):
    Accountlist.objects.filter(outdated_exact= True).delete()

    return redirect('index')