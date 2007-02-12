Summary:	Network traffic monitoring utility
Summary(pl.UTF-8):	Narzędzie do monitorowania ruchu w sieci
Name:		trafshow
Version:	5.2.3
Release:	1
License:	Free copying + BSD license
Group:		Networking/Utilities
Source0:	ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}.tgz
# Source0-md5:	0b2f0bb23b7832138b7d841437b9e182
URL:		http://soft.risp.ru/trafshow/
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
trafshow is a ncurses based utility showing you in detail the network
traffic. It shows you a table with source address, source port,
destination address, destination port, IP proto, byte counter and CPS.
Counters are updated on package receiving, and the table is resorted
by byte counter with given interval.

trafshow accept filters like tcpdump so you can inspect a required
part of network traffic.

%description -l pl.UTF-8
trafshow jest opartym o ncurses narzędziem pokazującym szczegółowo
ruch w sieci. Pokazuje tabelę z adresami i portami źródłowymi,
adresami i portami docelowymi, protokołem, liczbą bajtów i CPS.
Liczniki są uaktualniane po otrzymaniu pakietu, a tabela ponownie
sortowana po ilości bajtów co podany czas.

trafshow akceptuje filtry podobne do tcpdump, więc można śledzić
wybraną część ruchu.

%prep
%setup -q
sed -i 's/static//' screen.c

%build
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,%{_sysconfdir}}
install trafshow $RPM_BUILD_ROOT%{_sbindir}
install trafshow.1 $RPM_BUILD_ROOT%{_mandir}/man1
install .trafshow $RPM_BUILD_ROOT%{_sysconfdir}/trafshow

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_sbindir}/trafshow
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/trafshow
%{_mandir}/man1/trafshow.1*
