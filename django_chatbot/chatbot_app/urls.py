from chatbot_app import views
from django.urls import path

import chatbot_app

urlpatterns = [
    path('',views.home,name="home"),
    path('predict',views.predict,name="predict") 
]



