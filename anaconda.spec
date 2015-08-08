%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Version: 23.19
Release: 1%{?dist}
License: GPLv2+ and MIT
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

# To generate Source0 do:
# git clone https://github.com/rhinstaller/anaconda
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).

# Also update in AM_GNU_GETTEXT_VERSION in configure.ac
%define gettextver 0.18.3
%define intltoolver 0.31.2-3
%define pykickstartver 2.9
%define dnfver 0.6.4
%define partedver 1.8.1
%define pypartedver 2.5-2
%define nmver 0.9.9.0-10.git20130906
%define dbusver 1.2.3
%define mehver 0.23-1
%define firewalldver 0.3.5-1
%define utillinuxver 2.15.1
%define dracutver 034-7
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.873-26
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.34
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
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libgnomekbd-devel
BuildRequires: libxklavier-devel >= %{libxklavierver}
BuildRequires: pango-devel
BuildRequires: python3-kickstart >= %{pykickstartver}
%if ! 0%{?rhel}
BuildRequires: python3-bugzilla
%endif
BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: systemd
# rpm and libarchive are needed for driver disk handling
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
Requires: python3-dnf >= %{dnfver}
Requires: python3-blivet >= 1:1.12
Requires: python3-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libselinux-python3
Requires: rpm-python3 >= %{rpmver}
Requires: parted >= %{partedver}
Requires: python3-pyparted >= %{pypartedver}
Requires: python3-requests
Requires: python3-requests-file
Requires: python3-requests-ftp
Requires: python3-kickstart >= %{pykickstartver}
Requires: langtable-data >= %{langtablever}
Requires: langtable-python3 >= %{langtablever}
Requires: libuser-python3
Requires: authconfig
Requires: firewalld >= %{firewalldver}
Requires: util-linux >= %{utillinuxver}
Requires: python3-dbus
Requires: python3-pwquality
Requires: python-IPy-python3
Requires: python3-pytz
Requires: realmd
Requires: teamd
%ifarch %livearches
Requires: usermode
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum >= %{isomd5sum}
Requires: createrepo_c
Requires: NetworkManager >= %{nmver}
Requires: NetworkManager-glib >= %{nmver}
Requires: NetworkManager-team
Requires: dhclient
Requires: kbd
Requires: chrony
Requires: python3-ntplib
Requires: rsync
Requires: systemd
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: python3-iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif
%ifnarch aarch64
Requires: kexec-tools
%endif
Requires: python3-pid

Requires: python3-coverage

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
Requires: python3-meh-gui >= %{mehver}
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
Requires: python3-gobject-base

# Needed to compile the gsettings files
BuildRequires: gsettings-desktop-schemas

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
Requires: python3

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
Requires: dracut-live
Requires: xz
Requires: python3-kickstart

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q

%build
%configure
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

%files core -f %{name}.lang
%license COPYING
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%exclude %{_prefix}/libexec/anaconda/dd_*
%{python3_sitearch}/pyanaconda/*
%exclude %{python3_sitearch}/pyanaconda/rescue.py*
%exclude %{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%exclude %{python3_sitearch}/pyanaconda/ui/gui/*
%exclude %{python3_sitearch}/pyanaconda/ui/tui/*
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
%{python3_sitearch}/pyanaconda/ui/gui/*
%{_datadir}/anaconda/window-manager/glib-2.0/schemas/*
%{_datadir}/themes/Anaconda/*

%files tui
%{python3_sitearch}/pyanaconda/rescue.py
%{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%{python3_sitearch}/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*

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
* Fri Aug 07 2015 Brian C. Lane <bcl@redhat.com> - 23.19-1
- Add basic support for LVM cache creation in kickstart (vpodzime)
- Use labels for the rest of the non-autopart test results. (dshea)
- Use a disk label to find the filesystem for escrow results (dshea)
- Use someone else's code for PID file management. (dshea)
- Prevent incomplete translations from making the TUI unusable (#1235617)
  (mkolman)
- Apply the environment substitutions more liberally in nfs-repo-and-addon
  (dshea)
- Use stage2=hd: instead of stage2=live: (dshea)
- Add test for liveimg kickstart command (bcl)
- Fix pre-install script execution (bcl)
- test pre-install kickstart section (bcl)
- Use sys.exit() instead of the exit() created by site.py. (dshea)
- Call ipmi_report before sys.exit (dshea)
- Add a test for proxy authentication (dshea)
- Add optional authentication to the proxy server (dshea)
- Add more tests to proxy-kickstart (dshea)
- Show an alternative prompt if a hub contains only a single spoke (#1199234)
  (mkolman)
- Add few docs and improvement in check_ip_address (jkonecny)
- Check whether files actually contain translatable strings. (dshea)
- Add specific error string to TUI user dialog (#1248421) (bcl)
- Make EditTUIDialog error generic (#1248421) (bcl)
- Fix and expand nfs-repo-and-addon.ks (dshea)
- Added a script to make the packages used by nfs-repo-and-addon (dshea)
- Implement the rest of the repo options in dnfpayload. (dshea)
- Fix kickstart test for bond interface creation (jkonecny)

* Fri Jul 31 2015 Brian C. Lane <bcl@redhat.com> - 23.18-1
- Move the proxy server script into a common file. (dshea)
- Use python3 for the proxy server and remove python2 compatibility (dshea)
- makePickle now needs to return bytes (bcl)
- gi.require_version raises ValueError (bcl)
- Remove duplicate signal setup block (bcl)
- Fix three bugs discovered by driverdisk-disk.ks (clumens)
- Fix error with OEMDRV ks auto-load check. (#1057271) (sbueno+anaconda)
- Make sure TUI is readable for non-latin languages (#1182562) (mkolman)
- Equalize capacity & mount point entries (#1212615) (dshea)
- Disable GRUB os_prober on POWER (#1193281) (rmarshall)
- Cancel Container Edit Sensitizes Update (#1168656) (rmarshall)
- Fix SoftwareSpoke._kickstarted. (dshea)
- Disable a Pylint false-positive (#1234896) (mkolman)
- Add support for autostep and --autoscreenshot (#1234896) (mkolman)
- Escape \'s in doc strings (dshea)
- Ellipsize the file system type combo box (#1212615) (dshea)
- Add graphviz to make-sphinx-doc script (jkonecny)
- Remove many of a documentation compilation errors (jkonecny)
- Add class diagrams to existing spokes and hubs (jkonecny)
- Add class diagram settings to documentation (jkonecny)
- Fix the UnusuableConfigurationError dialog (#1246915) (dshea)
- Chase pygobject's stupid moving target (dshea)
- Add missing translation contexts (dshea)
- Actually translate the container type labels (dshea)
- Check whether a translated string requires a context or comment. (dshea)
- Clean up the temporary pools virt-install makes. (clumens)
- Return the same object for repeated calls to __get__ (#1245423) (dshea)
- Use sys.exit instead of os._exit. (clumens)
- Add parentheses around the IPV6 regex fragment. (dshea)
- Add tests for IPv6 literals in URLs (dshea)
- Modify Installation Source Proxy Label (#11688554) (rmarshall)

* Fri Jul 24 2015 Brian C. Lane <bcl@redhat.com> - 23.17-1
- Fix Initial PPC PReP Boot Selector Name (#1172755) (rmarshall)
- Require a newer version of pykickstart (vpodzime)
- Use dictionaries is thread-safe manner. (dshea)
- Merge pull request #234 from wgwoods/master (wwoods)
- Auto-load ks.cfg if OEMDRV volume available. (#1057271) (sbueno+anaconda)
- Check the encrypt checkbox when encrypted specified in KS (vtrefny)
- Do not raise KickstartValueError for missing passphrase (vtrefny)
- Ask for encryption passphrase when not specified in ks (#1213096) (vtrefny)
- dracut: minor cleanup (wwoods)
- dracut: fix missing messages for inst.ks=cdrom (wwoods)
- Wait forever for kickstarts on CDROM (#1168902) (wwoods)
- Use abs_builddir instead of builddir so paths will look more reasonable.
  (clumens)
- Add a new makefile target that does everything needed for jenkins. (clumens)
- Merge pull request #228 from AdamWill/logind (dshea)
- Fix crash when mirrorlist checkbox is checked (jkonecny)
- Fix crash when user start typing proxy credentials (jkonecny)
- Check repository URL before leaving Source Spoke (jkonecny)
- Add IDs to identify addon repositories (jkonecny)
- Repositories can be checked without a selection (jkonecny)
- Consolidate the language environment variables. (dshea)
- Change the generated API indices slightly (dshea)
- Ignore "mountpoint" used a format specifier (dshea)
- filesystems -> file systems, per the style guide (dshea)
- Properly parameterize a translated string (dshea)
- Fix pylint errors in rescue.py. (dshea)
- Remove unused imports (dshea)
- Remove text.py from spec file (#965985) (sbueno+anaconda)
- Merge pull request #220 from AdamWill/1243962 (dshea)
- Fix adding 'boot=' option in FIPS mode (vtrefny)
- anaconda.target: Wants systemd-logind.service (#1222413) (awilliam)
- Remove the last usage of newt and get rid of it as a dependency (#965985)
  (sbueno+anaconda)
- Enable anaconda to use the new rescue mode. (#965985) (sbueno+anaconda)
- Get rid of unnecessary constants in constants_text. (#965985)
  (sbueno+anaconda)
- Get rid of some unnecessary files. (#965985) (sbueno+anaconda)
- Display verbose packaging errors to the user (bcl)
- Show source errors from refresh method (bcl)
- Fix the validate functions in the btrfs kickstart_tests. (clumens)
- Connect kickstart lang data to dnf-langpacks (#1051816) (dshea)
- Add simple_replace config file function (bcl)
- Remove some vestiges of the old packaging module (dshea)
- Remove window boot block detection functions. (dshea)
- Remove iutil.xprogressive_delay. (dshea)
- Simplify iutil.mkdirChain. (dshea)
- Decode wifi SSIDs into strings. (#1240398) (dshea)
- Actually use the temp directory so test files get cleaned up (dshea)
- Disable the output from rpmbuild (dshea)
- Remove stray references to python2. (dshea)
- Fix possible to start installation without network (#1221109) (jkonecny)
- Fix 'q' (to quit) do not work in TUI hub (jkonecny)
- act on the right objects when stripping URL protocols (#1243962) (awilliam)
- Fix 'App' object has no attribute 'queue' (#1243316) (jkonecny)

* Thu Jul 16 2015 Brian C. Lane <bcl@redhat.com> - 23.16-1
- fix storage writing for live and ostree installs (#1236937) (awilliam)
- Add O_CREAT to the open flags when extracting rpm files. (dshea)
- Move ostree gobject version check next to the import (#1243543) (bcl)
- Remove rpmfluff from the buildrequires. (dshea)
- Only import readline if readline is necessary. (dshea)
- use the right baseurl in run_install_test.sh. (clumens)
- Don't copy the environment when starting metacity. (dshea)
- Fix the use of a temporary file in SimpleConfig.write (dshea)
- Add a test for SimpleConfig.write(use_tmp=True). (dshea)
- Remove an unnecessary chmod when creating chrony.conf (dshea)
- Fix some bad uses of chmod. (dshea)
- Add a function to open a file with specific permission bits (dshea)
- Don't ask to start vnc if user specifies text mode. (#1202277)
  (sbueno+anaconda)
- New Anaconda documentation - 23.15 (bcl)
- Add a helper for building Sphinx docs using mock. (bcl)
- Update Sphinx configuration for python3 (bcl)
- Running without a GUI can also raise ValueError in errors.py (bcl)
- parse-kickstart_test.py: fix driverdisk_test() (wwoods)
- Fix the spelling of "version" (dshea)

* Mon Jul 13 2015 Brian C. Lane <bcl@redhat.com> - 23.15-1
- Some dracut modules anaconda needs have been split into their own package.
  (clumens)
- User operation kickstart tests. (kvalek)
- Kickstart tests for UTC and LOCAL hwclock. (kvalek)
- Kickstart firewall tests. (kvalek)
- Fix Repository New_Repository has no mirror or baseurl (#1215963) (jkonecny)

* Fri Jul 10 2015 Brian C. Lane <bcl@redhat.com> - 23.14-1
- Catch blivet formatDevice ValueError in custom (#1240226) (bcl)
- There's now a python3-rpmfluff, so revert this. (clumens)
- Fix a couple other pylint problems in the driver disk tests. (clumens)
- Merge pull request #194 from wgwoods/master (wwoods)
- dracut: fix boot failure waiting for finished/dd.sh (wwoods)
- Use builddir instead of srcdir to find the dd utils (dshea)
- Fix the dd_test for python3. (dshea)
- Fix %%files to deal with compiled python3 modules (dshea)
- Add a bunch of gi.require_version calls (dshea)
- Temporarily disable the error about not importing rpmfluff. (clumens)
- Don't try to iterate over threads directly in wait_all. (clumens)
- Update the btrfs kickstart tests to use functions.sh. (clumens)
- Merge pull request #182 from wgwoods/dd-refactor (wwoods)
- driver_updates: fixes from patch review (wwoods)
- Don't be too picky about what name is --device=link (dshea)
- Ignore stderr output from parse-kickstart. (dshea)
- Add an option to execReadlines to filter out stderr. (dshea)
- Ignore interruptible system calls in the dd test (dshea)
- Fix an undefined variable in writeStorageLate (dshea)
- Connect zfcp entries to the discovery buttons (dshea)
- Connect iscsi activations to buttons (dshea)
- Connect the dasd number entry to the discovery buttons. (dshea)
- Add keyboard layouts on the row-activated signal. (dshea)
- Connect dialog inputs to default actions. (dshea)
- Remove unnecessary GtkNotebooks. (dshea)
- Re-save some dialog glade files. (dshea)
- Merge pull request #181 from wgwoods/master (wwoods)
- dd-refactor: dracut + build bits (wwoods)
- Add kickstart test for RAID1 (bcl)
- pass PYTHONPATH to the kickstart test framework (bcl)
- Write servers to chronyd.conf even if it's off (#1197575) (wwoods)
- Refresh advanced disks after disk summary dialog (#1226354) (bcl)
- parse-kickstart: just emit 'inst.dd=XXX' for driverdisk (wwoods)
- parse-kickstart: pylint fixes (wwoods)
- dd-refactor: new driver_updates.py + tests (wwoods)
- payload: fix driverdisk repos (wwoods)
- dracut: fix boot with inst.ks and no inst.{repo,stage2} (#1238987) (wwoods)
- Use the most recent versions of the btrfs, logvol, part, and raid commands.
  (clumens)
- Allow /boot partition on iscsi with ibft (#1164195) (jkonecny)
- Add kickstart tests to test btrfs installation (vtrefny)
- Fix broken test by infiniband patch (#1177032) (jkonecny)

* Thu Jul 02 2015 Brian C. Lane <bcl@redhat.com> - 23.13-1
- Add a switch for the Airplane Mode label (dshea)
- Connect labels with keyboard accelerators to a widget (dshea)
- Add a test for dangling keyboard accelerators. (dshea)
- Use pocketlint for translation and markup checking (dshea)
- Flatten the glade test directory. (dshea)
- Add support for specifying arbitrary mkfs options. (clumens)
- Fix kickstart install with infiniband (#1177032) (jkonecny)
- anaconda-dracut: Fix sysroot mount for netroot (#1232411) (bcl)
- Add RAID swaps to /etc/fstab (#1234469) (bcl)
- network: catch another race when calling dbus methods on invalid devices
  (rvykydal)
- network: GUI, add connection even when virtual device activation failed
  (#1179276) (rvykydal)
- Fix IP / hostname mismatches when showing VNC server address (#1186726)
  (rvykydal)
- Check also ipv6 default routes when looking for onboot=yes device (#1185280)
  (rvykydal)
- Merge pull request #157 from wgwoods/master_dd_fixes (wwoods)
- Do not check dependencies on invalid payloads (dshea)
- network: don't set onboot=False for default autoconnections (#1212009)
  (rvykydal)
- Fix the types used to write anaconda-tb-all.log (dshea)
- dd: drop unnecessary archive_read_data_skip (wwoods)
- dd_extract: -l should not extract modules+firmware (wwoods)
- dd: fix permissions on extracted files (#1222056) (wwoods)
- tests: add dd_tests (wwoods)

* Fri Jun 26 2015 Brian C. Lane <bcl@redhat.com> - 23.12-1
- Revert "Add an optional conditional to progress_report." (bcl)
- Fix inconsistencies in the payload messages. (dshea)
- Fix install-requires and install-buildrequires (dshea)
- anaconda-dracut: Mount /dev/mapper/live-rw (#1232411) (bcl)
- Eliminate some false test results when running glade tests. (atodorov)
- Move the knowledge about network packages into ksdata.network. (clumens)
- Add an optional conditional to progress_report. (clumens)
- Move the big block of late storage writing out of install.py. (clumens)
- The attribute is named ostreesetup.nogpg. (clumens)
- Use the index in grubenv (#1209678) (bcl)
- Do not raise an exception on EINTR from os.close or os.dup2 (dshea)
- Merge pull request #154 from mulkieran/master-959701 (mulkieran)
- Improve focus behavior in the advanced user dialog (dshea)
- Re-save advanced_user.glade (dshea)
- Depsolve kickstarted packages on the summary hub (#961280) (dshea)
- Add a kickstart test for %%packages --ignoremissing (dshea)
- Remove descriptions for RAID levels (#959701) (amulhern)
- No kexec-tools on aarch64 (bcl)

* Fri Jun 19 2015 Brian C. Lane <bcl@redhat.com> - 23.11-1
- Do not import iutil from flags (dshea)
- Ignore EINTR errors in files unlikely to encounter them (dshea)
- Reimplement the open override for the dracut scripts (dshea)
- Wrap the only non-open call found by the new pocketlint checks (dshea)
- Redefine open to retry on EINTR (dshea)
- Remove __future__ imports (dshea)
- Use python 3's OSError subclasses instead of checking errno (dshea)
- Allow kwargs in eintr_retry_call (dshea)
- Remove explicit uses of /dev/null (dshea)
- Do not retry calls to close or dup2 (dshea)
- Remove another function from isys (dshea)
- Make dialogs behave better with timed input validation (dshea)
- Fix the password/confirm checks to work with delayed validation (dshea)
- Move the URL protocol removal out of the input check (dshea)
- Remove the vestigal capslock label from the password spoke (dshea)
- Re-saved a few glade files (dshea)
- Run set_status unconditionally from update_check_status (dshea)
- Do not run input checks for every keystroke of input (#1206307) (dshea)
- Add a method to execute timed actions early (dshea)
- Use comps.environments instead of comps.environments_iter (#1221736) (dshea)
- Merge pull request #83 from mulkieran/master-requires (mulkieran)
- Only show supported autopart choices in choices combo. (amulhern)
- Strip out device types that blivet is not able to support. (amulhern)
- Update blivet required version. (amulhern)
- Fix nfs4 stage2 and repo handling (#1230329) (bcl)
- Update upd-kernel so that it actually works (#1166535) (bcl)
- Fix passing ,nfsvers=3 to dracut (#1161820) (bcl)
- Require the python3 version of iscsi-initiator-utils (dshea)
- Fix the pylint pre-commit hook for python3 and pocketlint (dshea)
- Fix a type check to work with python 3. (dshea)
- Do not log Xorg output to tty5 (dshea)

* Wed Jun 10 2015 Brian C. Lane <bcl@redhat.com> - 23.10-1
- Deal with encrypted partitions not being readable by virt-cat. (clumens)
- Make use of the restore_signals Popen argument (dshea)
- Don't allow /boot on iSCSI. (#1164195) (sbueno+anaconda)
- Merge pull request #127 from mulkieran/master-kickstart (mulkieran)
- Actually distribute the clickable message test, too (dshea)
- Fix disk argument passing to virt-cat in the ostree test. (clumens)
- Relabel all password and group files in %%post (#1228489) (dshea)
- Deal with the order of ifcfg files not being guaranteed. (clumens)
- Add a __init__.py to fix up an error when running iutil_test.py. (clumens)
- Actually run the clickable message test (dshea)
- Add a false positive to pylint checking for S390Error. (clumens)
- Let the excludedocs test pass if there are only directories left. (clumens)
- Allow successful kstest results to provide more details. (clumens)
- The escrow_cert test cannot use autopart. (clumens)
- Don't warn on PyInit__isys being unused. (clumens)
- Test that root LV is encrypted. (amulhern)
- Deal with subprocess returning bytes in tests/lib/filelist.py, too. (clumens)
- Make anaconda+python3+pocketlint work. (clumens)
- Start using our new shared pylint framework in anaconda. (clumens)
- Remove our extra pylint checkers. (clumens)
- Remove a duplicate libselinux-python3 requires. (clumens)
- Run makeupdates with Python 2 for now (mkolman)
- Don't use the _safechars private property (#1014220) (mkolman)
- Make sure directory size is returned as int (#1014220) (mkolman)
- Only warn about missing yum-utils (#1014220) (mkolman)
- Make sure set_system_time() gets an integer (#1014220) (mkolman)
- Make sure the column number in TUI is an integer (#1141242) (mkolman)
- Python 3 compatible sorting fixes (#1014220) (mkolman)
- Make version comparison Python 3 compatible (#1014220) (mkolman)
- Don't apply numeric comparison on None (#1141242) (mkolman)
- Avoid comparing None to an integer (#1141242) (mkolman)
- Handle urllib split (#1014220) (mkolman)
- Don't try to decode strings (#1014220) (mkolman)
- Rename function attributes (#1014220) (mkolman)
- Replace raw_input() with input() (#1014220) (mkolman)
- Make iterators and their usage Python 3 compatible (#1014220) (mkolman)
- Convert Python 2 metaclass magic to Python 3 metaclass magic (#1014220)
  (mkolman)
- Make the raise syntax Python 3 compatible (#1014220) (mkolman)
- Python 3 no longer does tuple parameter unpacking (#1014220) (mkolman)
- Make isys Python 3 compatible (#1014220) (mkolman)
- Set a correct mode for the tempfile (#1014220) (mkolman)
- Python 3 temp files no longer reflect external changes (#1014220) (mkolman)
- Make print usage Python 3 compatible (#1014220) (mkolman)
- Rename the warnings spoke to warnings_spoke (#1014220) (mkolman)
- Replace list comprehension with for at class level (mkolman)
- Make gettext usage Python 3 compatible (#1014220) (mkolman)
- Do not open tty5 for writing in the "a" mode (#1014220) (vpodzime)
- Do not use pykickstart's RepoData as a key in a dict (#1014220) (vpodzime)
- Do not run repo attrs' checks if they are not set up yet (#1014220)
  (vpodzime)
- Don't depend on side effects of map() (#1141242) (mkolman)
- Don't use exceptions' message attribute (#1014220) (vpodzime)
- Addapt to string type changes (#1014220) (mkolman)
- Handle modules returning bytes in Python 3 (#1014220) (mkolman)
- Add and use function that makes sure we work with strings (#1014220)
  (vpodzime)
- Handle modules requiring different string types in Python 3 (#1014220)
  (mkolman)
- Remove sitecustomize (#1014220) (mkolman)
- Make ASCII conversions Python compatible (#1014220) (mkolman)
- Remove "is Unicode" tests (#1014220) (mkolman)
- Fix ASCII conversion tests (#1014220) (mkolman)
- Return a string when calling a program (#1014220) (mkolman)
- Handle subprocess returning bytes (#1014220) (mkolman)
- Handle latin-1 strings in locale -a output (#1014220) (mkolman)
- Open the VNC password file for binary writing (#1014220) (mkolman)
- Update parse-kickstart for python3 (#1014220) (bcl)
- Update driver-updates for python3 (#1014220) (bcl)
- Update python-deps for python3 (#1014220) (bcl)
- Add a test for parse-kickstart (#1014220) (bcl)
- Make the import Python 3 compatible (#1014220) (mkolman)
- Change configparser and queue imports (#1014220) (mkolman)
- Remove imports from the __future__ (#1014220) (mkolman)
- Use the imp module directly (#1014220) (mkolman)
- Use Python 3 versions of Python dependencies  (#1014220) (mkolman)
- Use /usr/bin/python3 in scripts (#1014220) (mkolman)
- Use Python 3 versions of nose and Pylint (#1014220) (mkolman)
- Build the Anaconda widgets for Python 3 (#1014220) (mkolman)
- Update makebumpver for python3 (#1014220) (bcl)
- Fix Kickstart installation without default gateway errors out (jkonecny)
- Fix results checking in a couple ks tests. (clumens)

* Wed Jun 03 2015 Brian C. Lane <bcl@redhat.com> - 23.9-1
- Fix a usage typo in run_once_ks script. (sbueno+anaconda)
- Add kickstart tests for keyboard settings. (sbueno+anaconda)
- Add a kickstart test for lang settings. (sbueno+anaconda)
- Fix a %% call inside _(). (clumens)
- Convert ntp-pools.* to using the new kstest functions and autopart. (clumens)
- Fix up the expected output in parse-kickstart_test.py. (clumens)
- Fix a couple more pylint problems in the s390 code. (clumens)
- Use the adapted Timezone class for kickstart data (vpodzime)
- Add a kickstart test for processing NTP servers/pools configuration
  (vpodzime)
- Show error on invalid username attempts in TUI. (#1171778) (sbueno+anaconda)
- Fix dracut reads ksdevice from missing os enviromnent (jkonecny)
- Run kickstart tests through an LMC-like program, not LMC itself. (clumens)
- Move common kickstart_test code out into its own functions.sh file. (clumens)
- Switch to using autopart in the kickstart tests. (clumens)
- Fix a couple pylint errors. (sbueno+anaconda)
- Make anaconda changes necessary for libblockdev s390 plugin.
  (sbueno+anaconda)
- Add a kickstart test for lvm with percentage-based sizes. (dlehman)
- Add kickstart test for basic fixed-size lvm layout. (dlehman)
- Add a kickstart test to validate the default fstype. (dlehman)
- Add kickstart test to test bond interface creation (jkonecny)
- Add kickstart test to test vlan creation (jkonecny)
- Fix --device=link and --device not specified (#1085310) (rvykydal)
- Add kickstart test to test hostname (jkonecny)
- Add a /boot to tmpfs-fixed_size.ks. (clumens)
- Fix bad warning message when user set illegal IP (jkonecny)
- Fix bad check of illegal ip address (jkonecny)
- Add a simple tmpfs kickstart test (mkolman)
- Add a kickstart test for escrow packets and backup passphrases (dshea)
- Fix a typo that caused us to discard corrected target sizes. (#1211746)
  (dlehman)
- Don't pass anything to ./configure. (dshea)
- Fix a pylint problem in parse-kickstart_test.py. (clumens)
- Fix 0 choice in Language and Storage in TUI mode (jkonecny)
- Update html documentation for new boot-options section (bcl)
- Convert boot-options to ReST and include it in the Sphinx documents. (bcl)

* Fri May 15 2015 Brian C. Lane <bcl@redhat.com> - 23.8-1
- Clean up after processKickstart in parse-kickstart_test.py. (clumens)
- Add support to dnfpayload.py for addon NFS repos. (clumens)
- Fix IndexError: list index out of range (#1219004) (jkonecny)
- Fix a typo in proxy-kickstart.sh that was causing a test time out. (clumens)
- iSCSI Name Validation using regexes (sujith_pandel)
- Add kickstart tests for proxy usage. (dshea)
- In dracut, do not display a warning for network lines with just a hostname.
  (clumens)
- Add transport adapters to support ftp and file fetching (dshea)
- Fix for "Kickstart installation fails..." (#1197960) (jkonecny)
- Allow passing kickstart tests to be run on the command line. (clumens)
- Automatically collect environment variables to be passed to ks tests.
  (clumens)
- Use isinstance instead of type for doing type checks. (clumens)
- Remove yumpayload.py, its support files, and most references to yum.
  (clumens)
- Fix the packages-and-group wildcard exclusion test (dshea)
- Set the GUI-selected environment in the ksdata (#1192100) (dshea)
- Don't crash if the disk model is None (#1215251) (dshea)
- Correct an error message in packages-and-groups-1.ks. (clumens)
- Switch from testing for emacs* to kacst*. (clumens)
- Tests that end in a traceback are failures, not successes. (clumens)
- Don't run run_report.sh from within run_kickstart_tests.sh. (clumens)
- If a kickstart test failed due to a traceback, display that. (clumens)
- Wrap device labels earlier (#1212586) (dshea)
- Remove the angle property from the device label (dshea)
- Get rid of the find button in the filter spoke. (dshea)
- Rearrange filter.glade (dshea)
- Fix errors in the vendor column renderers. (dshea)
- Fix some minor inconsistencies in filter.glade (dshea)
- Fix issues with advanced storage searching. (dshea)
- Remove duplicate entries from search combo boxes (dshea)
- Use named IDs for the filter type combo boxes. (dshea)
- Rearrange filter.glade the way glade wants it now (dshea)
- Add a reporting support script to kickstart tests. (clumens)
- Return a specific error code when a test times out. (clumens)
- Fix indentation in run_one_ks.sh. (clumens)
- Also remove all the fonts in the packages-and-groups-1 test. (clumens)
- Enable the basic-ftp and basic-ftp-yum kickstart tests. (clumens)
- Fix a typo in groups-and-envs-2.ks (clumens)
- Get NTP pools and servers from ksdata for the runtime config (vpodzime)
- Adapt to the new argument list for save_servers_to_config. (clumens)
- Remove the restriction that /boot be below 2TB for grub (#1082331) (dshea)
- Distinguish between NTP pools and servers in GUI (vpodzime)
- Add support for chrony pool directive (mlichvar)
- Add a readme pointing to the documentation (bcl)
- Sphinx docs - use source order (bcl)
- Add html documentation for Anaconda v23.7 (bcl)
- Place html docs under ./docs/html/ (bcl)
- Configure proxy settings for dnf payload (#1211122) (bcl)
- Change online action to change (bcl)
- Check for images/install.img first for netboot (bcl)
- Ignore addon and anaconda sections in handle-sshpw (bcl)
- Ignore %%anaconda section in parse-kickstart (bcl)
- Change of label in iscsi storage spoke (jkonecny)

* Wed Apr 22 2015 Brian C. Lane <bcl@redhat.com> - 23.7-1
- Fix doReqPartition import from autopart (bcl)
- Add support for reboot --kexec kickstart command (bcl)
- Add inst.kexec and --kexec support to reboot with kexec (bcl)
- Add setup_kexec method to prepare the system for a reboot with kexec (bcl)
- Add kickstart %%pre-install section support (bcl)
- Remove the custom help button from the toolbar (bcl)
- Use multiple streams for zRAM instead of multiple devices (vpodzime)
- iscsi: pass rd.* options of devices to be mouted in dracut (#1192398)
  (rvykydal)
- Remove the unused productName import from custom_storage_helpers.py.
  (clumens)
- Remove the old custom partitioning help dialog (mkolman)
- Implement the new reqpart command. (clumens)
- Sort disks by name when checking disk selection (vpodzime)
- Set both .format's and .originalFormat's passphrase on unlock (vpodzime)
- Make the Encrypt checkbox insensitive for encrypted non-BTRFS devices
  (#1210254) (vpodzime)
- Check for Gtk before importing escape_markup (bcl)
- If the network is disabled, also disable the network part of the source
  spoke. (#1192104) (clumens)
- Add handling for unusable storage configurations. (dlehman)
- Allow markup in the label/message of DetailedErrorDialog. (dlehman)
- Allow passing an optional button list to showDetailedError. (dlehman)
- Allow kwargs with gtk_action_wait, gtk_action_nowait decorators. (dlehman)
- Fix makeupdates handling of Release: (bcl)
- Make sure we unmount the path we mounted (bcl)
- Fix up one more back_clicked reference that got missed. (clumens)
- Don't unconditionally set ksdata.lang.seen to True (#1209927) (mkolman)
- Reset the back_clicked flag if we stay on the Storage spoke (#1210003)
  (vpodzime)
- Mark the back_clicked attribute of the Storage spoke as private (vpodzime)
- TUI pwpolicy setup was supposed to be in __init__ not refresh (#1208607)
  (bcl)
- Preserve the order of boot args added by kickstart. (clumens)
- Revert "allow /boot on btrfs subvol or filesystem" (bcl)
- Connect scroll adjustments in the right class (#1206472) (dshea)

* Thu Apr 02 2015 Brian C. Lane <bcl@redhat.com> - 23.6-1
- Enforce sane disk selections. (dlehman)
- Add a test for parse-kickstart (bcl)
- Add --tmpdir to parse-kickstart for testing (bcl)
- Use the correct format for IPMI messages. (clumens)
- Do not use min_luks_entropy with pre-existing devices (#1206101) (dshea)
- Remove the dnf cache directory when resetting the repo (dshea)
- Do not add separators to the addon list when not needed (dshea)
- Only use the instclass environment if it actually exists. (dshea)

* Fri Mar 27 2015 Brian C. Lane <bcl@redhat.com> - 23.5-1
- Mock external module dependencies for readthedocs (bcl)
- Generate the pyanaconda module documentation (bcl)
- Reformat kickstart.rst using better ReST markup (bcl)
- Add some deprecation-related false positives. (clumens)
- Add Sphinx documentation support (bcl)
- Add documentation on %%anaconda kickstart command (bcl)
- Prevent Storage spoke Done button method from multiple launch (jkonecny)
- Prevent spokes from being exited more times. (jkonecny)
- Only depend on pygobject3-base in anaconda-core (#1204469) (mkolman)
- Use proxy when configured for the base repo (#1196953) (sjenning)
- Assume UTC if setting the system time without a timezone (#1200444) (dshea)
- Add boolean as return to ThreadManager.wait (jkonecny)
- Make sure LANG is always set to something (#1201896) (dshea)
- Fix pylint/translation issues from the pwpolicy patches. (clumens)

* Fri Mar 20 2015 Brian C. Lane <bcl@redhat.com> - 23.4-1
- Clean out the mock chroot before attempting to run the rest of the test.
  (clumens)
- Implement %%anaconda kickstart section for pwpolicy (bcl)
- Add pwpolicy support to TUI interface (bcl)
- Add pwpolicy for the LUKS passphrase dialog. (bcl)
- Add pwpolicy for the user spoke. (bcl)
- Use pwpolicy for the root password spoke. (bcl)
- Add the text for weak passwords to constants (bcl)
- Add tests with an FTP instrepo (dshea)
- Add kickstart tests for an NFS instrepo and addon repos. (dshea)
- Handle /boot on btrfs for live (#1200539) (bcl)
- rpmostreepayload: write storage config after shared var is mounted (#1203234)
  (rvykydal)
- Tweak tmux configuration file (jkonecny)
- Remove --device= from the new kickstart tests. (clumens)
- Add more kickstart-based packaging tests. (clumens)
- Fix enlightbox call in ZFCPDialog. (#1151144) (sbueno+anaconda)
- fix crash with bare 'inst.virtiolog' in boot args (wwoods)
- Do not attempt to set None as a warning (dshea)
- fix inst.ks.sendmac for static ip=XXX (#826657) (wwoods)

* Fri Mar 13 2015 Brian C. Lane <bcl@redhat.com> - 23.3-1
- Only insert strings into the environment (#1201411) (dshea)
- Fix the rescue kernel version list in writeBootLoader (#1201429) (dshea)
- Missing local variable check (omerusta)
- Fix the handling of nfs:// URLs. (dshea)
- Add glob support for the -a/--add option in makeupdates (mkolman)
- White Space fixes (omerusta)
- Put all mock results into the top-level source dir. (clumens)
- Merge pull request #31 from dcantrell/master (david.l.cantrell)
- Require newt-python in anaconda-core (dshea)
- Make merge-pr executable (dshea)
- Display an error for exceptions during GUI setup (dshea)
- Remove unused invisible char properties (dshea)
- Add a check for invisible_char validity (dshea)
- Connect viewport adjustments to child focus adjustments (#1192155) (dshea)
- Support '%%packages --multilib' in dnfpayload.py (#1192628) (dcantrell)

* Fri Mar 06 2015 Brian C. Lane <bcl@redhat.com> - 23.2-1
- Add rc-release target (bcl)
- Change --skip-tx to --skip-zanata in scratch-bumpver (bcl)
- Add --newrelease to makebumpver (bcl)
- Improve the addon repo name collision code (#1125322) (bcl)
- Fix the import of mountExistingSystem (vpodzime)
- Fix import error in anaconda-cleanup. (sbueno+anaconda)
- Use the new static method to get possible PE sizes (vpodzime)
- Try using the global LUKS passphrase if none is given for LV/part (#1196112)
  (vpodzime)
- Fix the help button mnemonic display on spokes (dshea)
- Only set the hub message if the message has changed (dshea)
- Wrap the info bar in a GtkRevealer (dshea)
- Add links to clickable warning and error messages. (dshea)
- Add a test to look for clickable messages that aren't clickable enough.
  (dshea)
- Increment the widgets version number (dshea)
- Allow markup and links in the info bar. (dshea)
- Add more links to gtk-doc comments (dshea)
- Handle New_Repository name collision source spoke (#1125322) (bcl)
- Fix a bad usage of execWithRedirect (#1197290) (dshea)
- Have to be root to delete /var/tmp/kstest-* on the remote machines. (clumens)
- Use the LUKS device for swap in fstab (#1196200) (vpodzime)
- Clear TUI source spoke errors that may have been leftover from a prior
  attempt. (#1192259) (sbueno+anaconda)

* Fri Feb 27 2015 Brian C. Lane <bcl@redhat.com> - 23.1-1
- Make sure python2 dnf is required (bcl)
- Fix pykickstart requirement. (clumens)
- Extract xattrs from tar payload (#1195462) (bcl)
- Add a script to rebase and merge pull requests (dshea)
- Update translation documentation for Zanata (bcl)
- Switch translation support to fedora.zanata.org (bcl)
- install.py: fix the 'is team device' check (awilliam)
- Explain why Anaconda requires rpm-devel and libarchive-devel during build
  (mkolman)
- Revert "Switch to temporary transifex branch" (bcl)
- Revert "makebumpver needs to know about anaconda-1 transifex name" (bcl)
- Commit 23.0 anaconda.pot file (bcl)
- Rename queue.py to queuefactory.py. (clumens)
- Remove references to old_tests, which no longer exists. (clumens)
- Fix package and group removing with the dnf payload. (clumens)
- Don't try to run new-kernel-pkg if it doesn't exist. (clumens)

* Fri Feb 20 2015 Brian C. Lane <bcl@redhat.com> - 23.0-1
- Remove unused imports (dshea)
- Check for unused imports in __init__ files (dshea)
- Remove timestamp-based version support. (dshea)
- Add test lib methods to check regexes (dshea)
- Cleanup BuildRequires (mkolman)
- Remove obsolete imports. (amulhern)
- Make print statement print output w/out surrounding parentheses. (amulhern)
- Remove an unused import (dshea)
- rpmostreepayload: Honor noverifyssl (walters)
- typo: packaging: Don't vary name of "verified" (walters)
- Disable the metacity mouse-button-modifier setting (dshea)
- Fix completion setting in TUI language spoke. (#1192230) (sbueno+anaconda)
- Remove the pylint false positives for the GLib module (dshea)
- Use ExtendAction for --ignore flag (amulhern)
- Use a simple ExtendAction for add_rpms option. (amulhern)
- Fix log message formating (mkolman)
- Don't clear nonexistent DNF package download location (#1193121) (mkolman)

* Mon Feb 16 2015 Brian C. Lane <bcl@redhat.com> - 22.20-1
- Make range usage Python 3 compatible (#1014220) (mkolman)
- Make map() usage Python 3 compatible (#1014220) (mkolman)
- Make the iter*() dictionary methods Python 3 compatible (#1014220) (mkolman)
- Remove the autopart.py module from POTFILES.in (vpodzime)
- Adapt to autopart and installation-specific code move in blivet (#1192702)
  (vpodzime)
- Revert "Move autopart functionality to anaconda" (vpodzime)

* Fri Feb 13 2015 Brian C. Lane <bcl@redhat.com> - 22.19-1
- Make sure yum is included in the packageset for yumpayload (#1152753) (bcl)
- Tweak parallel args. (clumens)
- Remove the Encoding entry from the .desktop file (dshea)
- Add an option to startProgram to not reset the locale (dshea)
- Set $LIBUSER_CONF early (dshea)
- Do not set $TZ (dshea)
- Assume that a bunch of digits in a version number is a timestamp (dshea)
- Avoid setting $LANG and $LANGUAGE, except where we can't (dshea)
- Add a parameter to iutil.startProgram to extend the environment (dshea)
- Add a method to set environment variables for child processes (dshea)
- Set $DISPLAY before threads are started. (dshea)
- Add a pylint module to look for modifications to the environment (dshea)
- Remotely do kickstart tests as a kstest user instead of root. (clumens)
- Add some documentation. (clumens)
- Do all package/group checking in %%post to save a reboot. (clumens)
- Support kickstart test jobs out to multiple computers with parallel.
  (clumens)
- Make it possible to ignore individual newly added dependencies (mkolman)
- Remove the old_tests directory (bcl)
- Use /usr/bin/python2 in scripts (bcl)
- Cleanup some pylint errors in analog (bcl)

* Fri Feb 06 2015 Brian C. Lane <bcl@redhat.com> - 22.18-1
- dracut needs iscsi_firmware cmdline arg (#1185792) (bcl)
- Clear the default titlebar text (mkolman)
- Move the pygobject3 dependency to the core package (#1188850) (mkolman)
- Bump the livecd making timeout to 90 minutes. (clumens)
- If a VM isn't going to finish in 60 minutes, it likely isn't going to finish.
  (clumens)
- Check that package globs install more than just the first package. (dshea)
- Remove some stray parenthesis (#1188618) (dshea)
- Replace urllib with python-requests for network access (#1014220) (mkolman)
- The repo has moved to github, so reflect that in the spec. (clumens)
- Fix pylint problems with the autopart commit. (clumens)
- network: adapt to NM fixing virtual device disconnection (#1084953)
  (rvykydal)
- Replace xrange() with range() (vpodzime)
- Move autopart functionality to anaconda (vpodzime)

* Fri Jan 30 2015 Brian C. Lane <bcl@redhat.com> - 22.17-1
- Fix pylint complaints about log lines (bcl)
- Add JENKINS_PROXY support to makebumpver (bcl)
- Copy the kickstart package tests for testing with yum (bcl)
- Pass multiple args to runone in run_kickstart_tests.sh (bcl)
- Ignore some accelerator collisions on the filter dialog. (clumens)
- Remove an unused variable. (clumens)
- network: fix a typo making creating virtual devices in %%pre fail (#1075195)
  (rvykydal)
- network: support for bridge, require pykickstart with the support (#1075195)
  (rvykydal)
- network: Catch exception from NM failing to create a bridge device (#1075195)
  (rvykydal)
- network: add bridge support for kickstart %%pre phase (#1075195) (rvykydal)
- network: generate kickstart commands for bridge devices (#1075195) (rvykydal)
- network: add bridge support to kickstart (#1075195) (rvykydal)
- network: support for adding bridge devices (#1075195) (rvykydal)
- network: display bridge devices in status (#1075195) (rvykydal)
- Fix position of Refresh List button in filter spoke (#1065716) (rvykydal)
- Fix accelerator collision of Refresh button (#1065716) (rvykydal)
- gui: add Refresh button to network storage UI (#1065716) (rvykydal)
- iscsi: display portal (address:port) of node in node list (#1114820)
  (rvykydal)
- iscsi: when logging into nodes consider ip:port of node (#1114820) (rvykydal)
- network: display only actual fqdn of ip we offer for vnc connection
  (#1089429) (rvykydal)
- network: GUI: reactivate connection automatically after configuration
  (#1033063) (rvykydal)
- Don't traceback if connection does not have read-only setting (#1158919)
  (rvykydal)
- network: enable NM ibft plugin only for ip=ibft boot option (#804511)
  (rvykydal)
- network: add support for vlan tag in iBFT (#804511) (rvykydal)
- network: pass team opts to dracut for netroot (#1075666) (rvykydal)
- Remove unused version macros from anaconda.spec.in (vpodzime)
- Don't process continue-clicked events for windows that aren't shown.
  (clumens)
- Add back an empty %%files for the anaconda metapackage (dshea)
- Do not include dd_list and dd_extract in the anaconda-core package. (clumens)
- Replace long usage with int (#1014220) (mkolman)
- Do not use sys.exc_type (#1014220) (mkolman)
- Replace StandardError with Exception (#1014220) (mkolman)
- Make filter() usage Python 3 compatible (#1014220) (mkolman)
- network: add teamd package if team is used during installation (#1185670)
  (rvykydal)
- network: add NetworkManager-team (#1182633) (rvykydal)
- Don't allow weak LUKS passwords either (bcl)
- Use %%license in anaconda.spec.in (bcl)
- Don't allow weak passwords (text mode). (sbueno+anaconda)
- Remove the press done twice to exit text (bcl)
- Don't allow weak user passwords (bcl)
- Don't allow weak root passwords (bcl)
- Increase minimum password length to 8 (bcl)
- Remove the unused re import from nm.py. (clumens)
- Remove IPy from nm.py for python 23 compatibility. (rvykydal)
- Show empty VGs in the custom spoke. (dlehman)
- Use the rpm database to find kernel package versions (#1074358) (dshea)
- Check whether a payload has an instclass (#1185588) (dshea)
- Remove the unused indexed_dict module (vpodzime)
- Use threadMgr to wait for exception handling to finish (vpodzime)
- Add a method for waiting for error handling to finish (vpodzime)
- Move HW errors processing to the code that runs in the main thread (vpodzime)
- Replace python-urlgrabber with python-requests (#1141242) (mkolman)

* Fri Jan 23 2015 Brian C. Lane <bcl@redhat.com> - 22.16-1
- Add some tests for kickstart and package selection for dnf. (clumens)
- Double quote when printing error results from a kickstart test. (clumens)
- Restrict payload kernel versions to kernels in the payload (#1074358) (dshea)
- Actually add the new definition of an already-defined repo. (clumens)
- Move hdiso handling code to PackagePayload (#1180765) (dshea)
- Actually install the metacity theme data (dshea)
- Show the event box immediately when setting infobar messages. (dshea)
- Move environment group selection logic to PackagePayload (#1179362) (dshea)
- Add a parameter to environmentGroups for wheter to include optionlist.
  (dshea)
- Remove unused methods for deselecting environments (dshea)

* Fri Jan 16 2015 Brian C. Lane <bcl@redhat.com> - 22.15-1
- makebumpver needs to know about anaconda-1 transifex name (bcl)
- Switch to temporary transifex branch (bcl)
- Fix an issue in the previous pre-existing repo kickstart patch. (clumens)
- Require the livecd target to be larger now. (clumens)
- Hook up jenkins support into makebumpver. (clumens)
- Change default console font to eurlatgr (myllynen)
- Update help text for the nodnf option (mkolman)
- Run AnacondaExceptionHandler in cmdline mode (bcl)
- Install a metacity theme to remove the titlebar. (dshea)
- Move metacity gsettings overrides into anaconda (dshea)
- Maximize anaconda instead of running fullscreen (#1164457) (dshea)
- Use a formatter on remotelog lines (bcl)
- Include NetworkManager-glib in anaconda-core (bcl)
- Make colon optional while adding iSCSI Initiator Name (sujithpshankar)
- If using pre-existing, no size needs to be specified in ksdata (#1172172)
  (amulhern)
- Add support for sending logs to a remote host with --remotelog (bcl)
- Implement askmethod in dnfpayload (dshea)
- Add an installclass property for the default package environment (#1175826)
  (dshea)
- Fix the FIXME re: tui default software selection (dshea)
- Add missing translation contexts for TUI navigation keys (dshea)
- Translate 'c' in the tui software spoke (dshea)
- Expect addons to have categories for both GUI and TUI (vpodzime)
- Remove an unused import in pyanaconda/ui/__init__.py (vpodzime)

* Fri Jan 09 2015 Brian C. Lane <bcl@redhat.com> - 22.14-1
- Add error checks to liveimg mount code (#1178703) (bcl)
- Switch kickstart tests to doing VNC instead of graphical. (clumens)
- Updates for new Size.convertTo() spec. (amulhern)
- Force a background in the main GtkBox in anaconda windows. (dshea)
- Animate the screen transitions. (dshea)
- Implement DNFPayload.environmentOptionIsDefault (#1179905) (dshea)
- Remove the directory dnf downloaded packages into. (clumens)
- Allow specifying pre-defined repos via kickstart with dnf backend (#1177988).
  (clumens)
- Get rid of unnecessary python disable-msg in zfcp spoke. (sbueno+anaconda)
- Fix typo in commit 472be66b2af2af69e7eac15ec9c94ccc818e12b5. (dlehman)
- Fix some pylint errors in the zfcp panel. (sbueno+anaconda)
- Fix an accelerator collision found on the filter page. (sbueno+anaconda)
- Fix some issues pylint found. (sbueno+anaconda)
- Show disk paths on Other page in advstorage. (sbueno+anaconda)
- Don't treat the baserepo as special when gathering metadata (#1177502)
  (dshea)
- Make dnf._base and dnf._base.comps always available. (dshea)
- Remove the checks for whether dnf and rpm were imported (dshea)
- Remove obsolete packaging code. (dshea)
- Do not bypass name setters in the custom spoke. (#1138370) (dlehman)
- Preserve kickstart url behavior for mirrorlist (#1109933) (bcl)
- Use a backslash to escape nfs spaces instead of x20 (#1109933) (bcl)
- Add missing translation context for Add ECKD DASD button in advstorage.
  (sbueno+anaconda)
- Add translation contexts for z and zfcp panel in advstorage.
  (sbueno+anaconda)
- Convert devices size to str for GUI for zFCP devices (amulhern)
- Fix string formatting of zFCP devices. (sbueno+anaconda)
- Fix the way zFCP devices are displayed in storage spoke. (#1024902)
  (sbueno+anaconda)
- Show labels on Add zFCP dialog. (sbueno+anaconda)
- Fix failure to search by LUN in advanced storage spoke. (sbueno+anaconda)
- Get rid of the clear button in advanced storage spoke. (sbueno+anaconda)
- Fix up the z Panel in advanced storage. (sbueno+anaconda)
- Add support for adding zFCP devices in the GUI (sbueno+anaconda)
- Remove DirtyFSError related callbacks and entries. (amulhern)
- Remove allowDirty parameter from mountExistingSystem() call. (amulhern)
- Remove old workaround for missing EFI bits. (dmarlin)
- Wait for payload thread in TUI software spoke. (#1178214) (sbueno+anaconda)
- Start the network before the display (#1167103) (dshea)

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
