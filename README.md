
Ansible Role: tilix
=========

Role to install (_by default_) `tilix` package  or uninstall (_if  passed as var_)  on **Debian** based systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
tilix_app: tilix
tilix_desired_state: present
```

Variable `tilix_app`: Defines the app to install i.e. **tilix**

Variable `tilix_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **tilix** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.tilix
```

For customizing behavior of role (i.e. installation of latest **tilix** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.tilix
      vars:
        tilix_desired_state: latest
```
             
For customizing behavior of role (i.e. un-installation of **tilix** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.tilix
      vars:
        tilix_desired_state: absent
```      
         
License
-------

[MIT](https://github.com/darkwizard242/ansible-role-tilix/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
