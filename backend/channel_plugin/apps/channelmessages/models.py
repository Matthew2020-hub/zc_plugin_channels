from dataclasses import dataclass, field

from django.utils import timezone

from channel_plugin.utils.customrequest import Request

MESSAGE_TYPES = ["message", "event"]
DEFAULT_MESSAGE_TYPE = "message"

# Create your models here.


@dataclass
class ChannelMessage:
    user_id: str
    channel_id: str
    content: str
    # list of thread emojis
    emojis: list = field(default_factory=list)
    pinned: bool = False
    edited: bool = False
    can_reply: bool = True
    type: str = DEFAULT_MESSAGE_TYPE
    timestamp: str = timezone.now().isoformat()

    def create(self, organization_id):
        payload = {
            "user_id": self.user_id,
            "channel_id": self.channel_id,
            "content": self.content,
            "emojis": self.emojis,
            "pinned": self.pinned,
            "edited": self.edited,
            "type": self.type,
            "can_reply": self.can_reply,
            "timestamp": self.timestamp,
        }
        response = Request.post(
            organization_id, self.__class__.__name__.lower(), payload
        )
        return response

    def __str__(self):
        return self.content
