from django.conf.urls import patterns, url, include
from thinkster_django_angular_boilerplate.views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from authentication.views import LoginView
from authentication.views import LogoutView
from posts.views import AccountPostViewSet, PostViewSet

# Config routers

router = routers.DefaultRouter()

router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router,
    r'accounts',
    lookup='account'
)

accounts_router.register(r'posts', AccountPostViewSet)

urlpatterns = patterns(
    '',

    # API
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),

    # URLs
    url('^.*$', IndexView.as_view(), name='index'),
)