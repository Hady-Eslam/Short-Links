from django.views.generic import ListView, CreateView, UpdateView, RedirectView
from django.http import Http404, HttpRequest, JsonResponse
from django.urls import reverse
from Apps.Auth.mixins import LoginRequiredMixin, SuccessMessageMixin
from Apps.Profile.mixins import ProfileMixin
from .helper import Random
from .models import Url



class UrlsView(LoginRequiredMixin, ProfileMixin, ListView):
    def get_queryset(self):
        return Url.objects.filter(user=self.request.user, is_deleted=False).order_by('-id')


class CreateUrlView(LoginRequiredMixin, ProfileMixin, SuccessMessageMixin, CreateView):

    success_flash_message_name = 'success_create_url'
    success_flash_message = 'Your Link Created Successfully'

    model = Url
    fields = ['title', 'description', 'url']

    def get_success_url(self):
        return reverse('Url:Url', kwargs={'Url_id': self.object.id})

    def form_valid(self, form):
        _Count = Url.objects.count()
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.short_url = Random.create_random_token(_Count + 1, _Count + 3)
        self.object.save()
        return super().form_valid(form)


class UrlView(LoginRequiredMixin, ProfileMixin, SuccessMessageMixin, UpdateView):

    success_flash_message_name = 'success_edit_url'
    success_flash_message = 'Your Link Edited Successfully'

    model = Url
    fields = ['title', 'description', 'url']

    def get_success_url(self):
        return reverse('Url:Url', kwargs={'Url_id': self.object.id})

    def get_object(self, queryset=None):
        self._url = Url.objects.filter(id=self.kwargs['Url_id'], user=self.request.user, is_deleted=False).first()
        if self._url is None: raise Http404('URL Not Found Or Not URL Creator')
        self._url.updated_short_url = self.request.build_absolute_uri(
            reverse('Url:Redirect', kwargs={'Short_Url': self._url.short_url})
        )
        return self._url
    
    def delete(self, request: HttpRequest, Url_id: str):
        _Url = Url.objects.filter(id=self.kwargs['Url_id'], user=self.request.user, is_deleted=False).first()
        _Url.is_deleted = True
        _Url.save()
        return JsonResponse({'Result': 'Done'})


class RedirectUrlView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        _Url = Url.objects.filter(short_url=kwargs['Short_Url'], is_deleted=False).first()
        if _Url is None: raise Http404('Link Does Not Exists')
        return _Url.url
