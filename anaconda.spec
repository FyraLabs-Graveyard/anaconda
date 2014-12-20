%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Version: 22.13
Release: 1%{?dist}
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).

# Also update in AM_GNU_GETTEXT_VERSION in configure.ac
%define gettextver 0.18.3
%define intltoolver 0.31.2-3
%define pykickstartver 1.99.65
%define yumver 3.4.3-91
%define dnfver 0.4.18
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define nmver 0.9.9.0-10.git20130906
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.23-1
%define sckeyboardver 1.3.1
%define firewalldver 0.3.5-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 034-7
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.870-3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.18-1
%define libxklavierver 5.4
%define libtimezonemapver 0.4.1-2
%define helpver 22.1-1

BuildRequires: audit-libs-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gtk3-devel-docs
BuildRequires: glib2-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: pygobject3
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libgnomekbd-devel
BuildRequires: libxklavier-devel >= %{libxklavierver}
BuildRequires: pango-devel
BuildRequires: pykickstart >= %{pykickstartver}
%if ! 0%{?rhel}
BuildRequires: python-bugzilla
%endif
BuildRequires: python-devel
BuildRequires: python-urlgrabber >= %{pythonurlgrabberver}
BuildRequires: python-nose
BuildRequires: systemd
BuildRequires: yum >= %{yumver}
BuildRequires: NetworkManager-devel >= %{nmver}
BuildRequires: NetworkManager-glib-devel >= %{nmver}
BuildRequires: dbus-devel >= %{dbusver}
BuildRequires: dbus-python
BuildRequires: rpm-devel >= %{rpmver}
BuildRequires: libarchive-devel >= %{libarchivever}
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif
BuildRequires: libtimezonemap-devel >= %{libtimezonemapver}

Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-gui = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Requires: dnf >= %{dnfver}
Requires: python-blivet >= 1:0.70
Requires: python-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libselinux-python
Requires: rpm-python >= %{rpmver}
Requires: parted >= %{partedver}
Requires: pyparted >= %{pypartedver}
Requires: yum >= %{yumver}
Requires: python-urlgrabber >= %{pythonurlgrabberver}
Requires: pykickstart >= %{pykickstartver}
Requires: langtable-data >= %{langtablever}
Requires: langtable-python >= %{langtablever}
Requires: libuser-python
Requires: authconfig
Requires: firewalld >= %{firewalldver}
Requires: util-linux >= %{utillinuxver}
Requires: dbus-python
Requires: python-pwquality
Requires: python-IPy
Requires: pytz
Requires: realmd
Requires: teamd
%ifarch %livearches
Requires: usermode
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum >= %{isomd5sum}
Requires: yum-utils >= %{yumutilsver}
Requires: createrepo_c
Requires: NetworkManager >= %{nmver}
Requires: dhclient
Requires: libselinux-python
Requires: kbd
Requires: chrony
Requires: python-ntplib
Requires: rsync
Requires: systemd
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif

Requires: python-coverage

# required because of the rescue mode and VNC question
Requires: anaconda-tui = %{version}-%{release}

Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty <= 0.107-1

%description core
The anaconda-core package contains the program which was used to install your
system.

%package gui
Summary: Graphical user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-widgets = %{version}-%{release}
Requires: python-meh-gui >= %{mehver}
Requires: adwaita-icon-theme
Requires: system-logos
Requires: tigervnc-server-minimal
Requires: libxklavier >= %{libxklavierver}
Requires: libgnomekbd
Requires: libtimezonemap >= %{libtimezonemapver}
Requires: nm-connection-editor
%ifarch %livearches
Requires: zenity
%endif
Requires: keybinder3
%ifnarch s390 s390x
Requires: NetworkManager-wifi
%endif
Requires: anaconda-user-help >= %{helpver}
Requires: yelp

%description gui
This package contains graphical user interface for the Anaconda installer.

%package tui
Summary: Textual user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}

%description tui
This package contains textual user interface for the Anaconda installer.

%package widgets
Summary: A set of custom GTK+ widgets for use with anaconda
Group: System Environment/Libraries
Requires: pygobject3
Requires: python

%description widgets
This package contains a set of custom GTK+ widgets used by the anaconda installer.

%package widgets-devel
Summary: Development files for anaconda-widgets
Group: Development/Libraries
Requires: glade
Requires: %{name}-widgets%{?_isa} = %{version}-%{release}

%description widgets-devel
This package contains libraries and header files needed for writing the anaconda
installer.  It also contains Python and Glade support files, as well as
documentation for working with this library.

%package dracut
Summary: The anaconda dracut module
Requires: dracut >= %{dracutver}
Requires: dracut-network
Requires: xz
Requires: pykickstart

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q

%build
%configure --disable-static \
           --enable-introspection \
           --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%ifarch %livearches
desktop-file-install ---dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%endif
# NOTE: If you see "error: Installed (but unpackaged) file(s) found" that include liveinst files,
#       check the IS_LIVEINST_ARCH in configure.ac to make sure your architecture is properly defined

%find_lang %{name}

%post widgets -p /sbin/ldconfig
%postun widgets -p /sbin/ldconfig


%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files
%doc COPYING

%files core -f %{name}.lang
%doc COPYING
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
%exclude %{_libdir}/python*/site-packages/pyanaconda/rescue.py*
%exclude %{_libdir}/python*/site-packages/pyanaconda/text.py*
%exclude %{_libdir}/python*/site-packages/pyanaconda/ui/gui/*
%exclude %{_libdir}/python*/site-packages/pyanaconda/ui/tui/*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%ifarch %livearches
%{_bindir}/liveinst
%{_sbindir}/liveinst
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_datadir}/applications/*.desktop
%endif

%files gui
%{_libdir}/python*/site-packages/pyanaconda/ui/gui/*

%files tui
%{_libdir}/python*/site-packages/pyanaconda/rescue.py
%{_libdir}/python*/site-packages/pyanaconda/text.py
%{_libdir}/python*/site-packages/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{_libdir}/python*/site-packages/gi/overrides/*

%files widgets-devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Fri Dec 19 2014 Brian C. Lane <bcl@redhat.com> - 22.13-1
- Print the result to the log, not the variable name. (clumens)
- Ellipsize comboboxes (#1170275) (dshea)
- Allow the columns of the container combo box to flow (#1170275) (dshea)
- Allow specifying how much from kickstart_tests to keep. (clumens)
- Fix up two problems in run_kickstart_tests.sh. (clumens)
- Fix detecting errors in groups-and-envs-1.ks. (clumens)
- Add a network command to the various kickstart test ks files. (clumens)
- Reorganize run_kickstart_tests.sh a bit to use parallel. (clumens)
- Use the anaconda-user-help package for help content (mkolman)
- Fix which TUI field is being checked for which input (#1169533) (dshea)
- Fix pylint-reported issues in RPMOSTreePayload (vpodzime)
- rpmostreepayload: Rework remote add handling (walters)
- Remove Requires: python-nss (vpodzime)
- If there's no boot.iso, skip the kickstart tests. (clumens)
- Test that a kickstart file with both an environment and group installs both.
  (clumens)
- Move the ostree test out of its own directory. (clumens)
- Add a general-purpose kickstart-driven testing setup. (clumens)
- Move the pykickstart version test into a different subdirectory. (clumens)
- Really hide and show passphrase warnings (#1162828) (dshea)
- Unsetup the payload on the way out of anaconda (#1164577) (dshea)
- Beware of 0 being the same bool value as None when setting time (vpodzime)
- Fix the last member of the struct_time struct (vpodzime)
- Use a flag to determine if the datetime spoke is shown (vpodzime)
- Put AM/PM label and buttons in a revealer and hide/unhide them (vpodzime)
- Fix issues with the date&time not being updated on timezone changes
  (vpodzime)
- Fix the way we create the list of DASDs needing dasdfmt. (#1073982)
  (sbueno+anaconda)
- Fix threading issues for dasdfmt in gui storage. (#1073982) (sbueno+anaconda)
- Add sshkey kickstart command (bcl)
- Skip setting up env and groups in software spoke for ks (#1173350) (bcl)
- Add missing dnf package selection support (#1169056) (bcl)
- Add variable substitution to DNF (#1164803) (bcl)
- Simplify and robustify handling of fstype combo box. (amulhern)
- Fix warnings about the default parameter that gdk deprecated (dshea)
- Remove the color override from MountpointSelector. (dshea)
- Move the layout indicator color to css and fix the colors (dshea)
- Don't crash in pre-commit if no files changed (dshea)
- Make the Selected Disks and Configure Mount Point dialogs wider (#1171834).
  (clumens)
- Sync up the Selected Disks and Configure Mount Points dialogs (#1171838).
  (clumens)
- Make sure /boot is not LVM LV if we're on s390x (#873135) (sbueno+anaconda)
- Only show the "SYSTEM" heading if there are data mount points under it.
  (clumens)
- Remove an unused import in rpmostreepayload.py. (clumens)
- Use DNF by default (#1156483) (mkolman)
- Check system-release for whether to enable betanag or not (#1168829).
  (clumens)
- rpmostreepayload: Avoid shutil.copytree in favor of cp -r to fix symlinks
  (walters)
- Look for Requires: and BuildRequires: at the front of a line. (clumens)
- Don't attempt to install anaconda packages from the install-requires target.
  (clumens)
- Remove _assureLogoImage (dshea)
- Add a stylesheet property to BaseInstallClass (dshea)
- Fix EOF error that occurs if user input required in x3270. (#1171135)
  (jstodola)
- Print an error when the kickstart file is missing (bcl)
- Remove UserInterface.basepath and UserInterface.basemask definitions.
  (amulhern)
- Remove pointless overrides identified by the pointless override checker.
  (amulhern)
- Add a simple pointless-override checker to pylint checkers. (amulhern)

* Thu Dec 04 2014 Brian C. Lane <bcl@redhat.com> - 22.12-1
- add code so that initramfs created for rescue kernel (#1170589) (gczarcinski)
- Start vncconfig for cutNpaste (hamzy)
- Handle unstaged changes in the pre-commit hook. (dshea)
- Use git status -z (dshea)
- Make Python's default encoding detection work on Live installations
  (#1169019) (vpodzime)
- Force translation files download instead of skipping them (#1169023)
  (vpodzime)
- Completely disable storage tests for the moment. (clumens)
- datetime_spoke: Fix warnings about removing nonexistent source (walters)
- Temporarily disable the BTRFSOnNonBTRFSComponent test. (clumens)
- Remove a slightly lighter grey background from the center of the hubs.
  (clumens)
- Actually fix the message dropping commit. (clumens)
- Make sure storage info bar is displayed (#1166730) (bcl)
- Clear Update Settings when Done clicked (#1167014) (bcl)
- Fix PWQError issues. (sbueno+anaconda)
- network: Add some doc strings (walters)
- It's spoke.title, not spoke.name (#1167036). (clumens)

* Fri Nov 21 2014 Brian C. Lane <bcl@redhat.com> - 22.11-1
- Skip tui askvnc reboot for dirinstall (#1164254) (bcl)
- If a message is for a spoke not on the current hub, throw it away. (clumens)
- Find storage test cases automatically. (clumens)
- Add new storage test cases that reuse results of earlier autopart runs.
  (clumens)
- Support high contrast mode in fedora-welcome (#1160499) (dshea)
- How the GUI test suite disk is displayed has changed. (clumens)
- do not delete liveimg --url=file:/// file (gczarcinski)
- Add support for doing a liveimg kickstart with local file (#1140358) (bcl)
- Create missing parent directories for user's home directory (#1163775) (bcl)
- Related bug can have different fixed-in and state (bcl)
- Provide useful hints on TTY1 during the installation (mkolman)
- Decrease memory requirements on gui tests, and make that attr private.
  (clumens)
- Don't use blivet in the gui tests. (clumens)
- Use MiB/GiB instead of MB/GB in GUI tests. (clumens)
- Make the No Space dialog look less terrible. (clumens)
- Add a test case where it's impossible to reclaim. (clumens)
- Use blivet's Size class instead of ints and such. (clumens)
- Get the gui tests running in parallel. (clumens)
- Add a basic test of the reclaim dialog. (clumens)
- Make images in raw format instead of qcow2. (clumens)
- Allow specifying which of the GUI tests you want to run. (clumens)
- Check if we read something when emptying stdin queue (vpodzime)
- Require min entropy for 'part --encrypted' devices (#1162695) (vpodzime)
- Don't rely on terminal attributes being configurable (#1162702) (vpodzime)
- Check for a GLib source ID of None in unwatchAllProcesses. (dshea)
- Disable payloads that failed to setup (#1162732) (dshea)
- Only enable non-interactive yum plugins (#1111535) (dshea)
- Add a placeholder for a product-specific logo (dshea)
- Load a stylesheet from product.img (dshea)
- Fix make distcheck (mkolman)
- Include help content in the Anaconda tarball (mkolman)
- Fix typo causing traceback when NTP is turned ON/OFF (vpodzime)
- Use /var/tmp for the temp directory when installing anaconda. (clumens)
- Prevent tb on s390x when de-selecting a DASD and doing custom part.
  (sbueno+anaconda)
- Revert "Revert productName repo name change (#1128474)" (bcl)
- Remove a comment that is a blatant lie. (clumens)
- Fix an environment variable setting in the test environment. (clumens)
- Update the background image paths used in Fedora. (dshea)
- Add a pylint module to detect uses of interruptible system calls. (dshea)
- Wrap interruptible system calls in a loop (#1160041) (dshea)
- Unpack the callback data given to us by blivet (vpodzime)
- Add timeout to callbacks waiting for enough entropy (#1073679) (vpodzime)

* Tue Nov 04 2014 Brian C. Lane <bcl@redhat.com> - 22.10-1
- Remove gui, install, and ostree tests from TESTS. (clumens)
- Update the ostree test for the new ostree+grub patches. (clumens)
- Add a timeout when the ostree test checks for proper booting. (clumens)
- bootloader: Bridge efi_dir configuration earlier for rpmostreepayload
  (walters)
- rpmostreepayload: Handle grub2+EFI layout (walters)
- rpmostreepayload: Copy all subdirectories of /usr/lib/ostree-boot (walters)
- Handle the case of rpmostreepayload + GRUB2 (walters)
- Test adding, removing, and reordering keyboard layouts. (clumens)
- Test displaying the help viewer on every screen. (clumens)
- Add functions to UITestCase to grab the contents of a view. (clumens)
- Extend the keyboard GUI test to test adding layout switching. (clumens)
- Add checks for selected language/locale on the welcome screen. (clumens)
- Catch EOFError in raw_input (#1158841) (bcl)
- Ensure we are specifying sensible target sizes for resize. (#1120964)
  (dlehman)
- Set the autopart fstype for boot too (#1112697) (bcl)
- Ensure we are specifying sensible target sizes for resize. (#1120964)
  (dlehman)
- Rework the placement of items on hubs. (dshea)
- Lightly rearrange the nav_area (dshea)
- Do not install interactive exception handler in cmdline mode (#1155979)
  (vpodzime)
- Remove dmidecode from Requires: (vpodzime)
- Wait until all spokes are setup before updating continue button (bcl)
- Allow adding prepboot to a blank disk in custom (#1155660) (bcl)
- Make anaconda more scrollable (#1135024) (dshea)
- Remove unused imports (vpodzime)
- Just preserve the %%addon header args if an addon is missing (#1155026)
  (vpodzime)
- Add a test to verify the help dialog pops up. (clumens)
- Look up most widgets relative to the currently displayed screen. (clumens)
- Make a few more updates for labels that have changed in the GUI. (clumens)
- Warn users about liveinst usage of --updates (#1153550) (bcl)
- Fix handling of md fwraid names in kickstart bootloader command. (#1156354)
  (dlehman)
- Use an empty string for no root password instead of None (#1155576) (dshea)
- Don't allow related bugs without acks (bcl)
- Fix switching environments when no environment is selected (#1018226) (dshea)
- Make size_from_input() and size_from_entry() methods handier. (amulhern)
- Changes around handling of size entries in custom spoke. (amulhern)
- network: handle dbus UnknownMethod exception on invalid objects (#1061796)
  (rvykydal)

* Wed Oct 22 2014 Brian C. Lane <bcl@redhat.com> - 22.9-1
- When I renamed the date & time spoke, I missed one string. (clumens)
- Fix two more problems with spoke selectors in GUI testing. (clumens)
- Fix the GRUB raid1 tests (dshea)
- Add syslinux to the packages in the gui_testing kickstart file, too.
  (clumens)
- Update the gui_testing kickstart file for productization changes. (clumens)
- Update checkSizes to work in terms of Size objects (#1129629). (clumens)
- Install grub to all disks in a btrfs raid1 /boot (#989644) (dshea)
- Really fix issue with starting in cmdline mode on s390x. (sbueno+anaconda)
- The network spoke's title has changed.  Reflect that in the test. (clumens)
- Grab memory.dat from running the GUI test. (clumens)
- Don't panic prematurely on a missing size (#1154190) (amulhern)
- Fix more messages the new pylint found. (clumens)
- dracut/save-initramfs.sh: don't save /tmp (wwoods)
- Get rid of some unnecessary text from dasdfmt dialog. (sbueno+anaconda)
- Quit if no device type name selected. (amulhern)
- Fix stray comment. (amulhern)
- If there's no attached ANACTEST device, don't attempt to mount and run it.
  (clumens)
- Fix a spelling error (#1153672) (dshea)
- Log when using updates from /tmp/updates/ (bcl)
- Fix # handling in SimpleConfigFile (#1045687) (bcl)
- Unconditionally clear the process handle when nm-c-e exits (#1132645) (dshea)
- Remove the code that reads /tmp/vncshell.pid. (dshea)
- Rewrite _bound_size() to bound_size() in storage_utils.py (amulhern)
- Changes for scheduling size change on an existing device (#1076055)
  (amulhern)
- Remove too strict condition for changing size (#1076055) (amulhern)
- Omit calculation and use of active_dev_type. (amulhern)
- Add a method that extracts device type name from combo box (amulhern)
- Don't pass use_dev around to internal methods. (amulhern)
- Check identity, not equality, for RaidLevel objects. (amulhern)
- Run restorecon on /etc/hostname (#1133368) (bcl)
- Add authconfig and firewalld packages when used in ks (#1147687) (bcl)
- Allow kickstart with no method (#972265) (bcl)
- Fix a typo from 73d3a8e5. (sbueno+anaconda)
- Respect both ways how to disable bootloader installation (vpodzime)
- Fix a bug unmounting /boot on efi+atomic installs. (clumens)
- Refactor handling of fsCombo considerations. (amulhern)
- Be more restrictive displaying btrfs device type. (amulhern)
- Get rid of unnecessary raid_level variable (amulhern)
- Use Size, not int, for size (#1076055) (amulhern)
- Remove an unused import (dshea)
- Don't automatically select environments for kickstart installs (#1018226)
  (dshea)
- Initialize the GUI lock in a way that doesn't break the API (dshea)
- Don't check enabledPlugins if plugins are not yet enabled (#1142544) (dshea)
- Add transifex branch check to makebumpver (bcl)
- Get rid of an unused variable in the localization test. (clumens)
- Don't strip accents from the user-inputted keyboard string (dshea)
- Convert strings to unicode in have_word_match (#1146581) (dshea)
- Use translated versions of the AM/PM strings consistently (vpodzime)
- Import GUI-specific stuff only when running GUI in entropy handling
  (vpodzime)
- Always store the information about display mode in ksdata (vpodzime)
- Connect signals to handlers for day/month/year changes (vpodzime)
- Switch to using the new help content path (#1072033) (mkolman)
- Remove unused variables in the datetime_spoke.py module (vpodzime)
- Add nombr to anaconda to suppress updating MBR (#886502) (gczarcinski)
- Make the date format locale-dependent in our GUI (#1044233) (vpodzime)
- A function for resolving date format and order (vpodzime)
- Make device/fs type comboboxes take less space (vpodzime)
- Skip running efibootmgr for noefi mode (#1047904) (bcl)
- Fix a race between checking for Gtk.main_level and running Gtk.main (dshea)
- Allow recursive lightbox calls (#1147337) (dshea)
- Disable the ntp service with --nontp (#1135768) (dshea)

* Wed Oct 08 2014 Brian C. Lane <bcl@redhat.com> - 22.8-1
- Add a test case for if all anaconda's Requires exist. (clumens)
- Only allow one anaconda instance (#1146735) (dshea)
- Ignore partition start if there is a biosboot partition (#1044849) (bcl)
- Remove duplicates when adding new devices (#887526) (bcl)
- Trim changelog entries from spec file (bcl)
- We now need to specify an epoch for the python-blivet version requires.
  (clumens)
- Remove the last references to tzmapdata (dshea)
- Add VNC to the ostree test arguments. (clumens)
- Fix autotools rules to properly include help placeholders (#1072033)
  (mkolman)
- Ignore an accelerator conflict between two Modify labels. (clumens)
- s390x: show dialog if kernel cmdline in zipl.conf is too long.
  (sbueno+anaconda)
- Convert process watching to use GLib before we start a main loop (dshea)
- Convert python signal handlers to GLib signal handlers (dshea)
- Reorganize the right side of the Custom spoke (#1094856) (vpodzime)
- Graphically handle errors arising from ostree repo pull problems. (clumens)
- Fix file name of the entropy dialog in POTFILES.in (vpodzime)
- Add support for thin pool profile specification in kickstart (vpodzime)
- Require minimum random data entropy when creating LUKS (#1073679) (vpodzime)
- Give blivet callbacks for reporting partitioning progress (vpodzime)
- Really exit when "Exit installer" in the error dialog is clicked (vpodzime)
- NM-wifi is missing on s390(x) (dan)

* Tue Sep 30 2014 Brian C. Lane <bcl@redhat.com> - 22.7-1
- Fix Welcome spoke not showing up during kickstart installation (#1147943)
  (mkolman)
- Don't allow /boot on lvm on s390x. (sbueno+anaconda)
- Handle failures to instantiate storage devices when parsing kickstart.
  (dlehman)
- Add the new langsupport.py TUI spoke to POTFILES.in. (clumens)
- Remove the now-unused imports of storageInitialize. (clumens)
- Add support for language selection in text mode. (sbueno+anaconda)
- packaging: handle new NFS installation source with inst.stage2=nfs:...
  (wwoods)
- Allow cdrom-swapping when doing "inst.ks=cdrom[:...]" (wwoods)
- anaconda-lib.sh: add tell_user() and dev_is_cdrom() (wwoods)
- Don't force a user to return to the storage spoke after dasdfmt
  (sbueno+anaconda)
- Don't run storageInitialize after dasdfmt (sbueno+anaconda)
- Shut up, parallel (dshea)
- Really fix unexpected exits in execReadlines (dshea)
- Add a context manager for executing code while UI signals are blocked.
  (clumens)
- Avoid the possibility of size variables being unset (#1146585) (dshea)
- s390x: Apply disk selection before dasdfmt to preserve data.
  (sbueno+anaconda)
- Fix a bad use of WIFSIGNALED (dshea)
- Handle 0's returned by Gdk (dshea)
- Adapt to corrected interpetation of logvol --percent. (dlehman)
- Always use iutil to start processes. (dshea)
- Move the X startup logic to iutil (dshea)
- Move process watching to iutil. (dshea)
- Close file descriptors while daemonizing auditd (dshea)
- Add an option to only capture stdout with execWithCapture (dshea)
- Simplify iutil.execReadlines. (dshea)
- Add close_fds to the Popen call. (dshea)
- Add an option to startProgram to reset signal handlers. (dshea)
- Add a method startProgram to handle process starting (dshea)
- Lock program_log_lock closer to where the log is written. (dshea)
- Record early crashes to ipmi (dshea)
- Clear the list of watched PIDs before exiting. (dshea)
- Remove the exitCode parameter from exitHandler. (dshea)
- Warn about uses of the string module. (dshea)
- Import _ from the i18n module instead of hand-crafting a copy of it (dshea)
- Import gettext in iutil instead of passing the module reference to iutil
  (dshea)
- Fix a typo in a comment (dshea)
- When running on HiDPI monitors, scale anaconda by a factor of 2 (dshea)
- Sort the contents of the file system type combo box. (clumens)
- Remove the border on the layout testing box. (clumens)
- Explain what the IPMI constants mean. (clumens)
- Don't attempt terminal size detection on the s390 (#1145065) (mkolman)
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
- Preserve network args on s390x. (sbueno+anaconda)

* Fri Sep 19 2014 Brian C. Lane <bcl@redhat.com> - 22.6-1
- Don't call storage.write for dirinstall (#1120206) (bcl)
- Fix pylint warning from a recent commit. (dlehman)
- Fix the link to the help-button-clicked signal (dshea)
- Assign mnemonics to two checkboxes on the user spoke that didn't have them.
  (clumens)
- Remove "MB" from the size string on the HDISO combo box. (clumens)
- Use _Cancel and _Continue mnemonics on these two screens. (clumens)
- Rename to be the TIME & DATE spoke. (clumens)
- Ok -> OK on the proxy dialog. (clumens)
- Handle cancellation of new container creation. (dlehman)
- Reflect previous custom/autopart selection in the storage spoke. (dlehman)
- Clear out custom storage ksdata after first attempt to apply it. (dlehman)
- Pass size as Size when adjusting container after device removal. (#1141707)
  (dlehman)
- Set flags.rescue_mode not anaconda.rescue (#1143056) (amulhern)
- Split localed's converted layouts and variants (#1073825) (vpodzime)
- Rename variable to not with a built-in (mkolman)
- Create free space snapshot before doing custom->autopart (vpodzime)
- Deprecate RUNKS cmdline option. (sbueno+anaconda)
- Show help also when alt+F1 is pressed (mkolman)
- Support display of the custom mnemonics on the help button (mkolman)
- Activate the built-in help when F1 is pressed (mkolman)
- Specify help file names for hubs and spokes (mkolman)
- Add a help button to every Anaconda screen (mkolman)
- Don't call BusyCursor before Gdk is setup (#1078868) (bcl)
- Fix SELINUX_DEFAULT import (#1137049) (bcl)
- Catch and rethrow BTRFSValueError as KickstartException (#1019685) (amulhern)
- Bump version so BTRFSValueError is found (#1019685) (amulhern)
- Don't change langpacks config of installer environment (#1066017) (rvykydal)
- network: fix typo 'Private ksy pasword' (#1120374) (rvykydal)
- Fix up a string style issue found in the last network commits. (clumens)
- network: WPA Enterprise: don't ask twice for password (#1120374) (rvykydal)
- network: add support for WPA Enterprise (#1120374) (rvykydal)
- network: add s390 network ifcfg options also for bond slaves (#1090558)
  (rvykydal)
- network: copy resolv.conf to chroot before installing packages (#1048520)
  (rvykydal)
- network: don't crash, just log for unrecognized bond options (#1039006)
  (rvykydal)
- network: don't traceback on invalid team options (#1114282) (rvykydal)
- network: don't write HWADDR in ifcfgs generated by kickstart (#1130042)
  (rvykydal)
- Re-order the tz's in text mode to mirror the graphical order.
  (sbueno+anaconda)
- Apply a better check for whether to fail if authconfig is missing. (clumens)
- driver-updates: fix backspace/delete in dd menus (#1080380) (wwoods)
- Fix an issue with bad NFS info specified in source spoke. (sbueno+anaconda)
- Fix the SIGSEGV handler (dshea)
- Remove argument handling from methods without arguments (dshea)
- Warn if software selection size exceeds available space. (sbueno+anaconda)
- X doesn't start when making the livecd on the GUI test either. (clumens)
- Handle spaces in inst.repo, kickstart nfs, and url commands (#1109933) (bcl)
- Fix that urllib2 problem more thoroughly. (clumens)
- Fix a problem where urllib2 is not getting pulled into the initrd. (clumens)
- Specify thin pool metadata/chunk size only if given by user (#1140635)
  (vpodzime)
- Fix q for quit issue in text mode (#997405) (sbueno+anaconda)
- Additional message if kickstart was used but did not finish (#1117908)
  (amulhern)
- Move some statically detectable kickstart errors out of anaconda (#1117908)
  (amulhern)
- Use only the digits from productVersion (bcl)
- If a kickstart installation stops because it doesn't know something, log
  that. (clumens)
- Don't care about crash args in bootloader (#1116323) (vpodzime)

* Wed Sep 10 2014 Brian C. Lane <bcl@redhat.com> - 22.5-1
- Fix noselinux cmdline default (#1137049) (bcl)
- Revert productName repo name change (#1128474) (bcl)
- Remove the --disable-overwrite parameter for the Transifex client (mkolman)
- Do not try to disable no firstboot services (#1139621) (vpodzime)
- Snapshot free space after clearpart for swap suggestion (#1132436) (vpodzime)
- Really fix an enlightbox call. (dshea)
- Correct issues merged from rhel-7 (dshea)
- A couple updates to installclasses. (clumens)
- Clear the kickstart password if cleared by the user (#1133185) (dshea)
- Change the accelerator key for Add DASD label. (sbueno+anaconda)
- Add dialog box for adding DASDs. (sbueno+anaconda)
- Add a button for adding an ECKD DASD. (sbueno+anaconda)
- Let finding install classes be more flexible for Fedora (#1138820). (clumens)
- fix inst.virtiolog (#1074499) (wwoods)
- Display container sizes to just two places, as well. (clumens)
- Fix two minor things on the source spoke. (clumens)
- border_width=5 -> border_width=6 in dasdfmt.glade. (clumens)
- Use first part of Product for UEFI entry (#1128474) (bcl)
- We can't pass "text" in the ostree .ks file because lmc doesn't like that.
  (clumens)
- Remove inactive languages from LINGUAS. (dshea)
- Do the ostree test in text mode for now. (clumens)
- Skip nvram update on ppc64 image/dir installations (#1136486) (bcl)
- Use first part of Product as repo name (#1128474) (bcl)
- makeupdates: Report git diff errors (bcl)
- For yum-based installs, move the progress bar while packages are installing.
  (clumens)
- Remove the mnemonics from the custom part toolbar. (clumens)
- Remove references to ia64. (clumens)
- Change a confusing string in TUI NFS configuration screen. (#1057690)
  (sbueno+anaconda)
- Fix two problems with the volume label and combo on custom partitioning.
  (clumens)
- Disable the Modify SW link on livecd installs (#1133726). (clumens)
- Require dmidecode for ARM (#1134651, jdisnard). (clumens)
- Require a larger /boot (#1129629). (clumens)
- Use suggested-action on more buttons (#1131254) (dshea)
- CmdlineError should exit with a 1 (bcl)
- Let gtk determine the allocation for overlays. (dshea)

* Wed Aug 27 2014 Brian C. Lane <bcl@redhat.com> - 22.4-1
- jwb would like us to be clear that bugs could be the system firmware...
  (pjones)
- Fix installing from a second iso (#1040722) (bcl)
- Remove anaconda_make_pixbuf (dshea)
- Trick automake into taking our wildcards (dshea)
- Distribute the right docs files (vpodzime)
- Require anaconda-widgets from anaconda-widgets-devel (dshea)
- Run /sbin/ldconfig when installing or uninstalling anaconda-widgets (dshea)
- Remove the shebang from anaconda.py (dshea)
- Exclude the compiled text and rescue files from anaconda-core (dshea)
- Update our copy of the GPL (dshea)
- Remove unused methods from packaging.Payload (dshea)
- Rearrange the entry, example and tip on Advanced User dialog (vpodzime)
- Change our docs that are close to ReST to proper ReST (vpodzime)
- Remove old outdated docs nobody should read (vpodzime)
- Send run-hub and run-spoke into the great beyond (dshea)
- Use one thread for payload setup. (dshea)
- Remove logging to tty3 and tty5 (#1073336) (bcl)
- Make missing encryption key error message more helpful (#1074441) (amulhern)
- Fix problems with the hdiso method. (clumens)
- Update makebumpver to include flags on first request (bcl)

* Fri Aug 15 2014 Brian C. Lane <bcl@redhat.com> - 22.3-1
- Add some tests for execReadlines (dshea)
- Remove iutil.fork_orphan (dshea)
- Move non-exec tests into a separate class. (dshea)
- Write storage after liveimg install (#1080396) (bcl)
- Add an option to makebumpver to skip all checks. (clumens)
- Write sslverify=0 for url kickstart method (#1116858) (bcl)
- Add noverifyssl and proxy support to dracut ks handling (#1116858) (bcl)
- Log installation successes and failures via ipmitool (#782019). (clumens)
- Default the OK button on the iscsi dialog to insensitive. (clumens)
- Add repo --install support to DNF (#1119867) (bcl)
- Install selected ks repos to target (#1119867) (bcl)
- Add check for the format of grub2 encrypted password (#1070327) (bcl)
- Add some sanity checking to live payload (vpodzime)
- Use blivet's getFreeSpace for limitting automatic swap size (vpodzime)
- Ask users for enough space right at the first time (#876916) (vpodzime)
- Use low level file i/o for rpm callback logging (#1035745) (bcl)
- In tui cmdline mode skip showError and log message (bcl)
- Modify nm to return defaults when no dbus is available (bcl)
- Skip networkInitialize for image and dir installations (bcl)
- Ignore safe_dbus errors in keyboard setup (bcl)
- Skip syslog for dirinstall (bcl)
- Clear out errors at the beginning of _save_right_side. (clumens)
- Filter empty comps groups from both specific and generic lists (dshea)
- Add a test for disadvised words. (dshea)
- Mountpoint encrypted checkbox reflects container state (#1000031) (bcl)
- Display a fatal error if unable to encrypt a password. (dshea)
- Change strings per stylistic advice from ECS (dshea)
- Untranslate the type column of the network device type combobox (dshea)
- Add more information to the custom part summary dialog (#975804). (clumens)
- Don't require user creation when root is locked (#1030626) (bcl)
- Import LUKSDeviceWithoutKeyError from the right place (vpodzime)
- Move _verifyLUKSDevicesHaveKey to Anaconda's codebase (vpodzime)
- Fix issues reported by pyflakes (vpodzime)

* Thu Jul 31 2014 Brian C. Lane <bcl@redhat.com> - 22.2-1
- Return NULL on error in doSetSystemTime. (dshea)
- Remove the /usr/bin/liveinst symlink during uninstall (dshea)
- Highlight languages in langsupport that contain selected locales (dshea)
- Add a wrapper function for GtkTreeViewColumn.set_cell_data_func (dshea)
- Remove the STANDALONE #ifdef from auditd. (dshea)
- Mark zRAM devices as protected and ignore them (vpodzime)
- Make storage sanity check aware of base RAM requirements (#1123466)
  (vpodzime)
- Move sanityCheck code to anaconda's codebase (vpodzime)
- Clean up stylesheet comments (dshea)
- Resurrect auditd (dshea)
- Fix the spacing on the non-verbose doc building messages (dshea)
- Switch to kinder, gentler autoconf errors (dshea)
- Clean up the handling of CFLAGS (dshea)
- Remove unused parts of the configure.ac files. (dshea)
- Add a couple of configure checks from autoscan (dshea)
- Include config.h in every C file. (dshea)
- Use the result from AC_FUNC_FORK at build time (dshea)
- Don't distribute the gnome desktop file with translations (dshea)
- Build documentation during build instead of dist (dshea)
- Do not multiply/divide RAM sizes by 1024 back and forth (vpodzime)
- Raise exception if reading lines from a killed process (vpodzime)
- Use zRAM swap up to 2 GB of RAM (vpodzime)
- RAM requirements depend on squashfs.img's origin (vpodzime)

* Fri Jul 25 2014 Brian C. Lane <bcl@redhat.com> - 22.1-1
- Add platform specific group selection (#884385) (bcl)
- Use parallel instead of xargs (vpodzime)
- Solidify the row separator in the welcome spoke. (dshea)
- Don't skip cpfmtxa formatted dasds if zerombr specified in ks. (#1073982)
  (sbueno+anaconda)
- Fix TUI error message regarding username creation. (#1058637)
  (sbueno+anaconda)
- Determine the lang selected arrow direction at render time (dshea)
- Lessen the visible resize when entering the welcome and lang spokes (dshea)
- Reset the want_x flag after the memory check (vpodzime)
- Fix crash caused by passing kwargs to log functions (vpodzime)
- Check graphical RAM requirements if running graphical installation (vpodzime)
- Document the inst.zram boot option (vpodzime)
- Adapt the memory requirements to zRAM swap usage (vpodzime)
- Remove an unused MEM-related constant and use the other one (vpodzime)
- Add a script for showing stats about zRAM (vpodzime)
- Set widgets to be focused when entering a spoke. (#1121285) (dshea)
- Allow a wider variety of mountpoints (#1109143) (dshea)
- Restrict the selected and insensitive style rules to anaconda widgets (dshea)
- Log more details about collect failure (bcl)
- Prevent crashes due to accessing X server from multiple threads (vpodzime)
- Add vnc to the arguments to qemu for the GUI testing. (clumens)
- Remove a commented out import (mkolman)

* Wed Jul 16 2014 Brian C. Lane <bcl@redhat.com> - 21.48-1
- Fix the custom accelerators in custom partitioning (#1118999) (dshea)
- Revert "Reset dnf package sack" (bcl)
- Ignore the home directory setting if no change was requested (#1119900)
  (dshea)
- Set an upper limit on uids and gids. (dshea)
- Remove the "Create a home directory" checkbox (dshea)
- Fix a typo: inital -> initial (mkolman)
- Don't create the configured.ini file (#1119166) (mkolman)
- zRAM swap for Anaconda (vpodzime)
- Split kickstart arg handling (bcl)
- Update icon names used within python code. (dshea)
- Add a check for whether icons used in glade files are valid (dshea)
- Load icons by name instead of stock-id. (dshea)
- Remove extra list() call with no effect (vpodzime)
- Add NetworkManager-wifi dependency for the GUI subpackage (#1111417)
  (mkolman)
- Python's octals changed; mount's didn't. (pjones)
- Add a basic test for ostree-based installs. (clumens)
- Print out exceptions at log level critical. (clumens)
- Rename environment variables in run_gui_tests.sh. (clumens)
- Rename gui/runtest.sh to fit in with the other test names. (clumens)
- Write the grub config even on errors (#1114774) (bcl)

* Fri Jul 11 2014 Brian C. Lane <bcl@redhat.com> - 21.47-1
- Fix references to requiredPackages (bcl)
- Drop anaconda. prefix from copied logs (bcl)
- dnf should put its logs in /tmp/ (bcl)
- Make sure the software listboxes are shown (bcl)
- dnf should report that it supports Closest Mirror (bcl)
- Do not prefer /tmp for dnf downloads (bcl)
- Reset dnf package sack (bcl)
- Fix dnf base repo setup to fall back to default gracefully (bcl)
- Move addDriverRepo into PackagePayload class (bcl)
- Rename some dnf items to match yum (bcl)
- rpmostreepayload: Drop selinux-ensure-labeled call (walters)
- Run anaconda in fullscreen whenever possible. (dshea)
- Correct the constant used with gtk_widget_set_state_flags (dshea)
- Restore some CSS rules from the pre-3.13 Adwaita theme. (dshea)
- Adapt to changes in blivet.udev interface. (amulhern)
- Bump blivet version to pick up blivet.udev interface changes. (amulhern)
- Use the enlightbox context manager for the add network device dialog
  (mkolman)
- DNFPayload: do not add group 'core' twice. (ales)
- Remove the window property from UIObject. (dshea)
- Unravel the Hub and Spoke classes. (dshea)
- Fix --kickstart option (bcl)
- Bump up the required pykickstart version (vpodzime)
- Use GtkRevealer for widget hiding in storage spoke (mkolman)
- rpmostreepayload: create /var/spool/mail required when adding user (rvykydal)
- rpmostreepayload: Don't recreateInitrds for this payload (walters)
- Don't use geolocation when installing with kickstart (mkolman)

* Wed Jul 02 2014 Brian C. Lane <bcl@redhat.com> - 21.46-1
- Ignore an error from pylint incorrectly analyzing types in dbus-python
  (dshea)
- Remove the Lightbox widget (dshea)
- Implement the lightbox in MainWindow (dshea)
- Added a method to create new GdkPixbufs from in-memory data (dshea)
- Add a delete-event handler for the main window (dshea)
- Add a window to manage Anaconda screen transitions. (dshea)
- Add a class BaseStandalone. (dshea)
- Increased the version of anaconda-widgets to 3.0 (dshea)
- Use globs for the anaconda widgets library paths (dshea)
- Remove the custom accelerators from custom storage. (dshea)
- Add a couple more deprecation warning ignores (dshea)
- Use a dict for string substitutions in a /boot/efi message. (clumens)
- Use the right index for selecting region (#1114234) (vpodzime)
- Add autopart --fstype support (#1112697) (bcl)
- Patches to allow /boot/efi to be RAID1 (#788313) (amulhern)
- Bump blivet version for succeeding commit. (amulhern)
- Map our log levels to syslog log levels (bcl)
- makeupdates: Put systemd files under /usr/lib/ (bcl)
- Make octal literals Python 3 compatible (mkolman)
- Use the built-in next() function for generators (mkolman)
- Make reduce function usage Python 3 compatible (mkolman)
- Use createrepo_c in place of createrepo (mkolman)

* Fri Jun 27 2014 Brian C. Lane <bcl@redhat.com> - 21.45-1
- Switch to tty1 if we get an exception before meh is setup (dshea)
- Remove surprises from X startup. (dshea)
- Import KS_MISSING_IGNORE from pykickstart.constants in DNF payload (mkolman)
- Import Pykickstart constants directly (mkolman)
- Switch error exit codes to 1 (bcl)
- Add help texts for the remaining Anaconda options (mkolman)

* Wed Jun 25 2014 Brian C. Lane <bcl@redhat.com> - 21.44-1
- Fix storage checker docstring (bcl)
- Modify --dirinstall to take a path (bcl)
- Drop ROOT_PATH, add a method to set it (bcl)
- Call setUpBootLoader in custom autopart (#1086811) (bcl)
- Remove the noipv6 Anaconda option (mkolman)
- Remove the -s/--script Anaconda option (mkolman)
- Make rescue_mode part of flags, hence more publicly available (#1090009)
  (amulhern)
- Check host filesystem space for dirinstall (bcl)
- Remove the viewport from the addon repo tree view (dshea)
- Add a check for GtkScrollables contained in GtkViewports (dshea)
- Enable rubber-banding in the disk tree views (dshea)
- Make the configure mount point dialog taller. (#924182) (dshea)
- Add the disk TreeViews directly to the scrolled windows (dshea)
- Opened up custom_storage_helpers.glade and hit Save (dshea)
- Add help texts for more Anaconda CLI options (mkolman)
- Remove the targetarch Anaconda option (mkolman)
- Add anaconda_options.txt to makeupdates (dshea)
- Allow the location of anaconda_options.txt to be overridden (dshea)
- Remove an unused import. (dshea)
- Remove the headless Anaconda option (mkolman)

* Thu Jun 19 2014 Brian C. Lane <bcl@redhat.com> - 21.43-1
- Allow NFS addon repos (#985080) (dshea)
- Add --disklabel support to clearpart (#1078537) (bcl)
- Replace redundant ifs with direct assignments to the anaconda variables
  (mkolman)
- Replace ifs when assigning option values to flags where possible (mkolman)
- Use True/False instead of 1/0 for flags (mkolman)
- Store auto gui results in the same directory as the test itself. (clumens)
- Use whatever network device was used to start installation. (clumens)
- Ignore more deprecation warnings. (dshea)
- Add help texts for the dmraid and nodmraid options (mkolman)
- Use True instead of 1 for the dmraid flag default value (mkolman)
- Add help texts for the ibft and noibft options (mkolman)
- Use True instead of 1 for the ibft flag default value (mkolman)
- Remove the iscsi and noiscsi options (mkolman)
- Add a new log level 'lock' for _yum_lock (bcl)
- Replace uses of gtk-missing-image (dshea)
- Improve the SpokeSelector icon error reporting. (dshea)

* Thu Jun 12 2014 Brian C. Lane <bcl@redhat.com> - 21.42-1
- Adjust the ui package paths to find hubs and spokes (bcl)
- Change emphasis from subvolumes to snapshots in removal warning. (dlehman)
- Reflect the fact that some block devices cannot be reformatted. (dlehman)
- Use StorageDevice.direct to detemine if a device is directly accessible.
  (dlehman)

* Wed Jun 11 2014 Brian C. Lane <bcl@redhat.com> - 21.41-1
- Use /usr/lib* in updates images. (dshea)
- Fix the paths we check for spokes. (sbueno+anaconda)
- Remove the kbdtype option (mkolman)
- Remove the noipv4 option (mkolman)
- Remove the autostep option (mkolman)
- Remove the disused nofb option (mkolman)
- Remove the module option (mkolman)

* Tue Jun 10 2014 Brian C. Lane <bcl@redhat.com> - 21.40-1
- fedora-welcome: Correct an icon name after the switch to Adwaita
  (kalevlember)
- Pass/check displaymode in collect_categories and collectCategoriesAndSpokes.
  (sbueno+anaconda)
- Add help texts to some Anaconda CLI options (mkolman)
- Don't install implicitly added but explicitly excluded packages (#1105013)
  (vpodzime)
- Update configure, make files, and PO files with new category changes.
  (sbueno+anaconda)
- Fix up collectCategoriesAndSpokes function. (sbueno+anaconda)
- Update all relevant UI files with new category path. (sbueno+anaconda)
- Move categories to pyanaconda.ui.categories. (sbueno+anaconda)
- Allow testing a regular install from the live environment. (clumens)
- Make sure /var/log/anaconda gets copied under the right root. (clumens)
- format.setup in blivet takes only kwargs. (clumens)
- Tweak spacing in the other storage options grid. (clumens)
- Remove the dlable option (mkolman)
- change default for grub2 save_entry to 0 (gczarcinski)
- Revert "Refresh after checkbox clicked (#1074188)" (dshea)
- Move assureLogoImage to GraphicalUserInterface (#1102238) (dshea)
- If we cannot activate keyboard, at least populate the missing items
  (#1104541) (vpodzime)
- network: generate dracut arguments also for IPADDRn ifcfg values (#1103571)
  (rvykydal)
- Memoize the results for *RaidLevelsSupported() functions (amulhern)
- RAID related changes for custom spoke. (amulhern)
- Bump required blivet version. (amulhern)
- Make parse-kickstart aware of the %%addon section (#1083002) (vpodzime)
- Revert "Work around a parsing bug in GtkBuilder" (dshea)
- Fix a typo in one of the bootloader installation warning messages (#1103410)
  (mkolman)
- Don't require network in standalone spoke for media installs (#1066807)
  (rvykydal)

* Mon Jun 02 2014 Brian C. Lane <bcl@redhat.com> - 21.39-1
- eu_ES has been dropped from the supported languages (bcl)
- Change 'elif encrypted' statement to 'else' statement. (amulhern)
- Work around a parsing bug in GtkBuilder (dshea)
- Don't uppercase the size values in the disk shopping cart. (clumens)
- Display the sentence about being able to reuse partitions even without roots.
  (clumens)
- Allow a couple more keyboard shortcuts on the custom part spoke. (clumens)
- Reword the close button on the software spoke's error dialog. (clumens)
- Fix up quoting around passing args to anaconda in the gui test. (clumens)
- Don't hide a serious issue (vpodzime)
- Move autopart choices to one place and use them in both GUI and TUI
  (vpodzime)
- Define default autopart type as a constant (vpodzime)
- Use enumerate() instead of getting indices of iterated items (vpodzime)
- Preserve net.ifnames cmdline arg (#1102401) (bcl)
- Revert the dialog sizing chunk from resize.glade. (clumens)
- Update GUI tests for changes in gtk/atk/anaconda/whatever. (clumens)
- Fix gui/runtest.sh to work under either "make check" or being run manually.
  (clumens)
- Add a -c argument to the ksflatten invocation. (clumens)
- Do basic logging setup when short circuiting the normal Anaconda init
  (mkolman)
- Fix boot option warning string formatting (mkolman)
- always rescan for vmlinuz if rescueKernelList (gczarcinski)
- move new-kernel-pkg rpmposttrans to end of install (gczarcinski)
- allow /boot on btrfs subvol or filesystem (gczarcinski)
- Allow /boot on LVMlv (gczarcinski)

* Wed May 28 2014 Brian C. Lane <bcl@redhat.com> - 21.38-1
- Parse boot options before parsing CLI options (#1101341) (mkolman)
- Check that bootloader devices are configured before validating (#1100928)
  (dshea)
- network: use IpInterface only for activated devices (#1101781) (rvykydal)
- Enable LVM Thin Provisioning in text mode (vpodzime)
- Remove the executable bit from anaconda.spec.in. (clumens)
- Fix the nm test for big-endian results (dshea)
- Fix issues with auto* and version.py (dshea)
- Allow file:// url handler in --repo arg (bcl)
- Ignore deprecation warnings for atk_role_register (dshea)
- Handle renames in makeupdates. (pjones)
- Move Anaconda version detection from isys to Python code (mkolman)
- network: use IpInterface instead of Interface (#1058906, #1029214) (rvykydal)
- network: don't modify network config for dirInstall and imageInstall
  (rvykydal)
- network: remove redundant image install guard (rvykydal)
- network: add first tests for nm.py (rvykydal)
- network: consolidate setNetworkOnbootDefault (rvykydal)
- Set ONBOOT=yes for the device used for installation (#1002544). (rvykydal)
- Use proper data for autopart type initialization (vpodzime)
- Line up the right side of the FCOE dialog. (clumens)
- Use default_width and _height on dialogs instead of _request. (clumens)
- Remove the border around the refresh storage dialog's button. (clumens)
- Short-circuit initialization when printing out Anaconda version (mkolman)
- Make print statements Python 3 compatible (mkolman)
- Fix the handling of set_const options pulled in from the boot cmdline (dshea)
- Fix the modify software tooltip on the installation options dialogs.
  (clumens)
- Better visually distinguish TUI spokes states (vpodzime)
- Reset the text direction as soon as the locale is changed (dshea)
- Show errors from the displayed mountpoint when exiting the custom spoke
  (dshea)
- Check that container names input by the user are valid (dshea)

* Tue May 20 2014 Brian C. Lane <bcl@redhat.com> - 21.37-1
- Chain up to parent size_allocate functions in our standalone widgets.
  (clumens)
- Format the help text to properly fit to the terminal window (mkolman)
- Call getPossiblePhysicalExtents() only once (vpodzime)
- Default PE size to blivet's default when requested from kickstart (#1098139)
  (vpodzime)
- A couple of anaconda whitespace fixes (mkolman)
- Replace the deprecated has_key() by in (mkolman)
- Disable pylint errors on NetworkData in the new network_test.py. (clumens)
- Tweak borders on the filter UI. (clumens)
- network: add tests (rvykydal)
- network: don't use ifcfg PREFIX when generating ipv6 dracut args (rvykydal)
- network: cleanup - remove ksdevice variable (rvykydal)
- Horizontally center the user creation spoke contents. (clumens)
- Un-indent the reclaim space checkbox. (clumens)
- Remove the RAID page from the filter UI. (clumens)
- install -> installation in a string on the source spoke. (clumens)
- Switch Anaconda to argparse (mkolman)
- rpmostreepayload: Use systemd-tmpfiles rather than handrolling mkdir
  (walters)
- Add some padding to the custom partitioning note. (dshea)
- Wrap the custom partitioning note (#1031850) (dshea)
- Make an ostree string easier for translators to deal with. (clumens)
- Fix the gettext warnings test for VPATH builds (dshea)
- network: fix crash on empty ksdevice boot option (#1096846) (rvykydal)
- Add RPMOSTreePayload (walters)
- bootloader: Allow extlinux loader configuration to handle RPMOSTreePayload
  case (walters)
- install: Handle distinct physical root/sysroot (walters)
- parse-kickstart: drop "mtu=" args (wwoods)
- Drop workaround for old dracut BOOTIF+ip problem (wwoods)
- Fix behavior (and docs) for ks=nfs:<path>/ (#1094645) (wwoods)
- Allow non-ASCII characters in passwords (#960837) (dshea)
- Use a separate label for passphrase warnings. (dshea)
- Move more of the passphrase dialog into the glade file. (dshea)
- Don't add redundant grub installs if stage1 is not a disk (dshea)
- Let the user continue on bootloader errors (#1006304) (bcl)
- Fix the parsing of NFS addon URLs (#966240) (dshea)
- Remove redundant import (mkolman)
- Don't overwrite function argument when parsing help texts (mkolman)
- Return CLI help text at once (mkolman)
- Fix typo in previous commit adjusting to blivet API change. (dlehman)
- Adjust for movement of functions from examples into blivet proper. (dlehman)

* Thu May 08 2014 Brian C. Lane <bcl@redhat.com> - 21.36-1
- Switch to adwaita-icon-theme (kalevlember)
- Hook up the TUI categories to autoconf/make. (#1095220) (dshea)
- Fix the object type specifying argument name for findActions (vpodzime)
- Remove keyword args 'ignoreErrors' from umountFilesystems() call. (amulhern)
- Updates for new blivet.size.Size.__new__ interface. (amulhern)
- Change uses of 'format' keyword param to 'fmt' keyword param (amulhern)
- Update devicetree.findActions invocations to match blivet interface change
  (amulhern)
- Bump blivet version to ensure next four patches get the right interface.
  (amulhern)

* Mon May 05 2014 Brian C. Lane <bcl@redhat.com> - 21.35-1
- Use format strings in the new kickstart error message translations. (clumens)
- Mark kickstart errors as translatable, and hopefully make them more useful
  too. (clumens)
- install: Move Payload postInstall() after bootloader (walters)
- iutil: Transparently redirect anyone who asks root=/mnt/sysimage to sysroot
  (walters)
- Fix the way categories are handled in text mode. (sbueno+anaconda)
- Move GUI-specific helper classes to a separate module (#1091542) (dshea)
- Fix license in parse-kickstart (mkolman)
- main: Set flags.extlinux if extlinux is used in interactive-defaults.ks
  (walters)
- anaconda.service: Set GIO_USE_VFS=local (walters)
- Use a gettext context where necessary when retranslating (#1091207) (dshea)
- Update makebumpver for python-bugzilla 1.0.0 (bcl)
- Skip source and software spoke in text live installations (#1092763) (bcl)
- Add correct kernel params if rootfs is btrfs on s390x. (#874622)
  (sbueno+anaconda)
- Don't crash on anaconda-yum output containing multiple colons (#1092441)
  (mkolman)
- Revert chrooting when setting user/root password (vpodzime)
- network: fix device configuration in text mode (#1058336) (rvykydal)
- Change order in which packages/groups are selected/excluded (#1091952)
  (vpodzime)
- Check the correct button when saving changes in the Custom spoke (#1090786)
  (vpodzime)
- Fix unloading modules in driver-updates (#1085099) (wwoods)
- Re-saved some of the glade files with a newer version of glade. (dshea)
- Add viewports for the ListBoxes in the software spoke. (dshea)
- Extend format string checks to translated format strings. (dshea)
- Fix typo in nm_is_connected method check. (rvykydal)
- iutil: Introduce getSysroot()/getTargetPhysicalRoot(), use instead of
  ROOT_PATH (walters)

* Thu Apr 24 2014 Brian C. Lane <bcl@redhat.com> - 21.34-1
- Improve the "adding yum repo" message structure (mkolman)
- Fix missing log message about adding a repository (#1089297) (mkolman)
- Ignore use of eval warnings. (dshea)
- Specify string format arguments as logging function parameters (dshea)
- New encrypted state is the dialog's encrypted attribute (vpodzime)
- Use human readable sizes with two decimal spaces in the GUI (vpodzime)
- Make the LUKS unlock callback a timed action (vpodzime)
- Hitting ENTER in the LUKS passwd entry should click the Unlock button
  (vpodzime)
- Block leaf device encryption if container is encrypted consistently
  (vpodzime)
- Do not remove the replacing item, remove the replaced one instead (vpodzime)
- Give include_btrfs variable a better name (vpodzime)
- Make the _resolve_btrfs_restrictions method's code nicer (vpodzime)
- Refactor the btrfs magic into a separate method (vpodzime)
- Switch the condition in long if-else statement (vpodzime)
- Give an opaque condition a better name explaining its real meaning (vpodzime)
- Refactor out the code for removing empty parents (vpodzime)
- Use the (vpodzime)
- Refactor out the code for adding device/mountpoint into a method (vpodzime)
- Relabel /home partition if using and existing one (#1087736) (vpodzime)
- Don't forget to call os._exit() in the child process (vpodzime)
- users: Add root= keyword argument to set{User,Root}Password (walters)
- users: Deduplicate code to fork()+chroot() (walters)
- gui/spokes/software: Enable iff payload is PackagePayload (walters)
- Use descriptive pylint messages instead of numbers. (clumens)
- Add input validation to the source spoke. (dshea)
- Remove the tests for duplicate and invalid repo names (dshea)
- Expand the proxy URL validation. (dshea)
- Convert the repository name test into a regex (dshea)
- Add a remove_check method for InputCheckHandler. (dshea)
- Use ID columns in the protocol combo boxes (dshea)
- Added a link to a bug about the user data in glade problem. (dshea)
- Remove the top and bottom padding from source spoke action area (dshea)
- Re-add a false-positive for the GLib module (dshea)

* Thu Apr 17 2014 Brian C. Lane <bcl@redhat.com> - 21.33-1
- Add an option to copy translation files to an updates.img (dshea)
- Set the selinux state from the command line (#784828) (dshea)
- Remove a whole bunch of pylint false positives (dshea)
- Ignore more informational messages printed by pylint pragmas (dshea)
- Use more wildcards in the tests dist_ variable (dshea)
- Make sure the idx variable is used instead of the old found variable
  (vpodzime)
- Disable a false positive from pylint (dshea)
- Only run dialogs in the enlightbox context (vpodzime)
- Separate code for finding item in containers combo and processing it
  (vpodzime)
- Check Update Settings button sensitivity when saving changes in one place
  (vpodzime)
- Only save changes if needed when adding mountpoint (vpodzime)
- No need to call bool() on a boolean expression result (vpodzime)
- Give names to some magic tuples, make them reusable and reuse them (vpodzime)
- Add DEVICE_TYPE_DISK's text description to the mapping (vpodzime)
- Move a few constants and mappings to the storage_utils module (vpodzime)
- Split long label's string into two lines (vpodzime)
- Don't rely on the ordering of autopart types in the combobox (vpodzime)
- Only save changes if there are any changes to be saved (vpodzime)
- Add device type constants to the device type combobox's store (vpodzime)
- Change some anaconda-yum DEBUGs to be more informative (bcl)
- Change Proxy Add Button to Ok (bcl)
- Display a message for missing required packages and groups (#1064565) (dshea)
- Fix issues with the errorHandler callback arguments (dshea)

* Thu Apr 10 2014 Brian C. Lane <bcl@redhat.com> - 21.32-1
- Refactor the code setting up the device type combobox a method (vpodzime)
- Rename 'swap' variable to 'is_swap' to better express its meaning (vpodzime)
- Refactor out the code setting up the fstype combobox into a method (vpodzime)
- Refactor the code updating info about device container into a method
  (vpodzime)
- Remove the default None value from the addPage's cb argument (vpodzime)
- Make on_updates_settings_clicked timed callback (vpodzime)
- Rename the callback for updating mountpoint settings (vpodzime)
- Hook up the GUI test so it's run as part of "make check". (clumens)
- Skip running pylint on files containing "skip-file". (clumens)
- Add comments to the kickstart tests. (clumens)
- Add the beginnings of an automated GUI test suite. (clumens)
- Add accessibility information to the user spoke. (clumens)
- Add accessibility information to the root password spoke. (clumens)
- Add accessibility information to the progress hub. (clumens)
- Add accessibility information to most of the widgets on the storage spoke.
  (clumens)
- Add enough accessibility information to the network spoke for livecds.
  (clumens)
- Add accessibility information to the keyboard spoke. (clumens)
- Add accessibility information to the date & time spoke. (clumens)
- Add a script and base kickstart file for making a dogtail-enabled livecd.
  (clumens)
- Add accessibility information to the welcome spoke and summary hub. (clumens)
- Add accessibility information to some of our widgets. (clumens)
- Don't use dhcp ntpservers for dir or image installation (bcl)
- Implement and use decorator for logging UI storage actions (vpodzime)
- Refactor out the code doing device reformat into a function (vpodzime)
- Refactor out the code handling encryption change into a function (vpodzime)
- Fix variable name when logging new fstype (vpodzime)
- Make it possible to override translation domain in GUIObjects (#1040240)
  (mkolman)
- Refactor out the code for handling device size change into a function
  (vpodzime)
- Refactor out the code for bounding size into a function (vpodzime)
- Refactor code for reverting device reformat into a function (vpodzime)
- Make the code changing an existing device more compact (vpodzime)
- Comment the part of the code changing an existing device (vpodzime)
- Do device change logging in one place where possible (vpodzime)
- Pass information about old and new device as a dictionary (vpodzime)
- Move code attempting to replace device into a separate function (vpodzime)
- Mountpoint validation should only care about the new fs type (vpodzime)
- Make size properties refreshing reused code (vpodzime)
- Use generator instead of list for auxiliary old_disk_names variable
  (vpodzime)
- Remove and unused variable in Custom spoke (vpodzime)
- Refactor mountpoint configuration validation out from _save_right_side
  (vpodzime)
- Don't overload selectorFromDevice function (vpodzime)
- Use dir_tree_map for the cleanPStore function (vpodzime)
- Check xconfig before setting the installed displaymode (dshea)
- DNFPayload: call close() when done with the Base. (ales)
- Do not try to get "" translated (vpodzime)
- Use for-cycle else: branch instead of extra variable (vpodzime)
- Have mountpoint descriptions defined in a dictionary (vpodzime)
- Uppercase global constants in the Custom spoke (vpodzime)
- Use cannonical RAID level names when populating RAID stores (vpodzime)
- No RAID level (RAID level None) is a valid choice for LVM(ThP) (vpodzime)
- LVM Thin Provisioning supports the same RAID levels as plain LVM (vpodzime)
- Only block the password/user spokes if data was given in kickstart (vpodzime)
- Disable a pylint error message for now. (clumens)
- Suppress selinux error log when using default (#1083239) (bcl)
- Use the AnacondaWidgets python gi-overrides for pylint (dshea)

* Wed Apr 02 2014 Brian C. Lane <bcl@redhat.com> - 21.31-1
- Only install consolehelper link on livearches (bcl)

* Wed Apr 02 2014 Brian C. Lane <bcl@redhat.com> - 21.30-1
- Add support ppc64le (hamzy)
- Validate proxy URLs (dshea)
- Provide feedback for invalid NTP hostnames. (dshea)
- Use GUIDialogInputCheckHandler in the advanced user dialog (dshea)
- Add a new InputCheck status for silent failures. (dshea)
- Add an InputCheckHandler subclass for dialogs. (dshea)
- Generalized and improved the proxy URL parsing regex (dshea)
- Update makebumpver for the newer python-bugzilla on rawhide. (clumens)
- network: don't crash on virtual devices turned off (#1080640) (rvykydal)
- network: don't pop HWADDR twice for vlan on s390 (#1061646) (rvykydal)
- Make safe_dbus module's functions less 'safe' (vpodzime)
- Add a list of cmdline args that append instead of replace (#1073130) (bcl)
- safe_dbus: Don't export DBus connection addresses as variables (walters)

* Wed Mar 26 2014 Brian C. Lane <bcl@redhat.com> - 21.29-1
- Add a Makefile target to create a set of empty .po files. (dshea)
- os.path.exists -> os.path.lexists when checking for authconfig. (clumens)
- Add support for tarfiles to liveimg kickstart command (bcl)
- mountExistingSystem raises an exception with dirty FS (#1080210) (vpodzime)
- Don't do yum lock logging when using updates.img (vpodzime)
- Pass Size(0) instead of 0 to the ContainerDialog if no size is given
  (vpodzime)
- Update the BaseWindow and HubWindow example UI fragments (dshea)
- Convert GtkHBox and GtkVBox to GtkBox. (dshea)
- Fix keyboard accelerator collisions from former stock buttons (dshea)
- Set the secret agent icon in the glade file (dshea)
- Remove stock labels and icons. (dshea)
- Run the pykickstart version test on the commands in parse-dracut (dshea)
- Don't reimport os - it's imported very early on. (clumens)
- Use an alternative image if logo is missing (mkolman)
- Update parse-kickstart for the new bootloader command. (clumens)
- Make sure the error info message starts on a new line (vpodzime)
- Define two env variables removing useless warnings (vpodzime)
- Check boot args for None (#1075918) (bcl)
- Revert "Enable make check in %%check and add the necessary BuildRequires"
  (dshea)
- Fix the argument list passed to the payloadInitialize thread (#1079628)
  (dshea)
- Fix filtering the _storage_playground out (vpodzime)
- Sync up step counts in install.py with reality. (clumens)
- Avoid the "unable to init server" message. (dshea)
- Do not attempt to run authconfig if it doesn't exist. (clumens)
- Allow skipping installation of the core group, if asked for in kickstart.
  (clumens)
- Drop the vconsole.font boot arg (#1074113) (vpodzime)

* Thu Mar 20 2014 Brian C. Lane <bcl@redhat.com> - 21.28-1
- Get the DBus session bus address in a method (dshea)
- Specify string format arguments as logging function parameters (dshea)
- Inhibit the screen saver on live installs (#928825) (dshea)
- Handle the dbus method call not returning anything. (dshea)
- Convert errors raised during dbus connection to DBusCallError (dshea)
- driverdisk: Show selection menu for network driver isos (#1075918) (bcl)
- Write a modprobe blacklist (#1073130) (bcl)
- Append cmdline arg values in BootArgs (#1073130) (bcl)
- Wait for other threads to finish before sending ready (#1075103) (bcl)
- set proxy related environmental variables (#854029) (bcl)
- Fix pylint error in yumpayload. (sbueno+anaconda)
- The custom spoke requires mountPointStore and mountPointCompletion, too.
  (clumens)
- Make the lists of files to check consistent across all checks. (dshea)
- Fix error handling in cmdline mode. (#1034773) (sbueno+anaconda)
- Don't create bootloader entries for kdump initrd and kernel. (#1036086)
  (sbueno+anaconda)
- Add a setting to network.py that got left out of the cherry-pick. (clumens)
- Enable make check in %%check and add the necessary BuildRequires (atodorov)
- Make it obvious user is going to begin installation. (#975793)
  (sbueno+anaconda)
- Move libtimezonemap requires to the anaconda-gui subpackage (vpodzime)
- network: apply ks configuration to devices activated in initramfs (#1037605)
  (rvykydal)
- Add support for kickstart --interfacename for vlans (#1061646) (rvykydal)
- network: handle race condition of disappearing active connection (#1073424)
  (rvykydal)
- Convert iter from filter model iter to backing store iter (#1074188)
  (amulhern)
- Provide ways in kickstart to skip kernel and bootloader (#1074522). (clumens)
- DNFPayload: apply the kickstart excludedList. (ales)
- Only pylint files that are in the git working copy (dshea)
- Move accordion population into a separate function (vpodzime)
- Short-circuit testing if root has any devices (vpodzime)
- Getting new devices is not enough cheap operation for being a property
  (vpodzime)
- Hide and unhide the same set of disks in the Custom spoke (vpodzime)
- Use GtkActionList when populating filesystem store (vpodzime)
- Fix XDG_RUNTIME_DIR not set messages by creating one (dshea)
- Make the ui_storage_logger reusable (vpodzime)
- Decide on supported RAID levels in a better way (vpodzime)
- Fix typo in the comment (vpodzime)
- Add and use MountpointSelector's attributes we need (vpodzime)
- Make code to get Size instance from user's input reusable (vpodzime)
- Make getting raid level less hacky (vpodzime)
- Implement a function to get container type name (vpodzime)
- Make custom partitioning helper constants look as constants (vpodzime)
- Simplify mountpoint validation and error reporting (vpodzime)
- Simplify label validation and error reporting (vpodzime)
- Move translated_new_install_name to the right place (vpodzime)
- Rename the __storage attribute to a more propriate name (vpodzime)
- Split out helper code from the Custom partitioning spoke (vpodzime)
- The reset button should only be sensitive if there's something to reset.
  (clumens)
- Confirm before resetting custom partitioning selections (#970093). (clumens)
- DNFPayload: Add languageGroups(). (ales)
- Use ROOT_PATH not /mnt/sysimage (bcl)
- Override ROOT_PATH with environmental variable (bcl)
- Import /etc/login.defs in libuser.conf (#979815) (dshea)
- Fix environment group changes based on ListBox row activation (dshea)
- DNFPayload: do not crash when an addon is unavailable. (ales)
- Payloads: make DEFAULT_REPOS a part of the interface. (ales)

* Tue Mar 11 2014 Brian C. Lane <bcl@redhat.com> - 21.27-1
- Don't disable anaconda repo on rawhide (bcl)
- Set log level to debug when using an updates image (bcl)
- driver-updates: accept burned driver discs (#1073719) (wwoods)
- Do nothing if previously selected selector gets focus again (#1029798)
  (vpodzime)
- Firstboot is deprecated and gone on Fedora 20 and anything newer (vpodzime)
- Reraise the exception properly (vpodzime)
- Set progress bar to 100 %% in a different way (#1058755) (vpodzime)
- Refresh after checkbox clicked (#1074188) (amulhern)
- Use instclass.efi_dir when constructing the EFI path (dshea)
- Add rescue kernels to the bootloader install list. (#1036349) (dshea)
- Cover both possible ways that GUI WWID may have been set (#1074184)
  (amulhern)
- Do not write out /etc/adjtime file on s390(x) (#1070748) (vpodzime)
- Ignore the data model and just return self.environment (mkolman)
- Software spoke can't be complete if the payload thread is running (mkolman)
- DNFPayload: blivet.size.Size() only knows 'spec' kwarg now. (ales)
- Specify string format arguments as logging function parameters (dshea)
- Add missing changelog entries (bcl)

* Fri Mar 07 2014 Brian C. Lane <bcl@redhat.com> - 21.26-1
- Don't traceback, just log a warning if connection is unavailable (#1070928)
  (mkolman)
- Remove unnecessary use_markup attributes. (dshea)
- Add a check for unnecessary markup. (dshea)
- Ignore the server keymap for spoke status if using VNC (#1045115) (dshea)
- Call % outside of the translation (dshea)
- Fix pylint errors about dangerous default values (dshea)
- Typo fix (dshea)
- driver-updates: skip iso selection with OEMDRV (#1066784) (bcl)
- driver-updates: allow interactive mode to load multiple devices (wwoods)
- driver-updates: add DoRefresh loop to select_iso() (#1066784) (wwoods)
- driver-updates: add 'refresh' to selection_menu() (wwoods)
- driver-updates: rework 'dd_finished' handling (wwoods)
- driver-updates: refactor dd_scan (wwoods)
- driver-updates: refactor menu to allow other options (wwoods)
- Bump blivet Requires for DASD changes. (#1064423) (sbueno+anaconda)
- Add GUI and TUI logic to handle unformatted DASDs. (#1064423)
  (sbueno+anaconda)
- Show unformatted DASDs in the local disk store. (#1064423) (sbueno+anaconda)
- Add dialog box to warn about formatting DASDs. (#1064423) (sbueno+anaconda)
- Update disk refs when recovering from a devicefactory failure. (#1032141)
  (dlehman)
- Add typelib and library paths to the test environment. (dshea)
- Run pylint with NO_AT_BRIDGE=1 set in the environment (dshea)
- pylint: Clean up accordion warnings (bcl)
- Let Gtk pick the size for the isoChooserDialog (#973376) (dshea)
- network kickstart: do not bind to MAC if SUBCHANNELS are present (#1070232)
  (rvykydal)

* Fri Feb 28 2014 Brian C. Lane <bcl@redhat.com> - 21.25-1
- pylint: Add a pile of new E1101 exceptions (bcl)
- pylint: change disable-msg to disable (bcl)
- Fix console for s390 and 'noshell' mode (#1070672) (wwoods)
- Check that the addon selection state exists before reading it (dshea)
- Set the name in the volume group store (dshea)
- Don't ignore the directory of the driver disk iso file (vpodzime)
- Set rpm macros in DNFPayload (dshea)
- Implement %%packages --instLangs (#156477) (dshea)
- Set rpm macro information in anaconda-yum. (dshea)
- Move the anaconda-yum exception handler (#1057120) (dshea)
- Only run gtk actions in the gtk thread. (dshea)
- Add createrepo Requires (#1016004) (bcl)
- Fix a traceback gathering free space info for a container. (#1069854)
  (dlehman)
- network: detect also fcoe vlan device names exceeding IFNAMESIZ (#1051268)
  (rvykydal)
- DNFPayload: display the download progress on the hub. (ales)
- driverdisk: Fix typo in error logging (#1016004) (bcl)
- driverdisk: Create a repo for network drivers (#1016004) (bcl)
- driverdisk: Catch blkid failure (#1036765) (bcl)
- driverdisk: Ignore extra blkid fields (#1036765) (bcl)
- We can't trust rhcrashkernel-param to give us newline-free text. (pjones)
- Remove redundant _setCurrentFreeSpace() call (#1043763) (amulhern)
- Enable python-coverage in anaconda (dshea)
- Move the sidebar to the right for RTL languages (dshea)
- Remove a bunch of unused includes and tests for headers (dshea)
- Add a note about when and how to remove isys.sync (dshea)
- Remove isys.isPseudoTTY (dshea)
- Convert isys.isIsoImage to python code (dshea)
- Focus the language search input by default (#973967) (dshea)
- Ensure media being verified is always unmounted (dshea)
- Write 'text'/'cmdline' in anaconda-ks.cfg in text/cmdline mode (wwoods)
- text install -> text system (#1021963) (wwoods)
- Support the 'skipx' kickstart command (wwoods)
- let systemd decide when to start anaconda-sshd (wwoods)
- Don't use tmux for inst.noshell (#1058607) (wwoods)
- Fix a nitpick from bcl. (pjones)
- Make rhcrashkernel-param get run on non-GRUB 2 platforms. (pjones)
- Cast the blame appropriately when the kernel refuses efivars changes.
  (pjones)
- Do not use shim.efi on ARMv8 aarch64 (#1067758) (dmarlin)
- Handle missing environments specified through kickstart (#1067492). (clumens)
- create_sparse_file in blivet now expects a Size object. (clumens)
- Don't traceback when no size is given in kickstart (#1067707). (clumens)

* Fri Feb 21 2014 Brian C. Lane <bcl@redhat.com> - 21.24-1
- setup default environment in initialize (bcl)
- Move environmentAddons into packaging (bcl)
- Skip running efibootmgr for image and dir installations (#1067749) (bcl)
- Move translatable format strings into python. (dshea)
- Added a check for translatable format strings in glade. (dshea)
- Use a single script to run the glade tests. (dshea)
- Check that s390x LVM configuration is valid. (#873135, 885011)
  (sbueno+anaconda)
- Re-apply disk selection on error in TUI storage. (#1056316) (sbueno+anaconda)
- Properly retry package downloads (#924860) (mkolman)
- Change the CSS class name of the sidebar (#1067049). (clumens)
- Preserve ipv6.disable=1 on target system (#1040751) (wwoods)
- Remove an unused import in driver-updates. (clumens)
- Fix heredoc usage in generated /etc/grub.d/01_users (#1044404). (dcantrell)

* Tue Feb 18 2014 Brian C. Lane <bcl@redhat.com> - 21.23-1
- driverdisk: Parse all blkid output (#857248) (bcl)
- Fix blkid output parsing and our output (vpodzime)
- Don't use positional arguments to initialize Gtk objects (dshea)
- Set mandatory property in network tui spoke. (#1064139) (sbueno+anaconda)
- Disallow /boot on RAID on s390x. (#1027670) (sbueno+anaconda)
- Remove a stray break statement (dshea)
- Use devicetree.resolveDevice instead of udev_resolve_devspec. (#1047338)
  (dlehman)
- Set ThreadManager.any_errors to be a property (dshea)
- Error on "bootloader --location=partition" when using grub2 (#969095).
  (clumens)
- Fix the handling of kernel parameters with no = (#1065704) (dshea)
- Deal with a couple more "except Exception" lines. (clumens)
- Fix pylint errors in the latest dnf-related commit. (clumens)
- DNFPayload: pick the right FS as package download target. (ales)
- DNFPayload: log import crashes. (ales)
- DNFPayload: use dnf.exceptions.MarkingError. (ales)
- Return the returned value in the fire_gtk_action (vpodzime)
- Allow AddonData classes to parse options in the %%addon line (dshea)
- Pass ints to Gtk resize functions (#1065021) (bcl)

* Fri Feb 14 2014 Brian C. Lane <bcl@redhat.com> - 21.22-1
- Remove app_paintable from a couple nav boxes (#1064708). (clumens)
- Give a more correct error for missing groups/packages on exclude (#1060194).
  (clumens)
- Fix some incorrect RPM macros in the spec file. (clumens)
- Allow using globs and alternative paths for specifying boot drive (#1057282).
  (clumens)
- Don't reset input check status when disabling a check (#1062273) (dshea)
- Fix how an input check is disabled (#1062275). (dshea)
- ListStore.remove expects an iter, not an int (#1062752). (clumens)

* Tue Feb 11 2014 Brian C. Lane <bcl@redhat.com> - 21.21-1
- Move save_netinfo into a hook (#1048231) (bcl)
- Cleanup log message for pylint (bcl)
- kickstart user accounts should be locked by default (#1063554) (bcl)
- pre-push hook checking bugzilla IDs on rhelX branches (vpodzime)
- Make sure LUKS devices can say they have a key (#1060255) (amulhern)
- Handle LUKS passphrase before doing sanity check (#1060255) (amulhern)
- Remove some unnecessary resets (#1060255) (amulhern)
- Do not consider no available LUKS passphrase an error in do_autopart
  (#1060255) (amulhern)
- Adapt to new blivet.sanityCheck() return type (#1060255) (amulhern)
- Adapt StorageChecker class for changed return type of sanityCheck (#1060255)
  (amulhern)
- Add sanityCheck functionality back into AutoPart.execute() (#1060255)
  (amulhern)
- Bump blivet version for changed sanityCheck() interface (amulhern)
- UnmanagedDeviceError and UnknownConnectionError are in the nm module.
  (clumens)
- blivet no longer has a protectedDevices property. (clumens)
- network: adapt to changed handling of devices without carrier in NM
  (#1062417) (rvykydal)
- driverdisk: Rename skip_dds to make pylint happy (bcl)
- driverdisk: Use a single systemd service to start DD UI (#1035663) (bcl)
- driverdisk: Add dd_args_ks handling to driver-updates (#1035663) (bcl)
- driverdisk: Process kickstart driverdisk commands (#1035663) (bcl)
- driverdisk: Handle kickstart driverdisk command (#1035663) (bcl)
- driverdisk: Use getargs instead of the env variable (#1035663) (bcl)
- Remove now-unused isys/devices.[ch]. (clumens)
- Call finalize functions in parent classes. (dshea)
- Fix crashes in the LayoutIndicator dispose function. (dshea)
- Require systemd (dshea)
- Remove the now-unused anaconda_spoke_header.png. (clumens)
- Minor aesthetic cleanups (#1045250). (duffy)
- Add a topbar design to SpokeWindows. (#1045250) (duffy)
- Update the Aarch64 packages to include efibootmgr. (dmarlin)
- Add a sidebar to the standalone and hub windows (#1045250) (duffy)
- Allow specifying an environment in the kickstart file (#1050994). (clumens)
- The autopart scheme combo should work for creating partitions manually, too.
  (clumens)

* Tue Feb 04 2014 Brian C. Lane <bcl@redhat.com> - 21.20-1
- makebumpver: Any failure should cancel the bump (bcl)
- Add option help text for --image and --dirinstall flags (#1056791) (amulhern)
- Update bumpver to allow Related bugs (bcl)
- Fix up some pylint errors. (clumens)
- If a user has been created, don't allow entering the user spoke (#1058564).
  (clumens)
- Tweak passphrase wording a bit. (clumens)
- Tweak the final progress messages to fit on the screen a little better
  (#1058463). (clumens)
- Fix iscsi target selection checkbox in GUI (#1058653) (rvykydal)
- network ks: allow setting only hostname with network command (#1051564)
  (rvykydal)
- fcoe: add fcoe=<NIC>:<EDB> to boot options for nics added manually (#1040215)
  (rvykydal)
- network GUI: ignore fcoe vlan devices (#1051268) (rvykydal)
- Use an unused variable. (dshea)
- Ignore an unused function warning on isys_init (dshea)
- Remove unused isys files. (dshea)
- Fix the handling of realloc failures. (dshea)
- Run cppcheck on the C source files. (dshea)
- Check RAID10 box for BTRFS (#1021856) (amulhern)
- Make sure directory for DD extraction exists (vpodzime)
- Handle --image arguments more thoroughly (#982164,#994488) (amulhern)
- Remove the border from the custom part notebook. (clumens)
- Style the Done button to make it more noticable (mizmo). (clumens)
- Change the string used to test for serial console (#1054951) (dmarlin)

* Tue Jan 28 2014 Brian C. Lane <bcl@redhat.com> - 21.19-1
- Change the reclaim space button rules (#980496) (bcl)
- Revert "Fix up username checking regex a bit." (dshea)
- Fix a pylint-caught problem from my previous cherry-pick. (clumens)
- Give priority to IPv4 addresses when showing VNC & SSH IP (#1056420)
  (mkolman)
- Display custom part warnings/errors on the spoke itself (#975840). (clumens)
- Fix listing threads that caused an error (vpodzime)
- Do not add errors item for thread in advance (vpodzime)
- Log exceptions before running exception handling (vpodzime)
- Fix kickstart 'updates' command (#1056727) (wwoods)
- Fix exitHandler loop deactivation (bcl)
- Show hidden disk images (#1034996) (bcl)
- Fix pylint errors (dshea)
- Provide a maximum width to the betanag dialog. (clumens)
- Don't include zero sized disks in the custom part UI either (#903131).
  (clumens)
- Move the Quit button to the right and make it consistently sized (#1038802).
  (clumens)
- "Delete All" on the reclaim dialog should not delete hdiso source (#980496).
  (clumens)
- Add a scrollbar to the error dialog (#1021506). (clumens)
- Change the product name we key off (#1055019). (clumens)
- Another dracut pylint change. (dshea)
- Fix page logic in driver selection (#1055333) (bcl)
- Give users way to select DD ISO interactively (#1036765) (vpodzime)
- Make network-fetched driver disk .iso files work (#1003595) (vpodzime)
- Disable pylint messages too annoying to deal with. (dshea)
- Fix unused variable warnings (dshea)
- Remove unused imports (dshea)
- Specify string format arguments as logging function parameters (dshea)
- Remove the raidstart and raidstop commands (dshea)
- Expand the reach of pylint (dshea)
- Put Xorg on tty6 in accordance with Ancient Anaconda Tradition (#980062)
  (wwoods)
- Fix the handling of kickstart NFS repos with options (#1045528) (dshea)
- Skip empty layout-variant specifications when setting layouts (#1057442)
  (vpodzime)

* Thu Jan 23 2014 Brian C. Lane <bcl@redhat.com> - 21.18-1
- Use validate_label to check whether label should be updated (#1038590)
  (amulhern)
- Always reject label if the format exists (#1038590) (amulhern)
- Make label field always sensitive (#1038590) (amulhern)
- Save module list after initial module load (#1050352) (bcl)
- Require gtk3 and glib2 documentation to build (dshea)
- Rename get_widgets_datadir to anaconda_get_widgets_datadir. (dshea)
- Include the annotation-glossary (dshea)
- Set device.format.label field close to where we read it (#1056139) (amulhern)
- Install the rpmrc file to the initrd.img (#1016004) (vpodzime)
- Give users hint about VNC password restrictions (#1053546) (vpodzime)
- Be more liberal in what is accepted as a size unit. (dshea)
- Remove en_spec parameters from blivet.size.Size. (dshea)

* Tue Jan 21 2014 Brian C. Lane <bcl@redhat.com> - 21.17-1
- Test for DataHolder Class (#1034427) (bcl)
- Use DataHolder for TUI nfs data (#1034427) (bcl)
- Add DataHolder class (#1034427) (bcl)
- Handle inst.{gpt,dnf,extlinux} using cmdline.getbool() (wwoods)
- Drop unreferenced 'useIPv[46]' flag (wwoods)
- Don't force shell on tty2 (#980062) (wwoods)
- add comment about boot-options.txt (wwoods)
- Add support for getting stage2 image from boot.iso (#1035514) (mkolman)
- Various changes to handling of filesystem label setting (#1038590) (amulhern)
- Fix translation context on the storage options dialogs. (clumens)
- Fix problems going into custom partitioning with the new work flow. (clumens)
- Don't show actions next to free space lines in the reclaim dialog (#1054208).
  (clumens)
- If there's a label in the ISO device combo, put it on a new line (#1031727).
  (clumens)
- Make the device name in a MountpointSelector less wide (#1048583). (clumens)
- If a root password is set, don't show the spoke (#910355, #1041405).
  (clumens)
- Check for certain disk attrs before trying to access them. (#1053055)
  (sbueno+anaconda)
- Use gtk_get_locale_direction. (dshea)
- Always run efibootmgr from ROOT_PATH (bcl)
- A class for scheduling Gtk actions and running them all at once (vpodzime)
- Remove some leftover float conversions. (dshea)
- Use uint64 for the resize target size. (dshea)
- Return program output as a string instead of a list (dshea)
- Implement and use a function for one-off running Gtk actions (vpodzime)
- Be more defensive when getting layouts and their variants (vpodzime)
- Implement and use functions for conversion between keymaps and layouts
  (vpodzime)
- Fix reset of existing device to its original size. (dlehman)
- Don't disable checks for global at the module level. (dshea)
- Clean up the pylint-false-positives. (dshea)
- Remove pylint comments that are no longer necessary (dshea)
- Allow pylint-false-positives to end with a newline (dshea)
- Change storage widget visibility based on disks selected. (clumens)
- Rename widgets in the two remaining options dialogs. (clumens)
- Allow going to the reclaim dialog even for autopart (#1014671). (clumens)
- Add the autopart type combo to custom storage (#1014671). (clumens)
- Tweak DiskOverview spacing a little bit (#1014671). (clumens)
- Add custom part and encryption buttons to the main storage spoke (#1014671).
  (clumens)
- Remove the existing install_options1 dialog, rename the others (#1014671).
  (clumens)
- Grow the spoke gradient image to fit the nav_area (#1035772). (clumens)
- Additional completion checks in network spoke. (#1044571) (sbueno+anaconda)
- Fix problems reported by pylint (dshea)
- Decode potentially 8-bit strings in TUI windows (dshea)

* Fri Jan 10 2014 Brian C. Lane <bcl@redhat.com> - 21.16-1
- Use blivet.size.Size for all size quantities. (dlehman)
- make anaconda-shell (wwoods)
- handle "ks=cdrom[:<path>]" on systems with multiple CDs (#1049237) (wwoods)
- dracut: add when_any_cdrom_appears for cdrom autoprobe (wwoods)
- dracut: minor shell cleanup (wwoods)
- fix inst.noshell (#807703) (wwoods)
- Error gracefully if we have a question in cmdline mode. (#869731)
  (sbueno+anaconda)
- Verify that designated label can be set (#1038590) (amulhern)
- Do not change sensitivity of label field (#1038590) (amulhern)
- Make the clear icon functional in language spoke. (sbueno+anaconda)
- Fix the translated pango markup check (dshea)
- Remove iutil.strip_markup. (dshea)
- Pass additional command-line arguments to pylint (dshea)
- Fix and ignore markup warnings where appropriate (dshea)
- Check that the Pango markup in glade files is valid (dshea)
- Added a pylint module to check pango markup. (dshea)
- Split the po-based translation code into a separate file. (dshea)
- Fix bool parsing of boot options with inst. prefix (#1044391) (mkolman)
- Use vc_keymap as X layout only if we get nothing from localed (#1048592)
  (vpodzime)
- Warn user if entering LUKS password with non-ASCII characters (#1039168)
  (vpodzime)
- Add back some erroneously removed set_use_underline calls (dshea)
- Only show the "DATA" heading if there are data mount points under it.
  (clumens)
- Don't allow the advanced user dialog to be saved with errors (dshea)
- Move the add_check stuff into helper classes. (dshea)
- Remove the UID and GID maximums. (#978846) (dshea)
- Fix an invalid mnemonic widget reference in passphrase entry (dshea)
- Added checks for some potential issues in glade files (dshea)
- Remove scrot dependency for global screenshot support (mkolman)
- Fix mnemonic widget reference id (vpodzime)

* Tue Jan 07 2014 Brian C. Lane <bcl@redhat.com> - 21.15-1
- Use the new Gtk.ListBox for displaying environments and addons (#1039683).
  (clumens)
- Display additional disk attributes in TUI storage spoke. (#1024760)
  (sbueno+anaconda)
- Fix 'select all disks' logic in TUI storage spoke. (sbueno+anaconda)
- Ignore the compile script (dshea)
- network GUI: don't crash when wifi is activated in standalone spoke
  (#1046138) (rvykydal)
- Use the right test for there being any storage actions. (clumens)
- Only display the actions summary dialog if there are any actions (#1030511).
  (clumens)
- Do not support kickstart+live installs (#1027160). (clumens)
- We no longer directly use libnl (#1034830). (clumens)
- Remove _transactionErrors from yumpayload.py. (clumens)
- Move xhost handling to the xinit script (#1045280) (dshea)
- Check for ready before baseRepo in completed (#1044985) (bcl)
- Treat the output of vncpasswd as binary data, since it is (#1045119) (dshea)
- Add iutil.exec* options for handling binary data (dshea)
- Print a message and exit if a user attempts to upgrade via kickstart. (dshea)

* Wed Dec 18 2013 Brian C. Lane <bcl@redhat.com> - 21.14-1
- Fix the release notes image cycler. (#1043393) (dshea)
- Do not schedule resize actions for non-resizing requests (#1039491)
  (vpodzime)
- Use ceil for minSize in resize dialog (#1040012) (bcl)
- Use integer numbers of megabytes in the Reclaim dialog (#1040012) (vpodzime)
- fcoe gui: repopulate device tree only if device was actually added (#1039223)
  (rvykydal)
- Exclude FCoE disks from local disks (#1039223) (rvykydal)
- fcoe: repopulate devicetree after adding FCoE SAN (#1039223) (rvykydal)
- Add initial 64-bit ARM aarch64 EFI support (#1034428) (dmarlin)
- Rename network spoke header (mkolman)
- Show the Shell spoke in debug mode (vpodzime)
- Accept only .iso files from the IsoChooser dialog (#1015169) (vpodzime)
- Just run the IsoChooser dialog lightbox (vpodzime)
- Use libxklavier's new methods instead of our nasty hack (vpodzime)
- Move atexit registration before running rescue mode (#1038855) (vpodzime)
- Only display the addon separator if there's a reason to. (clumens)
- Stop using deprecated gtk margin functions. (clumens)
- Fix the check_accelerators srcdir path. (dshea)
- Show msg in TUI if user attempts to create invalid username. (#965561)
  (sbueno+anaconda)
- Fix up username checking regex a bit. (sbueno+anaconda)
- Fix default device for ks=cdrom (#1042500) (bcl)
- createUser is already in a chroot (#1038241) (bcl)
- Skip checks on files that are not staged for commit. (dshea)
- Allow catching exceptions from threads (vpodzime)
- Enable warnings about abstract methods not overridden (dshea)
- Provide empty methods to override abstract parent methods. (dshea)
- Implement status in StandaloneSpoke. (dshea)
- Move a bunch of abstract methods from Payload to PackagePayload (dshea)
- Remove some methods from packaging.Payload. (dshea)
- Disable abstract method warnings in intermediate abstract classes. (dshea)
- Remove Personalization spoke (dshea)
- Remove some vestigal code from an earlier version of GUICheck (dshea)

* Thu Dec 12 2013 Brian C. Lane <bcl@redhat.com> - 21.13-1
- Refresh environment addons on source change (#1033749) (bcl)
- Fix selector device matching for unallocated partitions. (#1039292) (dlehman)
- Rename the network config spoke a little bit. (clumens)
- Don't encrypt device if container is encrypted (bcl)
- network: add s390 options in ifcfgs generated from kickstart (#1031376)
  (rvykydal)
- Remove enablement of whiteout/blackout plugins, and the requires on anaconda-
  yum-plugins. (notting)
- Fix checking if we are collecting our module (vpodzime)
- Remove an unnecessary continue statement in the potfiles check (vpodzime)
- Use sys.exit instead of os._exit in the potfiles test (vpodzime)
- List addons in exception report data (vpodzime)
- Make Hub.storage and Spoke.storage a property (dshea)
- Fix the botched helperization of StorageChecker (dshea)
- Disable tmpfs in the GUI (#1039511) (mkolman)
- Don't crash on NTP lookup without network (#1026079) (mkolman)
- Don't rely on Gtk being importable for exception handling (vpodzime)
- Support rnotes in SVG format (#1034407). (clumens)
- Fix a couple warnings from -Werror=format-security (#1036989). (clumens)
- Use abstract base classes for mixins. (dshea)
- Display free space remaining in containers (#1035832). (clumens)
- Make sure url and mirrorlist are not set at once (#1026834) (mkolman)
- if rootfs is btrfs, add rootflags=subvol to kernel parameters (gene)
- add ro to bootloader kernel parameters (gene)
- Added missing entries to POTFILES.in (dshea)
- Add a check that files with translatable strings are in POTFILES.in (dshea)
- Fix the handling of renames in the pylint git hook. (dshea)
- Remove startup-id from AnacondaBaseWindow. (dshea)

* Wed Dec 04 2013 Brian C. Lane <bcl@redhat.com> - 21.12-1
- Handle cancelation of device resize in the custom spoke. (#1027947) (dlehman)
- Disallow /boot on lvm until grub2 fully supports it. (#1036705) (dlehman)
- Disallow /boot on btrfs subvolume until grubby supports it. (#864198)
  (dlehman)
- Remove an empty initialize function. (clumens)
- Move PathDict into pyanaconda/ui/__init__.py. (clumens)
- Add one more directory for ignoring test log files (dshea)
- Defer translation of device_type_name (dshea)
- Disable pylint errors about gobject-introspection methods (dshea)
- Remove unused variables (dshea)
- Document the instl.multilib boot option (vpodzime)
- Minor tweak of our driver disk documentation (vpodzime)
- network: GUI, don't ask for wifi secrets upon Configure (#1033073) (rvykydal)
- network: GUI, add support for virtual devices removing (#1030870) (rvykydal)
- network: fix naming of slave ifcfg files from kickstart (#1036047) (rvykydal)
- network: GUI, handle virtual devices (bond, vlan, team) properly (#1036047)
  (rvykydal)
- Change how we test if the GUI is available in the anaconda script. (clumens)
- Update boot-options.txt. (amulhern)
- Omit /dev/sr* from list-harddrives (#1032500) (sbueno+anaconda)
- Fix EditTUISpoke to operate only on visible entries (vpodzime)
- Don't try to investigate empty string for unicode chars (#1035799) (vpodzime)
- Fix issues reported by the check_pw_visibility test (vpodzime)
- Add check testing visibility of password entries (vpodzime)
- Put tests of .glade files into a separate directory (vpodzime)
- Save a reference to the imported Xkl module for get_current_layout (dshea)
- Fix the Makefile.am subdirs for widget data. (dshea)
- Fix some pylint warnings. (clumens)
- Switch to libtimezonemap for the timezone map. (dshea)
- Set the _config_dialog property during __init__. (dshea)
- Fix handling of long release ids (mkolman)
- Store older valid packages in separate folder (mkolman)
- Fetch older valid releases (mkolman)
- Import Xkl only when really needed (vpodzime)
- Global screenshot support (#1025038) (mkolman)
- Require new version of python-blivet (vpodzime)
- Hide password characters in iSCSI login fields (#1034202) (vpodzime)
- Use format names instead of types in the resize dialog (vpodzime)
- Do not write out the vconsole.keymap boot option (#1035316) (vpodzime)

* Wed Nov 27 2013 Brian C. Lane <bcl@redhat.com> - 21.11-1
- Use raid RAID level constants instead of mdraid RAID level constants.
  (amulhern)
- Use level objects instead of level integer codes. (amulhern)
- clear software environment (#1029536) (bcl)
- Update source on errors (#1030997) (bcl)
- Fix errors in kickstart.py. (dshea)
- Update gettext.txt (dshea)
- Don't allow bootloader and /boot on iSCSI on s390 (#1034222) (vpodzime)
- Round float values coming from the Gtk stack (#1013586) (vpodzime)
- Generate missing machine-id (bcl)
- Fix problems reported by pylint. (dshea)
- Add HDD ISO support for TUI (#1000327) (mkolman)
- Use a directory in build tree for pylint data. (dshea)
- Remove MOSTLYCLEANDIRS from Makefile.am (dshea)
- fixup spec for fedup (bcl)

* Mon Nov 25 2013 Brian C. Lane <bcl@redhat.com> - 21.10-1
- Cleanup anaconda.spec.in (bcl)
- Handle non-leaf btrfs volumes with mountpoints. (#1016959) (dlehman)
- Use en_spec for blivet Size spec strings with constant components. (#1029616)
  (dshea)
- The gui and tui subpackages cannot be noarch (vpodzime)
- Cleanup unused and overly complicated stuff in isys (vpodzime)
- DNFPayload: tweak to the API changes in dnf-0.4.8 (ales)
- Don't use cached packages with different release id (mkolman)

* Fri Nov 22 2013 Brian C. Lane <bcl@redhat.com> - 21.9-1
- Add a test for accesses of yum.preconf outside of _resetYum. (clumens)
- Remove base_repo cache (#1011555) (bcl)
- Make _yum.preconf setup atomic (#1028245) (bcl)
- Remove threading from getBaseRepo handling (#1011555) (bcl)
- If there are incomplete spokes, let the user know which (#1032801). (clumens)
- tui: show Processing while source is busy (bcl)
- tui: wait for threads before entering source and software (#1032823) (bcl)
- clear errors when metadata is ok in tui source spoke (#1006570) (bcl)
- Fix parallel pylint in distcheck. (dshea)

* Wed Nov 20 2013 Brian C. Lane <bcl@redhat.com> - 21.8-1
- Fix geolocation on live installs (mkolman)
- Ignore the pylint warning on importing GraphicalUserInterface. (clumens)
- Fall back to text mode if GUI is not available (vpodzime)
- Get rid of unused isys.isCapsLockEnabled function (vpodzime)
- Don't rely on having zenity and require it only for GUI (vpodzime)
- No longer need the Gconf2 package (vpodzime)
- Split out anaconda's user interfaces into separate packages (vpodzime)
- Do not include tzmapdata into the main package (vpodzime)
- Create directories for stubs if they don't exist (vpodzime)
- Do not try to fetch our own packages that will be built (vpodzime)
- Remove the unused flags import from installclass.py. (clumens)
- Fix logging of pylint-one output (bcl)
- Do yum lock logging only with inst.debug or loglevel=debug (vpodzime)
- Don't panic on installclasses failing with inst.debug (vpodzime)

* Mon Nov 18 2013 Brian C. Lane <bcl@redhat.com> - 21.7-1
- Expand the use of ANACONDA_WIDGETS_DATADIR. (dshea)
- Make thread manager operations atomic (#1029898) (mkolman)
- Run pylint in multiple processes (vpodzime)
- Fix how "changed" signal is emitted on the TreeSelection (vpodzime)
- Pass biosdevname boot option to installed system (#1023609) (rvykydal)
- network: update required NetworkManager version (team support) (rvykydal)
- Use timing decorator for more actions (vpodzime)
- Add test for the have_word_match function (vpodzime)
- A nice decorator making Anaconda's GUI more responsive (vpodzime)
- Short-circuit layouts matching (vpodzime)
- Enforce upper bound for resize. (#1027947) (dlehman)
- Fix some pylint problems in network.py. (clumens)
- Add an updates location for the AnacondaWidgets overrides (dshea)
- Fix typo (#1003591) (rvykydal)
- network: call GDBus proxy methods like python (rvykydal)
- network: add team support for kickstart %%pre phase (#1003591) (rvykydal)
- network: generate kickstart commands for team devices (#1003591) (rvykydal)
- network: support for adding team devices (#1003591) (rvykydal)
- network: display team devices in status (#1003591) (rvykydal)
- network: add team support to kickstart (#1003591) (rvykydal)
- Initialize the AddLayouts dialog in advance in the KeyboardSpoke (vpodzime)
- Add function to map functions on items in the main thread (vpodzime)
- Allow having unique thread names with given prefix (vpodzime)
- Remove an unused and non-working leftover function resetResolve (vpodzime)
- Always center dialogs shown on top of lightbox (vpodzime)
- Set spokes' distribution and beta warning only once (vpodzime)
- use deepcopy on ksdata method (#1028243) (bcl)
- Change source spoke proxy handling to use local copy (#967805) (bcl)
- Apply a little tweak to the VNC password length message. (clumens)
- Match layouts with stripped accents in AddLayout dialog (vpodzime)
- Sort layout descriptions properly (#1026238) (vpodzime)
- Make AddLayout dialog persistent (vpodzime)
- Use Sphinx syntax in the iutil module (vpodzime)
- Warn if vnc passwd is longer than 8 chars (hamzy)
- Don't try to unicode unicode strings (#1029109) (vpodzime)
- Add tmpfs support (#918621) (mkolman)
- Added a few things that autoscan complained about (dshea)
- Actually use the config header we generate (dshea)
- Redirect pylint stderr to stdout (dshea)
- Fix the handling of files generated for xgettext (dshea)
- Use gettext to process glade files. (dshea)
- Always use $prefix in directory names. (dshea)
- Pass --enable-gtk-doc to configure in distcheck (dshea)
- Fix the liveinst install/uninstall hooks (dshea)
- Clean up after intltool (dshea)
- Add missing files to dist (dshea)
- DNFPayload: tweak to the API changes in dnf-0.4.7. (ales)
- Add tests for iutil (mkolman)

* Fri Nov 08 2013 Brian C. Lane <bcl@redhat.com> - 21.6-1
- Fix typos in translation functions (dshea)
- Put the cityCompletion back on the list of widgets (vpodzime)
- Do not translate strings defined at the module or class level. (clumens)
- Fix a couple places where we're doing %% inside of _(). (clumens)
- Add a custom pylint module to check i18n problems. (clumens)
- Remove an unused import. (clumens)
- Provide our own sorting functions for regions and timezones (#1025029)
  (vpodzime)
- Set locale for our process (vpodzime)
- Translate timezones in GUI (vpodzime)
- network gui: add apply tooltip to Configure button (#1018471) (rvykydal)
- Make dialog return code checking more robust (amulhern)
- Show last 4 bytes of wwid (#1024966) (jstodola)
- Handle focus changes of MountpointSelectors from outside (#975838) (vpodzime)
- network: do not crash when device for network --device is not found
  (#1023829) (rvykydal)
- Log continuing from hub if there are no spokes (vpodzime)
- Updates to boot-options.txt document (#1026449) (amulhern)
- No longer install anaconda user documentation (#1026449) (amulhern)

* Fri Nov 01 2013 Brian C. Lane <bcl@redhat.com> - 21.5-1
- Fix spoke sorting issues in text-mode. (#929177) (sbueno+anaconda)
- Send the continue click after the queue is empty (#1025347) (bcl)
- No longer use summary screen visit to decide whether bootloader has been
  configured (#1025811) (amulhern)
- Remove the bootloader line from the interactive kickstart file (#1025811)
  (amulhern)
- Set bootloader default location to mbr in constructor (#1025811) (amulhern)
- Remove column titles from the software spoke. (dshea)
- Fix the selection of default groups (#1023263) (dshea)
- Use the default yscale for the HubWindow alignment (dshea)
- Fix kickstart block device resolution. (#1022206) (dlehman)
- Specify query territory when getting language native name (vpodzime)
- Get rid of trailing whitespace (vpodzime)
- Export the right classes from the tui.spokes package (vpodzime)
- Define newLayoutStore before it is used by the filter (vpodzime)

* Wed Oct 30 2013 Brian C. Lane <bcl@redhat.com> - 21.4-1
- Fix up a couple more pylint errors. (clumens)
- Add check for Linux HFS+ ESP on Mac (#1010495) (bcl)
- Update bootDrive info when storage config updated in text-mode. (#861018)
  (sbueno+anaconda)
- Remove the special handling for en (dshea)
- Ignore SIGINT (#1024822) (amulhern)
- Don't show language twice for keyboard layouts (#1021907) (petersen)
- Make Software spoke ready even if there is no repo (#1010348) (vpodzime)
- Use decorator for methods that invalidate base repo cache (vpodzime)
- Use cache for base repo if possible (vpodzime)
- Make sure to actually set the autopart flag when needed. (#1023554) (dlehman)
- Fix Gtk errors about list store columns (dshea)
- Fix the layout up and down button sensitivies. (dshea)
- Fix the Gkbd spec string for layouts with no variant (dshea)
- pylint wants regexes with backslashes to be specified with 'r'. (clumens)
- Add ack flag checking to makebumpver (bcl)
- Correctly accept 'sshd' boot arg as alias for 'inst.sshd' (#924157) (wwoods)
- Only eject CDROM devices we're actually using (#949919) (wwoods)
- mem may not exist when it's printed out in these error messages. (clumens)

* Fri Oct 25 2013 Brian C. Lane <bcl@redhat.com> - 21.3-1
- Reset _proxyChange when a change is triggered (bcl)
- Setup No Update checkbox correctly (#1016801) (bcl)
- Fall back to closest mirror in source (#1016801) (bcl)
- anaconda-dracut: fix ks failure with hd:<dev>:some/path.ks (wwoods)
- Make sure lower bound for resize is applied. (#986575) (dlehman)
- Use devicetree to resolve device specs in kickstart. (#1022206) (dlehman)
- Disregard raid level combo when it isn't applicable. (#1022203) (dlehman)
- Mountpoint is an attr of the format, not the device. (#892747) (dlehman)
- Add bootloader execute before autopart (#1021258) (bcl)
- Do error checking of repository names on "Installation Source" screen.
  (amulhern)
- Avoid configure-event loops. (#1021511) (dshea)

* Wed Oct 23 2013 Brian C. Lane <bcl@redhat.com> - 21.2-1
- remove signal disconnect (#996899) (bcl)
- Re-saved every glade file with glade-3.16.0 (dshea)
- Fix pylint errors in network.py. (clumens)
- Always use decimal notation for Size specs (dshea)
- network kickstart: add support for devices configured in %%pre (#1019796)
  (rvykydal)
- network gui: make Configure button insensitive when no ap is selected
  (#1015212) (rvykydal)
- Encode possible unicode objects before calling str() on them (vpodzime)
- Fix a typo in function documentation (vpodzime)
- Use more general status for installations from media (#1017703) (vpodzime)

* Mon Oct 21 2013 Brian C. Lane <bcl@redhat.com> - 21.1-1
- Adds additional debug logging to yumpayload.py. (amulhern)
- Handle invalid JSON in geoloc (#1021410) (dshea)
- Revert "Only prompt for LUKS password if the user has chosen to configure
  automatically." (amulhern)
- Add context support to check_accelerators (dshea)
- Added translation contexts to the TUI. (dshea)
- Added translation contexts to the GUI. (dshea)
- Add support for context-based translations (dshea)
- Reset checks on both password fields. (#1020580) (dshea)
- Fix swaps added to fstab for noformat (gene)
- Don't update hub's continue button and label for every spoke (#1020373)
  (vpodzime)
- Add storage tests. (clumens)
- Add option to select all hard drives in text mode. (#965580)
  (sbueno+anaconda)
- BootLoaderError should not reset storage (#1019541) (bcl)
- Only prompt for LUKS password if the user has chosen to configure
  automatically. (amulhern)
- Remove an unused string (dshea)
- Translate AM and PM (dshea)
- Translate strings marked as translatable (dshea)
- network gui spoke: use GDBus to obtain list of settings (#1018467) (rvykydal)
- network: look for device settings also based on DEVICE value (#1017788)
  (rvykydal)
- Fix liveinst to work with livemedia-creator (#1009711) (bcl)
- Remove the button-label property on SpokeWindow. (clumens)
- Log entering/exiting spokes and hubs in the GUI. (clumens)
- Escape text inserted into markup strings (dshea)
- Move markup out of translatable strings (dshea)
- Move formating markup out of python where possible (dshea)
- Use explicit children to set label attributes (dshea)
- Turn on the image on the "Add a disk..." button. (dshea)
