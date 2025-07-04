Summary:	Enhanced WHOIS client
Name:		whois
Version:	5.6.2
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		https://github.com/rfc1036/whois
Source0:	https://github.com/rfc1036/whois/archive/refs/tags/v%{version}.tar.gz
Patch0:		whois-5.2.20-eegg.patch
BuildRequires:	gettext
BuildRequires:	pkgconfig(libidn2)
BuildRequires:	pkgconfig(libxcrypt)
BuildRequires:	pkgconfig(bash-completion)
%rename	fwhois

%description
This is a new whois (RFC 954) client rewritten from scratch.

It is derived from and compatible with the usual BSD and RIPE whois(1)
programs.

It is intelligent and can automatically select the appropriate whois
server for most queries.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build OPTS="%{optflags} -Oz" HAVE_ICONV=1 LDFLAGS="%{build_ldflags}" CONFIG_FILE="%{_sysconfdir}/whois.conf"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1

%make_install BASEDIR=%{buildroot} prefix=%{_prefix}/ mandir=%{_mandir}
%make_install BASEDIR=%{buildroot} prefix=%{_prefix}/ mandir=%{_mandir} -C po

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
%{_datadir}/bash-completion/completions/mkpasswd
%{_datadir}/bash-completion/completions/whois
%doc %{_mandir}/man1/whois.1*
%doc %{_mandir}/man1/whois-mkpasswd.1*
%doc %{_mandir}/man5/whois.conf.5*
