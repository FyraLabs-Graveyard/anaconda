ExclusiveArch: i386 ia64 alpha
Name: anaconda
Version: 7.1.95
Release: 0.2
Copyright: GPL
Summary: The Red Hat Linux installation program.
Group: Applications/System
Source: anaconda-%{PACKAGE_VERSION}.tar.bz2
Obsoletes: anaconda-reconfig
BuildPreReq: pump-devel, kudzu-devel, pciutils-devel, bzip2-devel, e2fsprogs-devel, python-devel db3-devel gtk+-devel gnome-libs-devel rpm-python, newt-devel, rpm-devel, gettext
Prereq: chkconfig /etc/init.d
Requires: rpm-python
Excludearch: sparc sparc64

BuildRoot: /var/tmp/anaconda-%{PACKAGE_VERSION}

%description
The anaconda package contains portions of the Red Hat Linux
installation program which can then be run by the user for
reconfiguration and advanced installation options.

%package runtime
Summary: Red Hat Linux installer portions needed only for fresh installs.
Group: Applications/System
AutoReqProv: false

%description runtime
The anaconda-runtime package contains parts of the Red Hat Linux
installer which are needed for installing new systems. These files are
used to build Red Hat Linux media sets, but are not meant for use on
already installed systems.

%prep

%setup -q

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
#strip $RPM_BUILD_ROOT/usr/sbin/ddcprobe

strip $RPM_BUILD_ROOT/usr/lib/anaconda/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
chkconfig --add reconfig

%preun
if [ $1 = 0 ]; then
	chkconfig --del reconfig
fi

%files
%defattr(-,root,root)
%doc COPYING
%doc docs/command-line.txt
/usr/sbin/anaconda
/usr/share/anaconda
/usr/share/locale/*/*/*
/usr/lib/anaconda
%ifarch i386
/usr/sbin/ddcprobe
%endif

%config /etc/rc.d/init.d/reconfig

%files runtime
%defattr(-,root,root)
/usr/lib/anaconda-runtime

%define date    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog
* %{date} Anaconda team <bugzilla@redhat.com>
- built new version from CVS

* Wed Jul 18 2001 Jeremy Katz <katzj@redhat.com>
- own /usr/lib/anaconda and /usr/share/anaconda

* Fri Jan 12 2001 Matt Wilson <msw@redhat.com>
- sync text with specspo

* Thu Aug 10 2000 Matt Wilson <msw@redhat.com>
- build on alpha again now that I've fixed the stubs

* Wed Aug  9 2000 Michael Fulbright <drmike@redhat.com>
- new build

* Fri Aug  4 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- allow also subvendorid and subdeviceid in trimpcitable

* Fri Jul 14 2000 Matt Wilson <msw@redhat.com>
- moved init script for reconfig mode to /etc/init.d/reconfig
- move the initscript back to /etc/rc.d/init.d
- Prereq: /etc/init.d

* Thu Feb 03 2000 Michael Fulbright <drmike@redhat.com>
- strip files
- add lang-table to file list

* Wed Jan 05 2000 Michael Fulbright <drmike@redhat.com>
- added requirement for rpm-python

* Mon Dec 06 1999 Michael Fulbright <drmike@redhat.com>
- rename to 'anaconda' instead of 'anaconda-reconfig'

* Fri Dec 03 1999 Michael Fulbright <drmike@redhat.com>
- remove ddcprobe since we don't do X configuration in reconfig now

* Tue Nov 30 1999 Michael Fulbright <drmike@redhat.com>
- first try at packaging reconfiguration tool

