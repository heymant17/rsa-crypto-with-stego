from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/<str:room_name>', consumers.ChatRoomConsumer.as_asgi()), 
]#just like urls.py upon getting a correct url it runs the code inside of chatroomconsumer 
 #which is inside of consumers.py(consider this as views.py).