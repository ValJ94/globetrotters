from django import forms
from forum_app.models import ForumPost, PostReply


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('title', 'content',)

        labels = {
            'title': '',
            'content': '',
        }
    
        widgets = {
                    'title': forms.TextInput(attrs={'class':'form-control, col-xs-2', 
                                                        'placeholder': 'Title', 
                                                        'id': 'post_title'}), # form-control is bootstrap
                    'content': forms.Textarea(attrs={'class':'form-control, col-xs-3', 
                                                        'placeholder': 'Write your post here', 
                                                        'id': 'post_content'}),
                }


class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply

        fields = ('content',)

        labels = {
            'content': '',
        }
    
        widgets = {
                    'content': forms.Textarea(attrs={'class':'form-control, col-xs-3', 
                                                        'placeholder': 'Write comment', 
                                                        'id': 'post_reply'}),
                }