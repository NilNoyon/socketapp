import json
from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
     def connect(self):
          self.accept()
          self.send(text_data=json.dumps({
               'message': 'GeeksforGeeks websocket'
          }))

     def disconnect(self, close_code):
          pass

     def receive(self, text_data):
          pass
    
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          await self.accept()
     async def disconnect(self, close_code):
          pass
     async def receive(self, text_data):
          text_data_json = json.loads(text_data)
          message = text_data_json['message']
          await self.send(text_data=json.dumps({
               'message': message
          }))