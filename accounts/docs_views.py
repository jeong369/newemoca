# swagger
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


# swagger schema
schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="여기는 EmoCA DB 활용 페이지입니다.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ij_cho@kaist.ac.kr"),
      license=openapi.License(name="emoca"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)