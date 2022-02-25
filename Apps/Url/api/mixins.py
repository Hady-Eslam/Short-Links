from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .versioning import Versioning
from .throttles import UrlThrottleClass


class BaseUrlAPI:
    permission_classes = [IsAuthenticated]
    throttle_classes = [UrlThrottleClass]
    renderer_classes = [JSONRenderer]
    versioning_class = Versioning
