Summary:	Enhanced WHOIS client
Name:		whois
Version:	4.7.26
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.linux.it/~md/software/
Source0:	ftp://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	libidn-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Obsoletes:	fwhois
Provides:	fwhois

%description
This is a new whois (RFC 954) client rewritten from scratch.

It is derived from and compatible with the usual BSD and RIPE whois(1)
programs.

It is intelligent and can automatically select the appropriate whois
server for most queries.

%prep
%setup -q

%build
%make OPTS="%{optflags}" HAVE_LIBIDN=1 whois

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall BASEDIR=%{buildroot} prefix=%{_prefix}/ mandir=%{_mandir}

install whois.conf %{buildroot}%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/whois.conf
%{_bindir}/*
%{_mandir}/*/*
