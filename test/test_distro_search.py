import pytest

from distro.distro import load, search


class TestDistroSearch(object):
    @pytest.fixture()
    def distros(self):
        return load()

    def test_empty_search(self):
        raise NotImplementedError

    def test_single_term_no_result(self):
        raise NotImplementedError

    def test_single_term_one_result(self):
        raise NotImplementedError

    def test_single_term_multiple_results(self):
        raise NotImplementedError

    def test_two_terms_no_result(self):
        raise NotImplementedError

    def test_two_terms_one_result(self):
        raise NotImplementedError

    def test_two_terms_multiple_results(self):
        raise NotImplementedError


class TestDistroSearchOutput(object):
    @pytest.fixture()
    def distros(self):
        return load()

    def test_output_text(self, distros):
        search(['xxx'], distros)
        raise NotImplementedError

    def test_output_csv(self, distros):
        search(['xxx'], distros)
        raise NotImplementedError

    def test_output_json(self, distros):
        search(['xxx'], distros)
        raise NotImplementedError
