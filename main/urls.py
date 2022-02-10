from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contests/detail/<slug:slug>', views.contest_detail_view, name='contest_detail'),
    path('events/detail/<slug:slug>', views.event_detail_view, name='event_detail'),
    path('contact/new/', views.contact_add_view, name='contact'),
    path('contest/register/', views.contest_register_view, name='contest_register'),
    path('contest/question/', views.contest_question_view, name='contest_question'),
    path('event/register/', views.event_register_view, name='event_register'),
    path('event/question/', views.event_question_view, name='event_question'),
]
