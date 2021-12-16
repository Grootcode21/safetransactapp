from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('add', views.addAccount, name='add' ),
    path('outdated/<account_id>', views.outdatedAccount, name='outdated' ),
    path('deleteoutdated', views.deleteOutdated, name='deleteoutdated' )
]