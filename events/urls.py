from django.conf.urls import url

from . import views

app_name = "events"
urlpatterns = [
    url(r'^home/$', views.EventListView.as_view(), name="home"),
    url(r'^create/$', views.CreateEventView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)$', views.UpdateEventView.as_view(), name="update"),
    url(r'^details/(?P<pk>\d+)$', views.DetialsEventView.as_view(), name="details"),
    # url(r'^add/$', views.CreateExpenseView.as_view(), name="create"),
]