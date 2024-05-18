from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import Message
class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #extracting room_name from url which gets placed to self.room_name
        self.room_name = self.scope['url_route']['kwargs']['room_name'] 

        self.room_group_name = 'chat_%s' % self.room_name 

        #constructing a group, using group allows us to brodcast message to all user in group.
        await self.channel_layer.group_add( 
            self.room_group_name,
            self.channel_name 
        )

        #Accepting a websocket connection.
        await self.accept()

    #when websocket connection is closed this method removes current channel from room group.
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)      
        image_data = data['image']
        username = data['username']
        room = data['room']
        message_length = data['message_length']
       
      
        await self.save_message(username, room, image_data, message_length)

        # Send message to room group after saving in database so it can be broadcasted to all users.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'image': image_data,
                'username': username,
                'message_length':message_length

            }
        )

    #Receive message from room group, it then extracts the message and username from event data.
    async def chat_message(self, event):
        image_data = event['image']
        username = event['username']
        message_length = event['message_length']

        #Send message to WebSocket to be displayed to the user.
        await self.send(text_data=json.dumps({
            'image': image_data,
            'username': username,
            'message_length':message_length

        }))

    @sync_to_async
    def save_message(self, username, room, data,message_length):
        Message.objects.create(user=username, room=room, content=data,length=message_length)
