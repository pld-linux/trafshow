Summary:	Network traffic monitoring utility
Summary(pl):	Narz�dzie do monitorowania ruchu w sieci
Name:		trafshow
Version:	3.1
Release:	2
License:	Free copying + BSD license
Group:		Networking/Utilities
Source0:	ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}.tgz
# Source0-md5:	085b99f160002a269b358aab1c5004f0
Patch0:		ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}-ipv6.patch
# Patch0-md5:	47a711438072e690029c3abd54c9f50e
Patch1:		%{name}-3.1-corect_ipv6.patch
Patch2:		%{name}-3.1-show-ppp.patch
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
trafshow jest opartym o ncurses narz�dziem pokazuj�cym szczeg�owo
ruch w sieci. Pojazuje tabel� z adresami i portami �r�d�owymi,
adresami i portami docelowymi, protoko�em, liczb� bajt�w i CPS.
Liczniki s� uaktualniane po otrzymaniu pakietu, a tabela ponownie
sortowana po ilo�ci bajt�w co podany czas.

trafshow akceptuje filtry podobne do tcpdump, wi�c mo�na �ledzi�
wybran� cz�� ruchu.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
./configure
%{__make} CC="%{__cc}" CFLAGS="-DHAVE_CONFIG_H -DINET6=1 %{rpmcflags} -I. -I%{_includedir}/ncurses -D_BSD_SOURCE=1"

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
%attr(755,root,root) %{_sbindir}/trafshow
%{_mandir}/man1/trafshow.1*
%{_sysconfdir}/trafshow
