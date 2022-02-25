from django.test import SimpleTestCase
from django.urls import reverse
from ... import helper
import requests, os




class TestApi(
    SimpleTestCase, helper.TestAPIHelper, helper.NoVersion, helper.InvalidVersion,
    helper.TokenNotInQuery, helper.TokenNotFound
):
    def setUp(self) -> None:
        self._setUp(
            Production=True,
            API_Name='Post Reset Password',
            URL=reverse('Auth.api:Reset-Password'),
            Host=os.environ.get('HOST')
        )
    

    def test_user_not_active(self):

        _response = requests.get(self._url, headers={
            'Version': 'V1'
        }, params={
            'Token': 'UWKWDkJRYljg4Qey7oIJEpG3A0X0hhk-nU4OSFsYkHbZRRB-r7yhP35a9OJKnHbDSMqpvZ7Fwgdx6Z6ugMdP'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 404, self._Message('User Not Active'))
    

    def test_reset_password(self):

        _response = requests.patch(self._url, headers={
            'Version': 'V1'
        }, params={
            'Token': 'T33enLGiR9-BH4MkpBdJ0F3iUa7HYrCJChjzOc-AIVeKzADz3aGTnSAelemJjBJ72JDGGBEZFu1HVmGIzsRTcFMH5P8'
        }, data={
            'password': 'P@ssw0rd'
        })

        self._print(_response)

        self.assertTrue(_response.status_code == 200, self._Message('Reset Password'))
