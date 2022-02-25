from django.test import SimpleTestCase
from django.urls import reverse
from ... import helper
import requests, os



class TestApi(
    SimpleTestCase, helper.TestAPIHelper, helper.NoVersion, helper.InvalidVersion, helper.NotAuthenticated,
    helper.PostInvalidData
):
    def setUp(self) -> None:
        self._setUp(
            Production=True,
            API_Name='Create Url',
            URL=reverse('Url.api:Urls'),
            Host=os.environ.get('HOST')
        )
        self._Authorize()


    def test_create_url(self):

        _response = requests.post(self._url, headers={
            'Version': 'V1',
            'Authorization': 'Bearer {0}'.format(self._Token)
        }, data={
            'title': 'Test API Url',
            'description': 'Test API Url Description',
            'url': 'https://www.youtube.com/watch?v=Z1RJmh_OqeA'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 201, self._Message('Creating Url'))
