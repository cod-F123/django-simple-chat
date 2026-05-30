from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import Chat

User = get_user_model()

class ChatForm(forms.ModelForm):

    title = forms.CharField(required=True)

    def clean(self):
        validated_data =  super().clean()

        if validated_data.get("chat_type") == "Private":
            self.add_error("chat_type", "chat type must be Channel or Group")



    class Meta:
        model = Chat
        fields = ["title", "chat_type"]

class CreateContactChatForm(forms.ModelForm):
    
    contact = forms.CharField(max_length=255, required=True)

    def clean(self):
        cleaned_data =  super().clean()

        owner = self.initial.get("owner")

        try:
            contact_user= User.objects.get(username = cleaned_data.get("contact"))
            cleaned_data["contact"] = contact_user
        
        except User.DoesNotExist:
            raise forms.ValidationError("user not found")

        existing_chat = Chat.objects.filter(
            chat_type='Private',
            members__user__in=[owner, contact_user]
        ).annotate(
            num_members=Count('members')
        ).filter(
            num_members=2
        )
        
        
        if existing_chat:
            raise forms.ValidationError("You have already had a private chat with this user.")
        
        return cleaned_data

    class Meta:
        model = Chat
        fields = ["contact"]
        
