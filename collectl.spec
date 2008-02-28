Summary:	A utility to collect various linux performance data
Name:		collectl
Version:	2.4.3
Release:	0.1
License:	Artistic, GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/collectl/%{name}-%{version}-src.tar.gz
URL:		http://collectl.sourceforge.net
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to collect linux performance data.

%prep
%setup -q

%build

%clean
rm -Rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir}}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/init.d
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT/var/log/%{name}

%files
%defattr(644,root,root,755)
