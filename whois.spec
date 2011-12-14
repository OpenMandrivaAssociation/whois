Summary:	Enhanced WHOIS client
Name:		whois
Version:	5.0.13
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.linux.it/~md/software/
Source0:	ftp://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	libidn-devel
Provides:	fwhois
Obsoletes:	fwhois
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a new whois (RFC 954) client rewritten from scratch.

It is derived from and compatible with the usual BSD and RIPE whois(1)
programs.

It is intelligent and can automatically select the appropriate whois
server for most queries.

%prep
%setup -q

%build
%make OPTS="%{optflags}" HAVE_LIBIDN=1 LDFLAGS="%ldflags" whois pos

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1

%makeinstall BASEDIR=%{buildroot} prefix=%{_prefix}/ mandir=%{_mandir}
%makeinstall BASEDIR=%{buildroot} prefix=%{_prefix}/ mandir=%{_mandir} -C po

install -m0644 whois.conf %{buildroot}%{_sysconfdir}

%find_lang %{name} %{name}.lang

# fix a file conflict with expect (#46500)
mv %{buildroot}%{_bindir}/mkpasswd %{buildroot}%{_bindir}/whois-mkpasswd
mv %{buildroot}%{_mandir}/man1/mkpasswd.1 %{buildroot}%{_mandir}/man1/whois-mkpasswd.1

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/whois.conf
%{_bindir}/whois
%{_bindir}/whois-mkpasswd
%{_mandir}/man1/whois.1*
%{_mandir}/man1/whois-mkpasswd.1*
