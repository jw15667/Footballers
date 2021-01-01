from django import forms

class SearchPlayersForm(forms.Form):
    player1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'input id': 'inputPlayer1',
            'class': 'form-control',
            'placeholder': 'Player 1',
        }
    ))
    player2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'input id': 'inputPlayer2',
            'class': 'form-control',
            'placeholder': 'Player 2',
        }
    ))