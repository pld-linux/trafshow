Summary:	Network traffic monitoring utility
Summary(pl):	Narzêdzie do monitorowania ruchu w sieci
Name:		trafshow
Version:	2.0
Release:	3
License:	Free copying + BSD license
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}.tgz
Source1:	ftp://castle.nmd.msu.ru/patches/linux-includes-1.tgz
Patch0:		ftp://castle.nmd.msu.ru/patches/%{name}-2.0-pcap.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-glibc.patch
URL:		http://soft.risp.ru/trafshow/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
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
ruch w sieci. Pojazuje tabelê z adresami i portami ¼ród³owymi,
adresami i portami docelowymi, protoko³em, liczb± bajtów i CPS.
Liczniki s± uaktualniane po otrzymaniu pakietu, a tabela ponownie
sortowana po ilo¶ci bajtów co podany czas.

trafshow akceptuje filtry podobne do tcpdump, wiêc mo¿na ¶ledziæ
wybran± czê¶æ ruchu.

%prep
%setup -q
%setup -q -D -T -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} FLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{mandir}/man1}
install trafshow/trafshow $RPM_BUILD_ROOT%{_sbindir}
install trafshow.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/trafshow
%{_mandir}/man1/trafshow.1*
