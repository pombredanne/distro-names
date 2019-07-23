import pytest

from distro.distro import load


class TestDistroClass(object):
    @pytest.fixture()
    def distros(self):
        return load()

    def test_name_required(self):
        raise NotImplementedError

    def test_version_or_versions_required(self):
        raise NotImplementedError

    def test_versions_list(self):
        raise NotImplementedError

    def test_version_absent(self):
        raise NotImplementedError

    def test_default_flavour(self):
        raise NotImplementedError

    def test_extra_args(self):
        raise NotImplementedError

    def test_setup_from_dict(self):
        raise NotImplementedError

    def test_setup_from_args(self):
        raise NotImplementedError

    def test_output_str(self):
        raise NotImplementedError

    def test_output_raw(self):
        raise NotImplementedError
