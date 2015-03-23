import json
import logging
import os
import uuid
import pytz
from datetime import datetime

from django.http import JsonResponse


jst = pytz.timezone('Asia/Tokyo')
logger = logging.getLogger(__name__)


def index(request):
    meta = {}
    # bodyはrequest.POSTより先に読み出す必要がある

    try:
        body = request.body.decode('utf-8')
    except UnicodeDecodeError as e:
        logger.warn('faild to load body as utf-8. %s', e)
        body = json.loads(request.body.decode('utf-8', 'replace'))

    for k, v in request.META.items():
        if k.startswith(('SERVER_', 'HTTP_', 'REMOTE_')):
            meta[k.lower()] = v

    res = {
        'hostname': os.getenv('HOSTNAME'),
        'appname': os.getenv('APPNAME'),
        'uuid': str(uuid.uuid4()),
        'datetime': datetime.now(jst).isoformat(),
        'get': dict(request.GET),
        'post': dict(request.POST),
        'body': body,
        'cookies': dict(request.COOKIES),
        'path': request.path,
        'meta': meta,
        'encoding': request.encoding,
        'method': request.method,
    }

    # POST bodyがjsonであればシリアライズ結果も返す
    try:
        body_json = json.loads(body)
        res['body_json'] = body_json
    except:
        pass

    return JsonResponse(res)
