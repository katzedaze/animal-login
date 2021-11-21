from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.classify, name='classify'),
]

# mediaディレクトリの画像表示のため
# 画像はlocalなStorageのMEDIA_ROOTに保存され、localなurl(相対url)のMEDIA_URLで参照
# if settings.DEBUG: で分岐させることも多い
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
