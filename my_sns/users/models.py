from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from posts.models import Post


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    image = ImageField(_("Image of User"), upload_to="image/", default="none/default_profile.jpg")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def posts(self):
        return Post.objects.filter(user=self)
