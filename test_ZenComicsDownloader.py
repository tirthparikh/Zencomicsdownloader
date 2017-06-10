from unittest import mock
import requests

from ZenComicsDownloader import check_connection


class TestClass():
    def test_check_connection_for_Invalid_Url(self):
        assert check_connection("zenpencils.com") == (
            False,
            "Invalid URL "+"zenpencils.com")

    @mock.patch("ZenComicsDownloader.requests.get")
    def test_check_connection_for_HTTPError(self, mock_get):
        """Testing the check_connection method for HTTPError"""
        mock_response = mock.Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = http_error

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response
        assert check_connection("http://zenpencils.com") == (
            False,
            "HTTPError :404")

    @mock.patch("ZenComicsDownloader.requests.get")
    def test_check_connection_for_Timeout(self, mock_get):
        """Testing the check_connection method for Timeouterror"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.Timeout()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert check_connection("http://zenpencils.com") == (
            False,
            "Connection Timeout! Please retry.")

    @mock.patch("ZenComicsDownloader.requests.get")
    def test_check_connection_for_TooManyRedirects(self, mock_get):
        """Testing the check_connection method for Too Many Redirects"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.TooManyRedirects()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert check_connection("http://zenpencils.com") == (
            False,
            "Too Many Redirects! Please refresh check the URL")

    @mock.patch("ZenComicsDownloader.requests.get")
    def test_check_connection_for_Connection_Error(self, mock_get):
        """Testing the check_connection method for Timeouterror"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.ConnectionError()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert check_connection("http://zenpencils.com") == (
            False, "Connection Error! PLease check you Connections")
