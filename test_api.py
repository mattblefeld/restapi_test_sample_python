import requests
import pytest


@pytest.mark.ron
class TestRonSwansonApi:
    test_url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

    def test_api_provides_valid_response(self):
        response = requests.get(self.test_url)
        assert (response.status_code is 200) is True

    def test_api_provides_content(self):
        response = requests.get(self.test_url)
        assert (response.text is not "") is True


@pytest.mark.geo
class TestGeoLocationAPI:
    test_url = "http://api.zippopotam.us/us/"

    def test_api_response_is_json(self):
        response = requests.get(self.test_url + "33498")
        assert ("application/json" in response.headers['Content-Type']) is True

    @pytest.mark.parametrize('location', ["90210", "33498", "10012", "90036", "60601"])
    def test_api_response_parameterized_through_pytest(self, location):
        response = requests.get(self.test_url + location)
        assert (response.status_code is 200) is True

    @pytest.mark.parametrize('location', [[{"state": "CA"}, {"zipcode": "90210"}],
                                          [{"state": "FL"}, {"zipcode": "33498"}],
                                          [{"state": "NY"}, {"zipcode": "10012"}],
                                          [{"state": "CA"}, {"zipcode": "90036"}],
                                          [{"state": "IL"}, {"zipcode": "60601"}]]
                             )
    def test_response_has_valid_state_for_zipcode(self, location):
        response = requests.get(self.test_url + location[1]['zipcode'])
        body = response.json()
        assert (body['places'][0]['state abbreviation'] == location[0]['state']) is True
