from django.test import SimpleTestCase
from django.urls import reverse
from ... import helper
import requests, os



class TestApi(
    SimpleTestCase, helper.TestAPIHelper, helper.NoVersion, helper.InvalidVersion, helper.NotAuthenticated
):
    def setUp(self) -> None:
        self._setUp(
            Production=True,
            API_Name='User Urls',
            URL=reverse('Url.api:Urls'),
            Host=os.environ.get('HOST')
        )
        self._Authorize()

    def test_urls(self):

        _response = requests.get(self._url, headers={
            'Version': 'V1',
            'Authorization': 'Bearer {0}'.format(self._Token)
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 200, self._Message('Get Urls'))
