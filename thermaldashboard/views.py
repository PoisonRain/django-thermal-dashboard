from django import forms
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from axes.utils import reset
from captcha.fields import CaptchaField
from easy_timezones.utils import get_ip_address_from_request

class AxesCaptchaForm(forms.Form):
			captcha = CaptchaField()

def locked_out(request):
		if request.POST:
				form = AxesCaptchaForm(request.POST)
				if form.is_valid():
						ip = get_ip_address_from_request(request)
						reset(ip=ip)
						return HttpResponseRedirect("/")
		else:
				form = AxesCaptchaForm()
		return render_to_response('chat/locked_out.html', dict(form=form), context_instance=RequestContext(request))
