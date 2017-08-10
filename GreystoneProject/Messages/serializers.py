from rest_framework import serializers

import models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ('id', 'message_text')