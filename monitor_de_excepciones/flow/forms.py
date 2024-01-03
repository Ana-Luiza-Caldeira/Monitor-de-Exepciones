from django import forms
from .models import Flow, Notification

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['id_processo', 'module', 'organization', 'description', 'state']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['flow', 'id_transacao', 'tipo', 'state', 'reprocessavel', 'gerenciavel']
