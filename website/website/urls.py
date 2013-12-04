from django.conf.urls import patterns, include, url
from views import StaticView

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'website.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^(?P<page>[^/\.]+).*$', StaticView.as_view()),
)
