from channels.consumer import AsyncConsumer
from  channels.exceptions import StopConsumer

class EchoComsumer(AsyncConsumer):

    async def websocket_connect(self, event):  
        await self.send({
            'type' : 'websocket.accept'
        })

    async def websocket_disconnect(self,event):
        raise StopConsumer()

    async def websocket_receive(self, event):
        await self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })

class ChatConsomer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            'type' : "websocket.accept"
        })

        # print(self.scope["user"])
        # print(self.scope['url_route']['kwargs']["chat_id"])



    async def websocket_disconnect(self,event):
        raise StopConsumer()

    async def websocket_receive(self, event):
        await self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })

    