Summary:	Enhanced WHOIS client
Name:		whois
Version:	5.3.1
Release:	2
License:	GPLv2+
Group:		Networking/Other
URL:		https://github.com/rfc1036/whois
Source0:	https://github.com/rfc1036/whois/archive/v%{version}.tar.gz
Patch0:		whois-5.2.20-eegg.patch
BuildRequires:	gettext
BuildRequires:	libidn-devel
%rename	fwhois

%description
This is a new whois (RFC 954) client rewritten from scratch.

It is derived from and compatible with the usual BSD and RIPE whois(1)
programs.

It is intelligent and can automatically select the appropriate whois
server for most queries.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags

%make OPTS="%{optflags}" HAVE_ICONV=1 LDFLAGS="%{ldflags}" CONFIG_FILE="%{_sysconfdir}/whois.conf"

%install
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

%files -f %{name}.lang
%doc README
%config(noreplace) %{_sysconfdir}/whois.conf
%{_bindir}/whois
%{_bindir}/whois-mkpasswd
%{_mandir}/man1/whois.1*
%{_mandir}/man1/whois-mkpasswd.1*
%{_mandir}/man5/whois.conf.5*
