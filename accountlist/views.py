from django.shortcuts import render

from .models import Accountlist

# Create your views here.
def index(request):
    account_items = Accountlist.objects.order_by('id')
    context = {'account_items' : account_items}
    return render(request, 'accountlist/index.html', context)