%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global upstream_name puppet-kmod
%global commit c3d90861081864c2e7d4a53d474a605e6f2ac70d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-kmod
Version:        3.0.1
Release:        0.1%{?milestone}%{?alphatag}%{?dist}
Summary:        Manage Linux kernel modules with Puppet
License:        ASL 2.0

URL:            https://github.com/camptocamp/puppet-kmod

Source0:        https://github.com/camptocamp/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Manage Linux kernel modules with Puppet

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/kmod/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/kmod/



%files
%{_datadir}/openstack-puppet/modules/kmod/


%changelog
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 3.0.1-0.1.0rc0.c3d9086git
- Update to post 3.0.1-rc0 (c3d90861081864c2e7d4a53d474a605e6f2ac70d)



