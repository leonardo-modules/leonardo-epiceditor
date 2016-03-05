
from django.http import JsonResponse
from django.views import generic

from .utils import DEFAULT_MARKUP_TYPES


class EpicEditorView(generic.TemplateView):

    def post(self, *args, **kwargs):

        if 'text' in self.request.POST:

            if 'type' in self.request.POST:

                for type in DEFAULT_MARKUP_TYPES:
                    if type[0] == self.request.POST['type']:
                        text = type[1](self.request.POST['text'])

            else:
                text = self.request.POST['text']

            return JsonResponse(
                {'text': text})

        raise Exception
