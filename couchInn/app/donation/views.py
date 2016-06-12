from datetime import date

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .forms import DonationForm
from .models import Donation

# Create your views here.
@login_required
def donate(request):
    donation_form = DonationForm(request.POST or None)
    if request.method == 'POST':
        if donation_form.is_valid():
            donation = donation_form.save(commit=False)
            donation.donation_date = date.today()
            donation.user = request.user
            donation.save()
            couchin_profile = request.user.couchinnuser
            couchin_profile.premium = True
            couchin_profile.total_donations += donation.amount
            couchin_profile.save()
            return HttpResponseRedirect(reverse('donation:index'))
    return render(request, 'donation/new.html', {'donation_form' : donation_form})

@login_required
def donation_index(request):
    donations = Donation.objects.all().filter(user=request.user)
    return render(request, 'donation/index.html',{'donations' : donations})
