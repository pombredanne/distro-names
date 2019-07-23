import pytest

from distro.distro import Distro


class TestDistro(object):
    @pytest.fixture()
    def distros(self):
        return Distro()

    def test_search_by_name(self, distro):
        pass
