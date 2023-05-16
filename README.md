Role openssh
=========

Install openssh and config sshd

Requirements
------------

There are no specific requirements

Role Variables
--------------

openssh_permit_root_login: "no" or "yes"
openssh_port: 22

Dependencies
------------

There are no specific dependencies

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ssh }

License
-------

Apache 2.0

Author Information
------------------

[VK](https://vk.com/mmblspace)
