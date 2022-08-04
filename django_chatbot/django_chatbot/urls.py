from chatbot_app import views
from django.contrib import admin
from django.urls import path, include

import chatbot_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chatbot_app.urls')),
]
