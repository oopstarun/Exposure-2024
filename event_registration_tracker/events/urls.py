from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login/event_list/', views.event_list, name='event_list'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
    path('feedback/<int:event_id>/', views.event_feedback, name='event_feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
