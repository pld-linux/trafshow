Name:		trafshow
Version:	2.0
Release:	1
Copyright:	Free copying + BSD license
Source0:	trafshow-2.0.tgz
Source1:	ftp://ftp.ee.lbl.gov/libpcap-0.3.1a3.tar.Z
Source2:	ftp://castle.nmd.msu.ru/patches/linux-includes-1.tgz
Patch0:		ftp://castle.nmd.msu.ru/patches/trafshow-2.0-pcap.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Summary:	Network traffic monitoring utility
Group:		Networking/Utilities

%description
trafshow is a ncurses based utility showing you in detail the network
traffic. It shows you a table with source address, source port, destination
address, destination port, IP proto, byte counter and CPS. Counters are
updated on package receiving, and the table is resorted by byte counter
with given interval.

trafshow accept filters like tcpdump so you can inspect a required part of
network traffic.

%prep
%setup -q
#%setup -D -T -a 1
#%setup -D -T -a 2
%patch -p1
#ln -s libpcap-0.3.1a3 libpcap

%build
#( cd libpcap; ./configure; make )
make

%install
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1
install -s -m 0755 trafshow/trafshow $RPM_BUILD_ROOT%{_sbindir}
install -m 0644 trafshow.1 $RPM_BUILD_ROOT%{_prefix}/man/man1

%files
%defattr(644,root,root,755)
%{_sbindir}/trafshow
%{_prefix}/man/man1/trafshow.1
