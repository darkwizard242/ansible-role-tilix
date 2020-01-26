import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tilix_package_installed(host):
    assert host.package("tilix").is_installed


def test_tilix_binary_exists(host):
    assert host.file('/usr/bin/tilix').exists


def test_tilix_binary_file(host):
    assert host.file('/usr/bin/tilix').is_file


def test_tilix_binary_which(host):
    assert host.check_output('which tilix') == '/usr/bin/tilix'
