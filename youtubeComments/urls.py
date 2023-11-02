from django.urls import path , include
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('refresh/',views.refresh,name='refresh'),
        path('summarize/',views.summarize,name='summarize'),
        path('clssummarize/',views.clssummarize,name='clssummarize'),


]
