from dal import autocomplete
from django.views.generic.list import ListView

from import_export import mixins

from . import models


class CategoryExportView(mixins.ExportViewFormMixin, ListView):
    model = models.Category


class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return models.Author.objects.none()

        qs = models.Author.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
