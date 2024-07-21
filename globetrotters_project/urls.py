
from django.contrib import admin
from django.urls import path, include, reverse
from globe_app import views as globe_views
from forum_app import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class Registration(RegistrationView):
    def get_success_url(self, user):
        return reverse('globe_app:register_contd')
        # return reverse('user_app:register_contd')


urlpatterns = [
    path('', globe_views.index, name='index'),
    path('globetrotters/', include('globe_app.urls')),
    path('forum/', include('forum_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', Registration.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
