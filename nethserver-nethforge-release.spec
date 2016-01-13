Summary: NethForge repositories
Name: nethserver-nethforge-release
Version: 6
Release: 1
License: GPL
BuildArch: noarch
Source0: NethForge.repo 
Source1: RPM-GPG-KEY-NETHFORGE-6

Requires: nethserver-release

%description
This package contains NethForge modules repository and
GPG key.


%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%install
rm -rf %{buildroot}

#GPG Key
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-NETHFORGE-6

# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/NethForge.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-NETHFORGE-6

%changelog
* Wed Jun 04 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6-1
- Initial Package
