import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


TILIX_BINARY_PATH = '/usr/bin/tilix'
TILIX_PACKAGE = 'tilix'


def test_tilix_package_installed(host):
    host.package("TILIX_PACKAGE").is_installed


def test_tilix_binary_exists(host):
    host.file('TILIX_BINARY_PATH').exists


def test_tilix_binary_file(host):
    host.file('TILIX_BINARY_PATH').is_file


def test_tilix_binary_whereis(host):
    host.check_output('whereis tilix') == TILIX_BINARY_PATH
