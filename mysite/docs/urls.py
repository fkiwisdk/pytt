from django.urls import path

from . import views

app_name = 'docs'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:ppk_id>/', views.detail, name='detail'),
    # ex: /docs/5/results/
    #path('<int:pk_id>/results/', views.results, name='results'),
    # ex: /docs/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]