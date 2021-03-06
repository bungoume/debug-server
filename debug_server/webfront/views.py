import json
import logging
import os
import uuid
from django.utils import timezone
from django.http import JsonResponse


logger = logging.getLogger(__name__)


def index(request):
    meta = {}
    # bodyはrequest.POSTより先に読み出す必要がある

    try:
        body = request.body.decode('utf-8')
    except UnicodeDecodeError as e:
        logger.warn('faild to load body as utf-8. %s', e)
        body = None

    for k, v in request.META.items():
        if k.startswith(('SERVER_', 'HTTP_', 'REMOTE_')):
            meta[k.lower()] = v

    res = {
        'hostname': os.getenv('HOSTNAME'),
        'appname': os.getenv('APPNAME'),
        'uuid': str(uuid.uuid4()),
        'datetime': timezone.localtime(timezone.now()).isoformat(),
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
    except (TypeError, ValueError) as e:
        logger.debug('faild to load as json. %s', e)
        pass

    return JsonResponse(res)


def handler400(request):
    res = JsonResponse({'error': {'code': 'bad_request',
                                  'message': "400 Bad Request"}}, status=400)
    return res


def handler403(request):
    res = JsonResponse({'error': {'code': 'permission_denied',
                                  'message': "403 Permission Denied"}}, status=403)
    return res


def handler404(request):
    res = JsonResponse({'error': {'code': 'not_found',
                                  'message': "404 Not Found"}}, status=404)
    return res


def handler500(request):
    res = JsonResponse({'error': {'code': 'server_error',
                                  'message': "500 Internal Server Error"}}, status=500)
    return res
