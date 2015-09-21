from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from anicard.models import MembershipCard, CardRequest
from anicard.forms import CardReqForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def memberCardView(request):
    card = getCurrentCard()
    if not card:
        return render_to_response('anicard/no-card.html',
            context_instance=RequestContext(request))
    else:
        status = getUsersCard(request.user)
        return render_to_response('anicard/card.html', {'card': card, 'status': status},
            context_instance=RequestContext(request))


def getCurrentCard():
    now = timezone.now()
    options = MembershipCard.objects.filter(open=True, year_start__lte=now, year_end__gte=now)
    if len(options) < 1:
        return None
    else:
        return options[0]

def getUsersCard(usr):
    if usr.is_anonymous():
        return None
    now = timezone.now()
    options = CardRequest.objects.filter(user=usr, year__year_start__lte=now, year__year_end__gte=now)
    if len(options) < 1:
        return None
    else:
        return options.last()

@login_required
def cardrequest(request):
    if getUsersCard(request.user):
        return HttpResponseRedirect('/card/status/')
    card = getCurrentCard()
    if not card:
        return render_to_response('anicard/no-card.html',
            context_instance=RequestContext(request))
    if request.method == 'POST':
        form = CardReqForm(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            req = CardRequest(user=request.user, year=card)
            req.save()
            return HttpResponseRedirect('/card/status/')
        else:
            messages.add_message(request, messages.ERROR, 'Registration error')
            return render_to_response('anicard/request.html', {'form': form},
                context_instance=RequestContext(request))
    else:
        data = {'first_name': request.user.first_name, 'last_name': request.user.last_name}
        form = CardReqForm(data)
        return render_to_response('anicard/request.html', {'form': form},
            context_instance=RequestContext(request))

@login_required
def cardStatus(request):
    card = getUsersCard(request.user)
    if not card:
        return HttpResponseRedirect('/card/request/')
    return render_to_response('anicard/status.html', {'card': card},
            context_instance=RequestContext(request))
