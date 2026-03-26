import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.room_group_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'order_id': event.get('order_id'),
            'product_name': event.get('product_name'),
            'buyer_name': event.get('buyer_name'),
        }))

@database_sync_to_async
def create_order_notification(order):
    """Envoyer une notification au farmer lorsqu'une commande est passée"""
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    
    channel_layer = get_channel_layer()
    
    # Notifier le farmer
    async_to_sync(channel_layer.group_send)(
        f"user_{order.product.farmer.id}",
        {
            'type': 'send_notification',
            'message': f'🛒 Nouvelle commande reçue !',
            'order_id': order.id,
            'product_name': order.product.name,
            'buyer_name': order.buyer.username,
        }
    )
