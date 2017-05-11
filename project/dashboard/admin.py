from django.contrib import admin

# Register your models here.
from .models import dashboard, stripeUser
class dashboardAdmin(admin.ModelAdmin):
	class Meta:
		model = dashboard
admin.site.register(dashboard,dashboardAdmin)

class stripeUserAdmin(admin.ModelAdmin):
	class Meta:
		model = stripeUser
 
admin.site.register(stripeUser,stripeUserAdmin)
