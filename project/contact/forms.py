from django import forms

class contactForm(forms.Form): #new form called contactForm
 	Username = forms.CharField(required=True,max_length=50,help_text='limit 50 chars')
	UserEmail = forms.EmailField(required=True)
	Message = forms.CharField(required=True,widget=forms.Textarea)
	#This widget overrides the defualt widdget defult in CharField. See Dj Docs.
