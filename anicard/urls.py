from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'anicard.views.memberCardView', name="card_view"),
    url(r'^request/$', 'anicard.views.cardrequest', name="card_request"),
    url(r'^status/$', 'anicard.views.cardStatus', name="card_status"),
)
