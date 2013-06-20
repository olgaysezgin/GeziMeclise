from django.conf.urls import patterns, url
from gezimeclise.profiles.views import ProfileListView, ProfileDetailView, \
                                       ProfileUpdateView, ProfileSupport

urlpatterns = patterns('',
    url(r'^$', ProfileListView.as_view(), name="profile_list"),
    url(r'^update/$', ProfileUpdateView.as_view(), name="profile_update"),

    url(r'^support/$', ProfileSupport.as_view(), name="profile_support"),

    url(r'^(?P<username>[-\w]+)/$', ProfileDetailView.as_view(), name="profile_detail"),
)
