from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
	'''checkout view function'''
	publishkey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.stripeuser.stripe_id
	if request.method == 'POST':
		print request.POST['stripeToken']
		token = request.POST['stripeToken']
		print request.POST
		#Charge usercard and charge 
		try:
			#create a card stripe docs
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)

			charge = stripe.Charge.create(
			  amount=1000,
			  currency="usd",
			  description="Example charge",
			  customer = customer,
			  
			) 
		except stripe.error.CardError as e:
			print 'The Card has been declined'
			pass
	context = {'publishKey':publishkey }
	template = 'checkout.html'
	return render(request,template,context)
