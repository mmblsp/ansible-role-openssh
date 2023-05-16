import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_installed_packages(host):
    package_list_apt = ['openssh-server', 'openssh-client']
    package_list_rpm = ['openssh-server', 'openssh-clients']
    if host.system_info.distribution in ['alt', 'centos']:
        for pkg in package_list_rpm:
            assert host.package(pkg).is_installed
    elif host.system_info.distribution == 'astralinuxce':
        for pkg in package_list_apt:
            assert host.package(pkg).is_installed

def test_is_listening_22port(host):
    assert host.socket("tcp://0.0.0.0:22").is_listening
