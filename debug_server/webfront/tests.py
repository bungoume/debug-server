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
