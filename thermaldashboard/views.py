from django import forms
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from captcha.fields import CaptchaField
from easy_timezones.utils import get_ip_address_from_request
