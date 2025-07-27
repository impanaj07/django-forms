from django import forms
class ReviewForm(forms.Form):
    user_name=forms.CharField(max_length=100, label='Your Name',error_messages={
        'required': 'Please enter your name.',
        'max_length': 'Name cannot exceed 100 characters.'
    })
    review_text=forms.CharField(widget=forms.Textarea, label='Your Review')
    rating=forms.IntegerField(min_value=1, max_value=5, label='Rating (1-5)', error_messages={
        'min_value': 'Rating must be at least 1.',      
        'max_value': 'Rating cannot exceed 5.'
    })
