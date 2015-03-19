Summary: NethForge repositories
Name: nethserver-nethforge-release
Version: 6.6
Release: 3%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

Requires: yum
Requires: centos-release

%description
This package contains NethForge modules repository and
GPG key.

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 644 RPM-GPG-KEY-NETHFORGE-6 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-NETHFORGE-6
install -Dpm 644 NethForge.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/NethForge.repo

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/NethForge.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-NETHFORGE-6

%changelog
* Thu Mar 19 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-3
- Updated mirrorlist URL and fixed spec file

* Mon Mar 16 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-2
- Use YUM mirrorlist plugin for NethServer 6.6

* Wed Jun 04 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6-1
- Initial Package
