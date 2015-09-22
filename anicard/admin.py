from django.contrib import admin
from anicard.models import CardRequest, MembershipCard
# Register your models here.

@admin.register(CardRequest)
class CardRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'year', 'paid', 'printed', 'delivered', 'lost')
    list_filter = ('year', 'paid', 'printed', 'lost')
    fields = ('user', 'name', 'year', ('paid', 'printed', 'delivered'), 'lost')
    readonly_fields = ('year', 'name')
    
    def name(self, instance):
        return instance.user.get_full_name()


@admin.register(MembershipCard)
class MembershipCardAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'year_end', 'open')
    list_filter = ('open',)
    fields = ('design', ('year_start', 'year_end'), 'open')
