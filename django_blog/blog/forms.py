from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags separated by commas (e.g., technology, python, web-development)'
        }),
        label='Tags',
        help_text='Separate tags with commas. Tags will be created if they don\'t exist.'
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Populate tags_input field with existing tags
            existing_tags = ', '.join([tag.name for tag in self.instance.tags.all()])
            self.fields['tags_input'].initial = existing_tags
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('Content must be at least 10 characters long.')
        return content
    
    def clean_tags_input(self):
        tags_input = self.cleaned_data.get('tags_input', '')
        if tags_input:
            # Validate tag names
            tag_names = [tag.strip().lower() for tag in tags_input.split(',') if tag.strip()]
            for tag_name in tag_names:
                if len(tag_name) > 50:
                    raise forms.ValidationError(f'Tag "{tag_name}" is too long. Maximum 50 characters.')
                if not tag_name.replace('-', '').replace('_', '').isalnum():
                    raise forms.ValidationError(f'Tag "{tag_name}" contains invalid characters. Use only letters, numbers, hyphens, and underscores.')
        return tags_input
    
    def save(self, commit=True):
        post = super().save(commit=commit)
        if commit:
            # Handle tags
            tags_input = self.cleaned_data.get('tags_input', '')
            if tags_input:
                tag_names = [tag.strip().lower() for tag in tags_input.split(',') if tag.strip()]
                tags = []
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    tags.append(tag)
                post.tags.set(tags)
            else:
                post.tags.clear()
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...',
                'maxlength': 1000
            })
        }
        labels = {
            'content': 'Your Comment'
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) < 3:
            raise forms.ValidationError('Comment must be at least 3 characters long.')
        if len(content) > 1000:
            raise forms.ValidationError('Comment cannot exceed 1000 characters.')
        return content.strip()

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search posts by title, content, or tags...',
            'autocomplete': 'off'
        }),
        label='Search'
    )