import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'tilix'
PACKAGE_BINARY = '/usr/bin/tilix'


def test_tilix_package_installed(host):
    """
    Tests if tilix is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_tilix_binary_exists(host):
    """
    Tests if tilix binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_tilix_binary_file(host):
    """
    Tests if tilix binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_tilix_binary_which(host):
    """
    Tests the output to confirm tilix's binary location.
    """
    assert host.check_output('which tilix') == PACKAGE_BINARY
