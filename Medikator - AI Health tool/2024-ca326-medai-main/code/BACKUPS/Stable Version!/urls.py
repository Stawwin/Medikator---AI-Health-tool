from django.urls import path
from . import views
from .views import process_user_input, display_user_inputs

urlpatterns = [
    # Define your app-specific URL patterns here
    # For example, if you have a view called 'chat_view', you can include a URL pattern like this:
    path('chat/', views.chat_view, name='chat_view'),
    path('process/', process_user_input, name='process_user_input'),
    path('display/', display_user_inputs, name='display_user_inputs'),
]
