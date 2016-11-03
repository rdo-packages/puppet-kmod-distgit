%{!?upstream_version: %global upstream_version %{commit}}
%global upstream_name puppet-kmod
%global commit ea03df0eff7b7e5faccb9c4e386d451301468f04
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-kmod
Version:        2.1.1
Release:        1%{?alphatag}%{?dist}
Summary:        Manage Linux kernel modules with Puppet
License:        Apache-2.0

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
* Thu Nov 03 2016 Jon Schlueter <jschluet@redhat.com> 2.1.1-1
- Update to 2.1.1 (ea03df0eff7b7e5faccb9c4e386d451301468f04) latest tag
  0d69a96 is next commit past 2.1.1 tag with a module sync update

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.0.1-1.0d69a96.git
- Newton update 0.0.1 (0d69a96e8d0d3a08da0d5f476c733134df4fb9ee)

