import os
import uuid
import pytz
from datetime import datetime

from django.http import JsonResponse


jst = pytz.timezone('Asia/Tokyo')


def index(request):
    meta = {}

    for k, v in request.META.items():
        if k.startswith(('SERVER_', 'HTTP_', 'REMOTE_')):
            meta[k.lower()] = v
    res = {
        'hostname': os.getenv('HOSTNAME'),
        'uuid': str(uuid.uuid4()),
        'datetime': datetime.now(jst).isoformat(),
        'get': dict(request.GET),
        'post': dict(request.POST),
        'cookies': dict(request.COOKIES),
        'path': request.path,
        'meta': meta,
        'encoding': request.encoding,
        'method': request.method,
    }
    return JsonResponse(res)
