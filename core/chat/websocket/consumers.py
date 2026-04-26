from channels.consumer import AsyncConsumer
from  channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
import json
from ..models import Chat, Message

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

        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.user = self.scope["user"]
        self.chat = await self.get_chat()
        self.checked_user = await self.check_user()

        if self.chat and self.checked_user :

            self.group_id  = f"chat_{self.chat_id}"

            await self.channel_layer.group_add(self.group_id,self.channel_name)

            await self.send({
                'type' : "websocket.accept"
            })

        # print(self.scope["user"])
        # print(self.scope['url_route']['kwargs']["chat_id"])



    async def websocket_disconnect(self,event):
        try:

            await self.channel_layer.group_discard(self.group_id,self.channel_name)
        except:
            pass 

        raise StopConsumer()

    async def websocket_receive(self, event):

        message_text = event.get("text")

        message = await self.create_message(message_text, "Message")

       
        await self.channel_layer.group_send(self.group_id,{
            "type" : "send_message",
            "message" : json.dumps( {"text": message_text, "sender" : self.user.get_username(), "message_id":message.id,"sended_at": message.sended_date.strftime("%H : %M")}),
            "channel_name" : self.channel_name
        })

        # await self.send({
        #     'type' : 'websocket.send',
        #     'text' : event['text']
        # })

    @database_sync_to_async
    def get_chat(self):
        return Chat.objects.filter(chat_id=self.chat_id).first()
    
    @database_sync_to_async
    def check_user(self):
        return self.chat.members.filter(user = self.user).first()
    
    @database_sync_to_async
    def create_message(self,text,message_type):
        message = Message.objects.create(chat= self.chat, sender = self.user, text = text, message_type = message_type)
        return message

    async def send_message(self, event):

        channel_name = event.get("channel_name")

        if not channel_name or self.channel_name != channel_name:
            await self.send({
                "type" : "websocket.send",
                "text" :event.get("message")
            })
    


    