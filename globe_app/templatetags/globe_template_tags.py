from django import template
from globe_app.models import Message

# From Legion Script on YT

register = template.Library()

# @register.inclusion_tag('globe_templates/notifications.html', takes_context=True)
# def show_notification(context):
#     request_user = context['request'].user
#     notifications = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
#     return {'notifications': notifications}


@register.filter
def get_notification_count(userID):
    print('test1')
    # notificationss = Notification.objects.filter(to_user=userID).exclude(user_has_seen=True)
    unread_messages = Message.objects.filter(messageReceiver=userID).exclude(messageRead=True)
    print(unread_messages)
    # print(notifications)
    return len(unread_messages)

