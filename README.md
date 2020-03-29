[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-tilix.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-tilix) ![Ansible Role](https://img.shields.io/ansible/role/43058?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43058?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43058?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-tilix&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-tilix) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-tilix?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-tilix?color=orange&style=flat-square)

# Ansible Role: tilix

Role to install (_by default_) [tilix](https://gnunn1.github.io/tilix-web/) package or uninstall (_if passed as var_) on **Ubuntu 18.04** and **Debian 10** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
tilix_app: tilix
tilix_desired_state: present
```

### Variables table:

Variable            | Value (default) | Description
------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
tilix_app           | tilix           | Defines the app to install on Debian based systems i.e. **tilix**
tilix_desired_state | present         | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **tilix** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tilix
```

For customizing behavior of role (i.e. installation of latest **tilix** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tilix
  vars:
    tilix_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **tilix** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tilix
  vars:
    tilix_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-tilix/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
