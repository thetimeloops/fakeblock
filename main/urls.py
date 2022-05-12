from django.urls import path
from . import views
urlpatterns = [
    path('',views.workflow,name="workflow"),
    path('check/<str:slug>',views.check,name="check"),
    path('invoice',views.index,name="index"),
    path('blockchains',views.blockchains,name="blockchains")
]
