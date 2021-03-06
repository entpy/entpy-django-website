from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.http import Http404
#from django.http import HttpResponse

class StaticView(TemplateView):
	def get(self, request, page, *args, **kwargs):
		self.template_name = page + '.html'
		response = super(StaticView, self).get(request, *args, **kwargs)
		# to highlight the active menu
		response.context_data = {"active_item": page + "_menu_item_active"}
		try:
			return response.render()
		except TemplateDoesNotExist:
			# return HttpResponse("Template non trovato " + self.template_name)
			raise Http404
