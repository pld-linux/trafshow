Summary:	Network traffic monitoring utility
Summary(pl):	Narzêdzie do monitorowania ruchu w sieci
Name:		trafshow
Version:	4.0
Release:	1
License:	Free copying + BSD license
Group:		Networking/Utilities
Source0:	ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}.tgz
# Source0-md5:	994355d6ba98d96ce06db9c92ae41669
URL:		http://soft.risp.ru/trafshow/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel

%description
trafshow is a ncurses based utility showing you in detail the network
traffic. It shows you a table with source address, source port,
destination address, destination port, IP proto, byte counter and CPS.
Counters are updated on package receiving, and the table is resorted
by byte counter with given interval.

trafshow accept filters like tcpdump so you can inspect a required
part of network traffic.

%description -l pl
trafshow jest opartym o ncurses narzêdziem pokazuj±cym szczegó³owo
ruch w sieci. Pokazuje tabelê z adresami i portami ¼ród³owymi,
adresami i portami docelowymi, protoko³em, liczb± bajtów i CPS.
Liczniki s± uaktualniane po otrzymaniu pakietu, a tabela ponownie
sortowana po ilo¶ci bajtów co podany czas.

trafshow akceptuje filtry podobne do tcpdump, wiêc mo¿na ¶ledziæ
wybran± czê¶æ ruchu.

%prep
%setup -q

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
%doc README
%attr(755,root,root) %{_sbindir}/trafshow
%{_mandir}/man1/trafshow.1*
%{_sysconfdir}/trafshow
