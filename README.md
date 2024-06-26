[![build-test](https://github.com/darkwizard242/ansible-role-tilix/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-tilix/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-tilix/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-tilix/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43058?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/tilix) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-tilix&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-tilix) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-tilix&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-tilix) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-tilix&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-tilix) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-tilix?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-tilix?color=orange&style=flat-square)

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

Variable            | Description
------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
tilix_app           | Defines the app to install on Debian based systems i.e. **tilix**
tilix_desired_state | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
