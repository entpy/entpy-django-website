from django.conf.urls import patterns, include, url
#from django.conf import settings
#from django.conf.urls.static import static
from views import StaticView

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'website.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^(?P<page>[^/\.]+).*$', StaticView.as_view()),
)# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
