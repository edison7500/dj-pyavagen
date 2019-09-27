import pyavagen
from io import BytesIO
from django.views import generic
from django.http import HttpResponse


class AvatarGenerateView(generic.View):
    http_method_names = ["get"]

    def generate_avatar(self, request, *args, **kwargs):
        _size = self.kwargs.pop("size")
        _name = self.kwargs.pop("name")
        avatar = pyavagen.Avatar(
            pyavagen.CHAR_SQUARE_AVATAR,
            size=int(_size), string=_name,
            squares_on_axis=10,
            rotate=10,
            font_outline=True,
            blur_radius=4, color_list=pyavagen.COLOR_LIST_MATERIAL
        )
        f = BytesIO()
        avatar.generate().save(f, format="JPEG")
        return f.getvalue()

    def get(self, request, *args, **kwargs):
        content = self.generate_avatar(request, *args, **kwargs)
        return HttpResponse(content=content, content_type="image/jpeg")
