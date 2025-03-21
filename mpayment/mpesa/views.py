import logging
import json

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MpesaCheckoutSerializer
from .util import MpesaGateWay

gateway = MpesaGateWay()

@authentication_classes([])
@permission_classes((AllowAny,))
class MpesaCheckout(APIView):
    """Checkout serializer class function"""
    serializer = MpesaCheckoutSerializer

    def post(self, request, *args, **kwargs):
        """post function"""
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            payload = {"data":serializer.validated_data, "request":request}
            res = gateway.stk_push_request(payload)
            return Response(res, status=200)

@authentication_classes([])
@permission_classes((AllowAny,))
class MpesaCallBack(APIView):
    """Callback function"""
    def get(self, request):
        """get method"""
        return Response({"status": "OK"}, status=200)

    def post(self, request, *args, **kwargs):
        """post method"""
        logging.info("{}".format("Callback from MPESA"))
        data = request.body
        return gateway.callback(json.loads(data))
