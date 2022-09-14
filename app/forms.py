from email.mime import image
from django import forms
from .models import Item

PLACES = (
    (1, '和食'),
    (2, '中華'),
    (3, '洋食'),
    (4, 'ジャンク'),
    (5, 'おやつ'),
    (6, 'その他'),
)

class ItemForm(forms.Form):
    item = forms.CharField(max_length=30, label='料理名')
    place = forms.fields.ChoiceField(
        label='ジャンル',
        choices = PLACES,
        required=True,
        widget=forms.widgets.Select
    )
    memo = forms.CharField(label='メモ', widget=forms.Textarea(), required=False)
    image = forms.ImageField(label= '写真')
