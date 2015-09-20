from django.shortcuts import render
from django.views.generic import ListView, DetailView
from anicard.models import MembershipCard, CardRequest
from anicard.forms import CardReqForm
from django.utils import timezone

# Create your views here.

def memberCardView(request):
    card = getCurrentCard()
    if not card:
        return render_to_response('anicard/no-card.html',
            context_instance=RequestContext(request))
    else:
        return render_to_response('anicard/card.html', {'card': card},
            context_instance=RequestContext(request))


def getCurrentCard():
    now = timezone.now()
    options = MembershipCard.objects.filter(open=True, year_start__lte=now, year_start__gte=now)
    if options.count < 1:
        return None
    else:
        return options[0]


def cardrequest(request):
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
            return HttpResponseRedirect('/card/thanks/')
        else:
            messages.add_message(request, messages.ERROR, 'Registration error')
            return render_to_response('anicard/request.html', {'form': form},
                context_instance=RequestContext(request))
    else:
        data = {'first_name': request.user.first_name, 'last_name': request.user.last_name}
        form = CardReqForm(data)
        return render_to_response('anicard/request.html', {'form': form},
            context_instance=RequestContext(request))
