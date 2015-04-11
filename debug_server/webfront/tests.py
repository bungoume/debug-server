import json
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndex(TestCase):
    def _getTargetURL(self, *args, **kwargs):
        return reverse('index', args=args, kwargs=kwargs)

    def test_it(self):
        res = self.client.get(self._getTargetURL(), {
            'param1': 'test_param'})
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.content.decode())
        self.assertEqual(res_data['get']['param1'], ['test_param'])

    def test_non_utf8_body(self):
        body = "foo".encode('utf-16')
        res = self.client.post(self._getTargetURL(), body, content_type="text/plain")
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.content.decode())
        self.assertEqual(res_data['body'], None)
        self.assertNotIn('body_json', res_data)

    def test_json_body(self):
        body = json.dumps({'data': 'sample'})
        res = self.client.post(self._getTargetURL(), body, content_type="application/json")
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.content.decode())
        self.assertEqual(res_data['body_json']['data'], 'sample')
