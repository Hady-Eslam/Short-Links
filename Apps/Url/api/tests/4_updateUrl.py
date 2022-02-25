from django.test import SimpleTestCase
from django.urls import reverse
from ... import helper
import requests, os



class TestApi(
    SimpleTestCase, helper.TestAPIHelper, helper.NoVersion, helper.InvalidVersion, helper.NotAuthenticated,
    helper.PatchInvalidData
):
    def setUp(self) -> None:
        self._setUp(
            Production=True,
            API_Name='Update Url',
            URL=reverse('Url.api:Url', kwargs={'Url_id': 1}),
            URL_Not_Found=reverse('Url.api:Url', kwargs={'Url_id': 10}),
            Host=os.environ.get('HOST')
        )
        self._Authorize()


    def test_url_not_found(self):

        _response = requests.patch(self._url_not_found, headers={
            'Version': 'V1',
            'Authorization': 'Bearer {0}'.format(self._Token)
        }, data={
            'title': 'Edited API Url',
            'description': 'Edited Test API Url Description',
            'url': 'https://www.youtube.com/watch?v=Z1RJmh_OqeA'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 404, self._Message('Url Not Found'))
    

    def test_not_user_url(self):

        self._Authorize(os.environ.get('TEST_USER_USERNAME'), os.environ.get('TEST_USER_PASSWORD'))

        _response = requests.patch(self._url, headers={
            'Version': 'V1',
            'Authorization': 'Bearer {0}'.format(self._Token)
        }, data={
            'title': 'Edited API Url',
            'description': 'Edited Test API Url Description',
            'url': 'https://www.youtube.com/watch?v=Z1RJmh_OqeA'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 404, self._Message('Not User Url'))


    def test_edit_url(self):

        _response = requests.patch(self._url, headers={
            'Version': 'V1',
            'Authorization': 'Bearer {0}'.format(self._Token)
        }, data={
            'title': 'Edited API Url',
            'description': 'Edited Test API Url Description',
            'url': 'https://www.youtube.com/watch?v=Z1RJmh_OqeA'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 200, self._Message('Edit Url'))
