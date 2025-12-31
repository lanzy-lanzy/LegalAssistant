from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze, name='analyze'),
    path('analyze/<int:doc_id>/', views.analyze_doc, name='analyze_doc'),
    path('clauses/', views.clauses, name='clauses'),
]


