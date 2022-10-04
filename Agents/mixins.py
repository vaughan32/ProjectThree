from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrgarnizerCheckLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an orgarnizer."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_orgarnizer:
            return redirect('lead_list')
        return super(OrgarnizerCheckLoginRequiredMixin,self).dispatch(request, *args, **kwargs)