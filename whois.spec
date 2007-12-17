%define name whois
%define version 4.7.22
%define release %mkrel 1
%define url http://www.linux.it/~md/software/

Summary: Enhanced WHOIS client
Name: %{name}
Version: %{version}
Release: %{release}
Source: ftp://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.gz
URL: %{url}
License: GPL
Group: Networking/Other
BuildRequires:	gettext
Obsoletes: fwhois
Provides: fwhois

%description
This is a new whois (RFC 954) client rewritten from scratch.

It is derived from and compatible with the usual BSD and RIPE whois(1)
programs.

It is intelligent and can automatically select the appropriate whois
server for most queries.

%prep
%setup -q

%build
%make OPTS="%optflags" whois

%install
rm -rf %buildroot
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1
make install BASEDIR=%buildroot prefix=%{_prefix}/ mandir=%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc [A-Z][A-Z]*
%{_bindir}/*
%{_mandir}/*/*


