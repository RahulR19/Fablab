from django.urls import path
from . import views

urlpatterns = [path(r"R.html",views.reserve, name='Reserve'),path(r"FL.html", views.index,name="Homepage"),path(r"", views.index,name=""),path(r"C.html",views.cancel, name='Cancel'),path(r"A.html",views.about, name='About'),
path(r"I.html",views.items, name='I'),path(r"I1.html",views.itemsuccess, name='Itemsuccess'),path(r"C2.html",views.cancelsuccess, name='Cancelsuccess')]
