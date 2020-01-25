Summary:	A utility to collect various linux performance data
Name:		collectl
Version:	2.5.1
Release:	0.1
License:	Artistic, GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/collectl/%{name}-%{version}-src.tar.gz
# Source0-md5:	eea1db0893ee9911bc9c10b1e7f687ac
URL:		http://collectl.sourceforge.net
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	perl-base >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to collect linux performance data.

%prep
%setup -q
%{__sed} -i -e 's,\r$,,' docs/FAQ-collectl.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,/etc/rc.d/init.d,/var/log/%{name},%{_sysconfdir}}
cp -a man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install initd/collectl $RPM_BUILD_ROOT/etc/rc.d/init.d
install collectl.pl $RPM_BUILD_ROOT%{_sbindir}/collectl
cp -a formatit.ph $RPM_BUILD_ROOT%{_sbindir} # XXX, move it out of sbindir, as not executable and not directly invokable
cp -a collectl.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* RELEASE-collectl
%attr(754,root,root) /etc/rc.d/init.d/collectl
%attr(755,root,root) %{_sbindir}/collectl
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/collectl.conf
# XXX not executable
%{_sbindir}/formatit.ph
%{_mandir}/man1/*
