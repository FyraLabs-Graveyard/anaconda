Name: anaconda
Version: 11.0.2
Release: 1
License: GPL
Summary: Graphical system installer
Group: Applications/System
Source: anaconda-%{PACKAGE_VERSION}.tar.bz2
BuildPreReq: pump-devel >= 0.8.20, kudzu-devel >= 1.2.0, pciutils-devel, bzip2-devel, e2fsprogs-devel, python-devel gtk2-devel rpm-python >= 4.2-0.61, newt-devel, rpm-devel, gettext >= 0.11, rhpl, booty, libxml2-python, zlib-devel, elfutils-devel, beecrypt-devel, libselinux-devel >= 1.6, libX11-devel, libXxf86misc-devel, intltool >= 0.31.2-3, python-urlgrabber, pykickstart, yum, device-mapper >= 1.01.05-3, libsepol-devel, pango-devel, pirut, libXt-devel
Requires: rpm-python >= 4.2-0.61, rhpl >= 0.170, parted >= 1.6.3-7, booty, kudzu > 1.2.0, yum >= 2.5.1-3, pirut
Requires: pyparted, libxml2-python, python-urlgrabber
Requires: system-logos, pykickstart
Requires: device-mapper >= 1.01.05-3
%ifnarch s390 s390x
Requires: python-pyblock >= 0.7-1
%endif
%ifnarch s390 s390x ppc64
Requires: rhpxl
%endif
Obsoletes: anaconda-images <= 10
Url: http://fedora.redhat.com/projects/anaconda-installer/

BuildRoot: %{_tmppath}/anaconda-%{PACKAGE_VERSION}

%description
The anaconda package contains the program which was used to install your 
system.  These files are of little use on an already installed system.

%package runtime
Summary: Graphical system installer portions needed only for fresh installs.
Group: Applications/System
AutoReqProv: false
Requires: libxml2-python, python, rpm-python >= 4.2-0.61, yum >= 2.4.0
Requires: anaconda = %{version}-%{release}
Requires: createrepo >= 0.4.3-3.1, squashfs-tools
Requires: /usr/bin/strip

%description runtime
The anaconda-runtime package contains parts of the installation system which 
are needed for installing new systems.  These files are used to build media 
sets, but are not meant for use on already installed systems.

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

%files
%defattr(-,root,root)
%doc COPYING
%doc docs/command-line.txt
%doc docs/install-methods.txt
%doc docs/kickstart-docs.txt
%doc docs/mediacheck.txt
%doc docs/anaconda-release-notes.txt
/usr/bin/mini-wm
/usr/sbin/anaconda
/usr/share/anaconda
/usr/share/locale/*/*/*
/usr/lib/anaconda

%files runtime
%defattr(-,root,root)
/usr/lib/anaconda-runtime

%triggerun -- anaconda < 8.0-1
/sbin/chkconfig --del reconfig >/dev/null 2>&1 || :

%changelog
* Wed Mar  8 2006 Jeremy Katz <katzj@redhat.com> - 11.0.2-1
- error handling on fs label reading (#184412)
- add sis190 driver
- remove no-longer shipped lvm2-cluster on upgrade (pjones)  

* Tue Mar  7 2006 Jeremy Katz <katzj@redhat.com> - 11.0.1-1
- Fix text display for rescue CD isolinux
- Fix usb-storage not showing up by default (#181739)

* Tue Mar  7 2006 Jeremy Katz <katzj@redhat.com> - 11.0.0-1
- Really fix the file contexts on the directories (#182252)
- More fixing for Xen kernel naming
- Branched, turn off betanag

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 10.92.17-1
- fix traceback in size check
- disable size check on upgrade (clumens, #184112)
- try to catch more failures to read repo metadata (clumens)
- only do runlevel 5 if graphical install (dcantrel, #184013)
- adjust to new xen kernel package naming
- add 'vesa' flag to force the use of the vesa driver
- more meaningful error messages on conflicts (pnasrat)
- ensure some dirs are labelled correct (#182252)

* Fri Mar  3 2006 Paul Nasrat <pnasrat@redhat.com> - 10.92.16-1
- Support Everything/globs in ks (pnasrat, clumens, #177621)
- Allow changes if not enough disk space (clumens, #183878)
- Set controlling tty in rescue mode (dcantrel,#182222)
- Sort list of languages (dcantrel)

* Fri Mar  3 2006 Jeremy Katz <katzj@redhat.com> - 10.92.15-1
- conditional code is now in yum (pnasrat)
- sort network devices smarter (clumens, #166842)
- select needed fs entries (#183271)
- more serbian fixes (#182591)

* Tue Feb 28 2006 Jeremy Katz <katzj@redhat.com> - 10.92.14-1
- fix traceback in pkgorder
- don't display xen 
- make partitioning type combo wider (dcantrel)
- handle Serbian locales properly (#182591)

* Mon Feb 27 2006 Jeremy Katz <katzj@redhat.com> - 10.92.12-1
- Dependency whiteout to fix ordering (clumens)
- Fix swap on RAID in kickstart (#176537)
- Add keymap overrides
- Fix segfault with USB CD/DVD drives (#182589)

* Fri Feb 24 2006 Jeremy Katz <katzj@redhat.com> - 10.92.11-1
- fix traceback with segv handler (pjones)
- various language fixes (dcantrel)
- be clearer about askmethod (#182535)

* Thu Feb 23 2006 Jeremy Katz <katzj@redhat.com> - 10.92.10-1
- more bogl removal (dcantrel)
- make the exception dumping less braindead about things we don't 
  want dumped (clumens)
- add backtrace handler to anaconda (pjones)
- fix warnings with new yum in pkgorder
- make conditional packages on deps work (pnasrat)
- suppress some warnings (dcantrel)
- text mode language fixes (dcantrel)

* Thu Feb 23 2006 Jeremy Katz <katzj@redhat.com> - 10.92.9-1
- Fix text mode traceback (dcantrel)
- Skip a few more things in traceback dumps
- Attempt to fix pkgorder so that we require less CDs for "normal" installs

* Wed Feb 22 2006 David Cantrell <dcantrell@redhat.com> 10.92.8-1
- Removed obsolete bogl code (katzj)
- Removed unused code in upgrade.py (pnasrat)
- Check version and packages to upgrade (pnasrat)
- Removed old IDE RAID code from isys (katzj)
- Various traceback fixes
- Don't use underline in device names for hotkeys in bootloader gui (pjones)
- Mount /selinux in rescue mode (katzj)

* Tue Feb 21 2006 Chris Lumens <clumens@redhat.com> 10.92.7-1
- Give Language a default display_mode (dcantrel)
- Get languages that need a default from localeInfo (dcantrel)

* Tue Feb 21 2006 Chris Lumens <clumens@redhat.com> 10.92.6-1
- Set a default language on text mode CJK installs (dcantrel, #180417)
- Fix case-sensitive matching of devices (notting, #182231)
- Be smarter about required media (pnasrat)
- Set MTU in the loader (katzj)
- Add dev package to remove blacklist (katzj, #181593)
- Try to mount device as ext3 in hard drive installs (katzj)
- Sanity check unknown package & group names (pnasrat)
- Reboot after writing exception dump (#181745)
- Confirm in interactive kickstart installs (#181741)
- Fix showing kickstart package selection again
- Don't traceback if we find a %%include file that doesn't exist yet (#181760)
- Skip partitioning if logvol or raid is given in ks (#181806)
- Initialize UTC checkbox (#181737)

* Tue Feb 14 2006 Jeremy Katz <katzj@redhat.com> - 10.92.5-1
- Fix traceback in language group selection
- No remote save traceback button if not network (clumens)
- More fixes for minstg2.img (clumens)
- Disable next/back while installing packages (dcantrel)
- Bump minimum amounts for install, graphical and early swap
- Enable Arabic for text mode (notting)

* Tue Feb 14 2006 Jeremy Katz <katzj@redhat.com> - 10.92.4-1
- improve globbing for xen guest kernels
- Don't add a kernel if one is already selected.

* Mon Feb 13 2006 Jeremy Katz <katzj@redhat.com> - 10.92.3-1
- Don't debug log about missing help text (clumens)
- Reduce deps for pkgorder
- Updated kickstart docs (clumens)

* Mon Feb 13 2006 Jeremy Katz <katzj@redhat.com> - 10.92.2-1
- more x86_64 xen guest fixing

* Mon Feb 13 2006 Jeremy Katz <katzj@redhat.com> - 10.92.1-1
- try to fix x86_64 xen guest

* Sun Feb 12 2006 Jeremy Katz <katzj@redhat.com> - 10.92.0-1
- Fix length of package name in text install (dcantrel, #180469)
- Various minor cleanups
- Support conditional packages for langsupport (pnasrat, #178029)

* Thu Feb 09 2006 Chris Lumens <clumens@redhat.com> 10.91.19-1
- Fix loader typo.

* Thu Feb 09 2006 Chris Lumens <clumens@redhat.com> 10.91.18-1
- Add iscsi support (Patrick Mansfield <patmans AT us.ibm.com>)
- Allow retry if CD image isn't found on NFS server (#109051, dcantrel)
- Fix location of video modes data files
- Add x86_64 kernel-xen-guest (katzj)
- Better loader debugging support (katzj)

* Wed Feb 08 2006 Paul Nasrat <pnasrat@redhat.com> - 10.91.17-1
- Handle bind mounts correctly (#160911, dcantrel)
- Upgrade package black list and make upgrades work
- Disable repo conf for now 
- loader debuginfo
- kickstart - suggest fix (#174597, clumens)

* Mon Feb  6 2006 Jeremy Katz <katzj@redhat.com> - 10.91.16-1
- fix writing out instdata for root password, etc (#180310)

* Mon Feb  6 2006 Jeremy Katz <katzj@redhat.com> - 10.91.15-1
- Remove debugging code that broke showing the Xen option on the task screen
- More sqlite files (#171232)
- Fix traceback for new method pirut depends on
- Ensure /dev/root exists (Patrick Mansfield)
- Force buttonbar on main screen active in congrats (dcantrel, #179924)
- Always pass loglevel (dcantrel)
- BR libXt-devel (dcantrel)
- Don't try to make /dev/mapper devs (pjones)
- More consistency in dev naming for dmraid (pjones)
- Start of iscsi patches (Patrick Mansfield)
- Fix pre-existing RAID chunksize reading (#178291)

* Fri Feb  3 2006 Jeremy Katz <katzj@redhat.com> - 10.91.14-1
- Handle reiserfs labels (dcantrel, #125939)
- Skip more steps in root mode (Jasper Hartline)
- Update driver list for current kernels
- Don't put mapper/ in the swap label (pjones)
- Set file contexts on blkid.tab* (pjones)
- Increase logical volume label field to 32 chars (dcantrel, #174661)
- More exception trimming (clumens)
- Fix args to writeConfiguration (clumens, #179928)
- Fix format strings in label device, proper max for swap labels (pjones)
- Make task definition more dynamic
- Add a hack to remove the xen group if we're running on xen (#179387)

* Thu Feb  2 2006 Jeremy Katz <katzj@redhat.com> - 10.91.13-1
- Speed up timezone screen (clumens)
- Make kickstart interactive mode work (clumens)
- Fix package selection screen (clumens)
- Add sqlite to traceonly to help http/ftp memory usage
- Write out repo config (pnasrat)
- Fix colors on boot splashes (#178033)
- Select lang groups before going to the screen (#178673)
- Clean up handling of grub vs no boot loader (#159658)

* Thu Feb  2 2006 Jeremy Katz <katzj@redhat.com> - 10.91.12-1
- improves %%packages section some more (clumens)
- give a better error on kickstart lvm syntax errors (clumens)
- display vncconnect error messages (clumens)
- make swap labels shorter for cciss (dcantrel, #176074)
- Make /dev/root for mkinitrd (#171662)
- Use pirut stuff for graphical group selection

* Tue Jan 31 2006 Paul Nasrat <pnasrat@redhat.com> - 10.91.11-1
- Factor some yum stuff into yum
- Text Clarification (#178105)
- Don't use install only pkgs (#179381)
- Various dmraid and bootloader fixes (pjones)

* Tue Jan 31 2006 Peter Jones <pjones@redhat.com> - 10.91.10-1
- add dmraid device renaming support for kickstart (pjones)
- fix paths for expat (clumens)
- remove unused functions (clumens)

* Mon Jan 30 2006 Jeremy Katz <katzj@redhat.com> - 10.91.9-1
- Skip partition and bootloader screens if requested for textmode 
  (dcantrel, #178739)
- Don't create /etc/X11/X symlink (dcantrel, #179321)
- Add ethiopic fonts
- Fix traceback in upgrade examine (clumens)
- Free up depsolving storage (pnasrat)
- Fix group selection screen that I mistakenly removed (oops)
- Remove some dead pieces (pnasrat, katzj)

* Thu Jan 26 2006 Jeremy Katz <katzj@redhat.com> - 10.91.8-1
- Remove rpm whiteout (clumens, #178540)
- Fix text in upgrade continue button (dcantrel, #178096)
- Make %%packages in anaconda-ks.cfg shorter (pnasrat)
- Fix text-mode drawing (clumens, #178386)
- Release notes viewer fixes (dcantrel)
- Reset -> reboot (dcantrel, #178566)
- Create ia64 images again (prarit, #175632)
- Make sure boot loader screen gets skipped (clumens, #178815)
- Don't ask about VNC in kickstart
- Don't ask for keyboard under Xen if it fails
- Add more basic "task" selection screen
- Text mode group selection is better now
- Remove some dead code
- Require squashfs-tools  (clumens)
- Fix rescue mode (dcantrel)
- Don't have devices disappear out from under us (Patrick Mansfield)

* Fri Jan 20 2006 David Cantrell <dcantrell@redhat.com> - 10.91.7-1
- Save state when moving back to "upgrade or install" window (#178095).
- Eject CD when in kickstart and given --eject parameter (clumens, #177554).
- Translate combo box and comments (clumens, #178250).
- Disable backend debugging mode for writeKS().
- Added a PYTHONSTARTUP file to autoload readline, etc. (pjones).
- Write %%packages section in template kickstart file (clumens, pnasrat).

* Wed Jan 18 2006 David Cantrell <dcantrell@redhat.com> - 10.91.6-1
- i18n fixes (katzj)

* Wed Jan 18 2006 David Cantrell <dcantrell@redhat.com> - 10.91.5-1
- i386 and ppc rescue image script fixes (jkeating)
- fix kickstart package deselection (clumens, #177530)
- fix header download issues (pnasrat, #177596)
- interface improvements on scp exception dialog (clumens, #177738)
- rescue image additions (pjones, dcantrell, #155399)
- misc kickstart fixes (clumens, #178041, #177519)
- fix fetching repo data on http installs (clumens, #178001)
- add gdk-pixbuf handler for XPM images (#177994)
- timezone screen fixes (clumens, #178140)
- add LSI mptsas driver to module-info (#178130)
- dmraid fixes for kickstart installs (pjones)
- add sr@Latn to lang-table (katzj, #175611)

* Wed Jan 11 2006 Jeremy Katz <katzj@redhat.com> - 10.91.4-1
- Add xen kernels

* Wed Jan 11 2006 Jeremy Katz <katzj@redhat.com> - 10.91.3-1
- remove some unneeded bits from the ppc boot.iso to make it smaller
- fix some text display (notting, #177537)
- Misc kickstart fixes (clumens)

* Tue Jan 10 2006 Jeremy Katz <katzj@redhat.com> - 10.91.2-1
- fix hard drive installs (pjones)

* Tue Jan 10 2006 Jeremy Katz <katzj@redhat.com> - 10.91.1-1
- more ppc rescue image (jkeating)
- actually commit the dmraid fix (pjones)

* Mon Jan  9 2006 Jeremy Katz <katzj@redhat.com> - 10.91.0-1
- tweaked selection stuff a little to be the same code as pirut
- tweak exception window to have an image and be better sized (dcantrell)
- write out RAID device name (clumens)
- scroll group list properly (dcantrell)
- fix ppc rescue image (jkeating)
- dmraid detection fix (pjones)

* Fri Jan  6 2006 Jeremy Katz <katzj@redhat.com> - 10.90.25-1
- no sr@Latn yet since the po files haven't been added

* Fri Jan  6 2006 Jeremy Katz <katzj@redhat.com> - 10.90.24-1
- move a11y stuff earlier
- fix the text mode progress bar (pnasrat, #176367)
- fix ppc drive unreadable warnings (#176024)
- add serbian locales (#175611)
- preserve review checkbox between combo box selections (dcantrell, #176212)
- quote ethtool args (#176918)
- various spacing cleanups (dcantrell)
- a few fixes to the group selector (dcantrell)
- don't try to make the timezone widget bigger than screen (clumens, #176025)
- fix rescue mode traceback (clumens)
- fix message wording on package retry (clumens, #155884)
- quiet debug spew in anaconda.log (clumens, #171663)
- add ppc rescue script from jkeating (#177003)

* Tue Dec 20 2005 Jeremy Katz <katzj@redhat.com> - 10.90.23-1
- more pkgorder fixes (pnasrat)
- fix some debug spew (notting)
- segfaults in the loader should at least give us a stacktrace to work from
- fix some padding on the network screen

* Mon Dec 19 2005 Jeremy Katz <katzj@redhat.com> - 10.90.22-1
- add more encoding modules to traceonly (clumens, #175853)
- Fix text installs (pnasrat, #175773)
- Fix for yum API changes (pnasrat)
- Don't install the smp kernel even if NX is available
- Adjust to be more dynamic about colors with syslinux-splash's
- Use the selected language for default keyboard layout (clumens, #172266)
- Better naming for psuedo-filesystems in /etc/fstab (dcantrel, #176149)
- Clean up image handling for new graphics
- Don't do the splashscreen stuff anymore.  If the window is too slow to 
  appear, we should fix that instead

* Thu Dec 15 2005 Jeremy Katz <katzj@redhat.com> - 10.90.21-1
- fix pkgorder for new group code
- fix ub vs usb-storage
- remove some redundant code (clumens)

* Thu Dec 15 2005 Jeremy Katz <katzj@redhat.com> - 10.90.20-1
- Fixes for new timezone stuff (pnasrat)
- Fix transaction sorting (pnasrat)
- Enable dmraid by default

* Wed Dec 14 2005 Chris Lumens <clumens@redhat.com> 10.90.19-1
- Use system-config-date for timezone selection UI (#155271).
- Work on vnc+shell spawning (dcantrell).
- Whiteout fixes (pnasrat, katzj).
- Progress bar fixes (katzj).
- Depsolving speedups (katzj).

* Mon Dec 12 2005 Jeremy Katz <katzj@redhat.com> - 10.90.18-1
- Handle monitor configuration in kickstart via "monitor" keyword instead of 
  "xconfig" consistently (clumens)
- Fix joe as nano (#175479)
- Try to get hard drive installs working again
- First steps towards using ub
- Fix depcheck progress bar to actually give progress.  

* Sun Dec 11 2005 Peter Jones <pjones@redhat.com> - 10.90.17-1
- Full dmraid support.  (still disabled by default)

* Sat Dec 10 2005 Jeremy Katz <katzj@redhat.com> - 10.90.16-1
- Ensure upgrades to depsolve and remove db locks (pnasrat)
- Tweak for improved and sortable groups/categories
- Put back basic text-mode package selection (#175443)

* Thu Dec  8 2005 Jeremy Katz <katzj@redhat.com> - 10.90.15-1
- Fix various typos in the new group selection code (clumens)
- Support bytesPerInode on RAID (Curtis Doty, #175288)
- Stub some more for the loader to fix line-drawing chars again
- Handle file read failures better (pnasrat)
- Initial support for upgrades again (pnasrat)
- Minor padding tweaks to the UI

* Thu Dec  8 2005 Jeremy Katz <katzj@redhat.com> - 10.90.14-1
- Fix up for moved x locale data
- Remove vnc hack now that VNC knows where to look for fonts
- Don't go to text mode for no mouse (notting)
- Update to work with yum 2.5.0 cvs snap
- New package selection code
- Add new chinese font back now that we're using squashfs (#172163)
- The return of locale-archive usage

* Mon Dec 05 2005 Chris Lumens <clumens@redhat.com> 10.90.13-1
- Reword media check dialog (dcantrell, #174530).
- gcc41 compile fixes (pjones).
- Add genhomedircon, setfiles, and /etc/shells for selinux.

* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 10.90.12-1
- some release notes viewer fixing (dcantrell)
- allow %%pre scripts in an %%include (clumens, #166100)
- fix the squashfs stuff to actually work
- hack around slang not initializing utf8 mode so that we have line 
  drawing chars (#174761) 

* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 10.90.11-1
- reworded media check prompt (dcantrell, #174472)
- let's try squashfs... 

* Wed Nov 30 2005 Jeremy Katz <katzj@redhat.com> - 10.90.10-1
- Don't split transactions on not split install types (pnasrat, #174033)
- Fix None vs "" for vncpasswd in test mode (Patrick Mansfield)
- Make release notes viewer as large as the screen (dcantrell)
- Allow system-logos instead of fedora-logos for the package name
- Try to build SELinux policy so that things work with selinux 
  2.x policy (#174563)

* Tue Nov 29 2005 Chris Lumens <clumens@redhat.com> 10.90.9-1
- Another stab at including email.Utils everywhere (#173169).
- Remove unneeded isys.sync calls (pjones).
- Fix /dd.ig in initrd (Dan Carpenter).
- Report no DNS servers if a hostname used (pnasrat, #168957).
- Fix ppc32 from CD (katzj, #174135).
- Don't look for hdlist when booting CD1 and using FTP/HTTP (katzj).
- Fullscreen release notes viewer (dcantrell).

* Mon Nov 21 2005 Jeremy Katz <katzj@redhat.com> - 10.90.8-1
- don't load pcspkr on ppc to avoid crashes on the g5

* Sun Nov 20 2005 Jeremy Katz <katzj@redhat.com> - 10.90.7-1
- fix backwards whiteout handling (#173738)
- fix bug in depsolver which would bring in a package for an already 
  satisfied dep

* Sat Nov 19 2005 Jeremy Katz <katzj@redhat.com> - 10.90.6-1
- fix removal of packages to not traceback
- fix anaconda.dmraid logging (clumens)

* Fri Nov 18 2005 Paul Nasrat <pnasrat@redhat.com> - 10.90.5-1
- Disable sqlite cache for pkgorder
- Fix for new selinux context types (katzj)
- vnc parameter handling (clumens)
- Add ellipsis (notting)

* Thu Nov 17 2005 Jeremy Katz <katzj@redhat.com> - 10.90.4-1
- don't traceback on unresolvable deps (#173508)
- fix pkg.arch for %%packages
- another hack for vnc
- debug prints to log.debug (#173533)

* Thu Nov 17 2005 Paul Nasrat <pnasrat@redhat.com> - 10.90.3-1
- Add group processing to buildinstall
- Add createrepo requires

* Thu Nov 17 2005 Jeremy Katz <katzj@redhat.com> - 10.90.2-1
- more pkgorder fixing (clumens)
- fix cd installs to not fall into the "not a real install method" case :)

* Thu Nov 17 2005 Jeremy Katz <katzj@redhat.com> - 10.90.1-1
- add handling for dmraid/nodmraid
- fix removals of packages which have already been removed
- turn off dmraid by default
- fix pkgorder (clumens)

* Thu Nov 17 2005 Jeremy Katz <katzj@redhat.com> - 10.90.0
- more tree build fixes
- fix group removal 
- non iso install fixes (clumens)
- pkgorder fixing (clumens)
- dmraid support (pjones)
- crude language support group hack

* Wed Nov 16 2005 Chris Lumens <clumens@redhat.com> 10.89.20.1-1
- Fix indentation.

* Wed Nov 16 2005 Paul Nasrat <pnasrat@redhat.com> - 10.89.20-1
- Restore YumSorter for pkgorder
- Single anaconda installer yum class
- Switching CD method 

* Wed Nov 16 2005 Jeremy Katz <katzj@redhat.com> - 10.89.19.1-1
- be explict about pango-devel being needed

* Wed Nov 16 2005 Jeremy Katz <katzj@redhat.com> - 10.89.19-1
- Fix vt switching with modular X
- Lots of CD install fixes (clumens, pnasrat)
- Clean up exception dump stuff
- Some more steps towards dm-raid support (pjones)
- Log info messages

* Wed Nov 16 2005 Jeremy Katz <katzj@redhat.com> - 10.89.18-1
- remove new chinese font since its too big for cramfs (#172163)
- Fix typo in trimpciids (notting)
- Don't build locale-archive for now since its too big for cramfs

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> - 10.89.17-1
- missed an x lib somehow

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> - 10.89.16-1
- lots of updates for modular X
- allow a shell on tty1 if using vnc
- various fixes for cd/install method stuff (pnasrat, clumens, katzj)
- install smp kernel if NX present (#172345)
- work with multiple videoaliases files (notting)

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> - 10.89.15-1
- fix up for new selinux policy

* Mon Nov 14 2005 Paul Nasrat <pnasrat@redhat.com> 10.89.14-1
- Move sorter for CD/pkgorder into yuminstall
- Add support for ub devices (katzj)

* Mon Nov 14 2005 Paul Nasrat <pnasrat@redhat.com> 10.89.13-1
- Reinstate image based install methods (excluding hd for now)
- Clean up install method classes
- device-mapper support (pjones)
- Log warning on no network link (katzj)
- Clean up error handling for pkgorder (clumens)

* Fri Nov 11 2005 Chris Lumens <clumens@redhat.com> 10.89.12-1
- Add buildreq for yum (katzj)
- Fix loader log levels (katzj)
- Add more libraries for dogtail (katzj)

* Thu Nov 10 2005 Jeremy Katz <katzj@redhat.com> - 10.89.11-1
- Fix stdout logging to print stuff (clumens)
- Start of some sorting/splitting stuff for CDs (pnasrat) 
- Make missing modules lower priority
- Look for xen devices
- Add some of the necessary requirements to try to get dogtail working (#172891)

* Thu Nov 10 2005 Chris Lumens <clumens@redhat.com> 10.89.10-1
- Add e2fsprogs-libs to the install images.

* Wed Nov  9 2005 Jeremy Katz <katzj@redhat.com> - 10.89.9-1
- Create interface earlier to prevent kickstart traceback (clumens)
- Logging fixes, everything should be in the logfile (clumens)
- Get rid of help which is irrelevant
- Clean up loader log levels

* Tue Nov  8 2005 Jeremy Katz <katzj@redhat.com> - 10.89.8-1
- Fix backwards message on upgrade (#172030)
- New chinese fonts (#172163)
- Don't try to update a progress window that's already popped (clumens, #172232)
- Fix snack deprecation warnings (clumens, #172232)
- Get rid of some cruft in traceback dumps (clumens)
- Add a method to check for "real" consoles, add xen console to the list 
  of weird stuff
- Basic support for transaction errors other than tracebacks...
- Fix a kickstart traceback for authconfig
- Add xenblk and xennet to module-info

* Mon Nov  7 2005 Jeremy Katz <katzj@redhat.com> - 10.89.7-1
- More detailed error logging (pnasrat)
- Add bnx2 driver (pjones)
- Various kickstart fixes (clumens, #172356)
- Fix shadow password convert (clumens)

* Fri Oct 28 2005 Jeremy Katz <katzj@redhat.com> - 10.89.6-1
- Make char devices slightly later to avoid tracebacks during tree compose
- Extract kernel-xen-guest for vmlinuz and initrd in images/xen
- Kickstart fix (clumens)
- Add some support for xen xvd blockdevs
- Select kernel-xen-guest as appropriate
- Ensure proper arch of glibc is selected (#171997)
- Select all proper multilib parts of a package (#171026) 

* Thu Oct 27 2005 Jeremy Katz <katzj@redhat.com> - 10.89.5-1
- Another fix for kickstart + help hiding
- Fix finding of kernel type
- Make synaptics device nodes before X starts (clumens)
- Use nofb by default
- Add pycairo stuff (clumens)
- Set minimum displayed log level to WARNING, everything is still in 
  the logfiles (clumens)
- Try to clean up syslog (clumens)
- Allow installation of hypervisor + xen host kernel by booing with 'xen0' on 
  the installer command line
- Fix x86_64 traceback

* Mon Oct 24 2005 Jeremy Katz <katzj@redhat.com> - 10.89.4-1
- changed the wrong field in lang-table

* Mon Oct 24 2005 Jeremy Katz <katzj@redhat.com> - 10.89.3-1
- don't do xsetroot anymore
- allow retrieving updates.img with 
  updates=(http|ftp)://host/path/to.img (clumens)
- some upd-instroot fixes (clumens)
- only get yum filelists when needed (pnasrat)
- clean up exception scp'ing (clumens)
- don't write empty authconfig line (clumens, #171558)
- make kickstart errors report line number of error (clumens)
- select most appropriate kernel (kernel-smp, etc)
- ensure we get a boot loader package installed
- minor fix for ia64 image creation
- tweaks to backend setup 
- don't have help as visible in the glade file so we don't have the pane 
  appear when doing a kickstart install
- use pl2 keymap for Polish (3171583)
- allow passing product information with env vars to help live cd

* Thu Oct 20 2005 Jeremy Katz <katzj@redhat.com> - 10.89.2-1
- fix references to second stage module stuff that caused breakage

* Thu Oct 20 2005 Jeremy Katz <katzj@redhat.com> - 10.89.1-1
- fix for mkcramfs -> mkfs.cramfs
- Use minstg2.img instead of netstg2.img/hdstg2.img in the loader

* Thu Oct 20 2005 Jeremy Katz <katzj@redhat.com> - 10.89.0-1
- Fix SELinux policy loading (clumens)
- Fix translation import for kickstart (laroche)
- Add yumcache (pnasrat)
- Upgrade blacklisting (pnasrat)
- Clean up exception copying (clumens)
- Improve text mode exception dialog too (clumens)
- Don't allow bootable partitions on XFS
- Some speed improvements, progress bars, etc for package stuff (pnasrat)
- Clean up image creation, move all modules to initrd.img.  

* Fri Oct 14 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.32-1
- fix typo causing traceback (pnasrat)
- Create character device nodes to fix synaptics (clumens)

* Wed Oct 12 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.31-1
- Handle missing metadata (pnasrat)
- Give indication of kickstarts scriptlets running (#170017)
- Fix a traceback with RAID (#170189)
- Fix an FTP install traceback (#170428)
- Clean up floppy stuff (clumens)
- Clean up some warnings (clumens)
- Make IDE device node creation cleaner
- Change location of modes data files

* Mon Oct 10 2005 Chris Lumens <clumens@redhat.com> 10.3.0.30-1
- Fix requirements for s390, s390x, ppc64.
- Fix typo in scripts/upd-instroot.

* Fri Oct 07 2005 Chris Lumens <clumens@redhat.com> 10.3.0.29-1
- Deal with new load_policy. (katzj)
- Create an SELinux config. (katzj)
- Use rhpxl instead of rhpl for X configuration.
- Use pykickstart.

* Wed Oct 05 2005 Chris Lumens <clumens@redhat.com> 10.3.0.28-1
- Add yuminstall (katzj, #169228)
- Skip bootloader screen unless modifying partitions (katzj, #169817)
- Don't skip manual partitioning on custom (katzj, #169001)
- Partitioning UI fixes (katzj)
- Don't overwrite empty strings in ksdata with None.
- Move kickstart file handling into pykickstart package.
- Kickstart LVM and RAID partitioning fixes.

* Fri Sep 30 2005 Chris Lumens <clumens@redhat.com> 10.3.0.27-1
- More kickstart script fixes.

* Tue Sep 27 2005 Chris Lumens <clumens@redhat.com> 10.3.0.26-1
- kickstart script fixes

* Sat Sep 24 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.25-1
- single ppc boot images stuff from dwmw2 (pnasrat, #166625)
- ppc netboot stuff from dwmw2 (pnasrat, #165239)
- fix some of the yum backend for yum changes
- Add a button to the traceback dialog to allow saving via scp (clumens)
- Don't load the parallel port module (#169135)
- Fix group deselection to not remove everything
- Move repo setup and group selection earlier (pnasrat)

* Tue Sep 20 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.24-1
- Some kickstart %packages fixes (clumens)
- Don't copy null bytes into syslog (clumens)
- New exception dialog (clumens)
- Fix a traceback (pnasrat)
- FTP/HTTP installation might now work (pnasrat)
- Very basic group selection in the UI

* Mon Sep 19 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.23-1
- fix a silly typo that would cause tracebacks
- Look for help in /tmp/updates too (#168155)
- Add skge driver (#168590)
- Some fixes to hopefully get x86_64 trees working

* Fri Sep 16 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.22-1
- Fix segfaults with nfs mounting
- Start of url install methods (pnasrat)
- Basic package/group selection is back in kickstart
- Macro magic fixups
- Use onboot by default for network devices in kickstart

* Thu Sep 15 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.21-1
- Run pre scripts for kickstart (clumens)
- Another tree fix
- Handle NULL for device->driver from kudzu (notting)
- Clean up internal mount stuff to be more extend-able 

* Wed Sep 14 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.20-1
- Fix runlevel setting (pnasrat)
- More dead stuff fixing.

* Tue Sep 13 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.19-1
- Fix pcmcia import traceback
- Some more kickstart fixing (clumens)
- Make SELinux/firewall defaults be done by the objects, not in the UI
  - This fixes booting with selinux=0, policy load failure, etc
- Allow sparse updates.img with yum, urlgrabber and rpmUtils too
- Some dead code removal
- PCMCIA for the loader again (notting)
- install.log tweaking

* Mon Sep 12 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.18-1
- Add back genhdlist to try to fix multiarch composes (pnasrat)
- Really fix disabling of upgrades
- Some typo fixes for X configuration and post-install config
- Remove some dead code related to boot disks, using fdisk/fdasd, X 
  configuration, pcmcia
- Move ppc X stuff to rhpl (clumens)
- Fix some kickstart stuff (clumens)
- Fix RPM logging output -> the log file
- Use gtkhtml2 for release notes

* Fri Sep  9 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.17-1
- more X fixage
- build against new kudzu that doesn't segfault :)

* Fri Sep  9 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.16-1
- More typo fixes (notting)
- Fix rhpl requires

* Fri Sep  9 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.15-1
- Fix typo that broke image building.
- Start of getting post-install stuff working (pnasrat)

* Fri Sep 09 2005 Chris Lumens <clumens@redhat.com> 10.3.0.14-1
- logging fix when running in test mode

* Fri Sep 09 2005 Bill Nottingham <notting@redhat.com> 10.3.0.13-1
- adapt to new X driver model in kudzu and associated rhpl changes
- pcitable/modules.pcimap/modules.usbmap are no longer used in probing;
  remove support for them and add modules.alias usage
- Turn off help (katzj)
- Kickstart fixes (clumens)

* Wed Sep 07 2005 Paul Nasrat <pnasrat@redhat.com> 10.3.0.12-1
- yum backend selinux file_context 
- Start using new kickstart code (clumens)
- Error handling and messages for kickstart (clumens)
- Partitioning kickstart fixups (clumens)

* Thu Sep 01 2005 Paul Nasrat <pnasrat@redhat.com> 10.3.0.11-1
- Yum backend work (macro support, whitelist)
- qla2100 (katzj, #167065)
- Kickstart Parser (clumens)
- authconfig handling changes (clumens)
- Autopartitiong Traceback fix (katzj)

* Fri Aug 26 2005 Jeremy Katz <katzj@redhat.com>
- More work from pnasrat on getting the yum backend working
- Don't set some irrelevant network TYPE= (#136188, #157193)
- New and improved autopartitioning screen

* Fri Aug 19 2005 Paul Nasrat <pnasrat@redhat.com> 10.3.0.10-1
- Working towards new backend architecture

* Thu Aug 18 2005 Chris Lumens <clumens@redhat.com> 10.3.0.9-1
- Rebuild for new cairo.
- Add support for ksdevice=bootif (Alex Kiernan, #166135).
- Fix /dev/tty3 logging problems.
- Add support for Pegasos machines (dwmw2, #166103).
- Switch to Sazanami font (#166045).
- Fix for autopart not in lvm (msw).

* Mon Aug 15 2005 Chris Lumens <clumens@redhat.com> 10.3.0.8-1
- Remove dead --ignoredeps code (katzj, #165224).
- New logging system with log levels and remote logging capabilities.
- Fix typo in network code (pnasrat, #165934).
- Fix buffer overrun in md5sum code (Dustin Kirkland).
- Add mptspi and mptfc drivers (katzj).
- Timestamp fixes (dgregor, #163875).

* Thu Jul 21 2005 Chris Lumens <clumens@redhat.com> 10.3.0.7-1
- Remove firewall configuration screen.  Open SSH by default and set
  SELinux to enforced.

* Wed Jul 20 2005 Paul Nasrat <pnasrat@redhat.com> 10.3.0.6-1
- Ensure boot flag only on correct partition on pmac (#157245)
- Plug in yum for nfs:/ by default
- Include sungem_phy for pmac

* Wed Jul 13 2005 Chris Lumens <clumens@redhat.com> 10.3.0.5-1
- Fix pygtk bug on progress bars.
- Bump ia64 boot.img size (katzj, #162801).
- Fix for clearpart --none (katzj, #162445).
- yum dependancy fixes (pnasrat).
- name.arch fix for kickstart (pnasrat).
- Fix multiple NICs in kickstart config files (#158556).

* Thu Jul 07 2005 Paul Nasrat <pnasrat@redhat.com> 10.3.0.4-1
- Select kernel-devel (katzj #160533)
- Fixups for ia64 images from prarit (katzj #162072)
- Include yum libraries in stage2
- Remove gzread.py (clumens)

* Wed Jun 29 2005 Chris Lumens <clumens@redhat.com> 10.3.0.3-1
- Mount "auto" filesystems on upgrade (#160986).
- Add cairo for new pango/gtk (katzj).
- Delete labels on swap and ext3 partitions before formatting.
- Remove langsupport keyword from kickstart.

* Mon Jun 20 2005 Bill Nottingham <notting@redhat.com> - 10.3.0.2-1
- fix genhdlist

* Fri Jun 17 2005 Jeremy Katz <katzj@redhat.com> - 10.3.0.1-1
- Fix release notes for ftp installs (#160262)
- Fix fd leak in edd support (Jon Burgess, #160693)
- Fix typo breaking pseries console (pnasrat, #160573)
- Allow ignoring packages without specifying the arch (clumens, #160209)
- Add gpart (clumens, #55532)
- Some warning fixes.
- Use full bterm font if available (#159505)
- Fix quoting of pvs in anaconda-ks.cfg (#159193)
- Fix segfault on upgrades
- String tweaks (clumens, #159044, #156408)
- Don't traceback on preexisting RAID (clumens, #159079, #159182)
- Fix display size of PVs (clumens, #158696)
- Don't consider drives without free space for partitions (pjones)
- Langsupport fixes (clumens, #154572, #158389)
- Hack around usb-storage slowness at finding devices that leads to the 
  reload not occurring
- Handle FC3 swap label format and convert to right format (#158195)
- Only set things up to change the default kernel if we're booting us (#158195)
- Fix deps on upgrades (#157754)
- Try to keep install screen from moving with length of strings
- Fix autopart problem leaving some freespace the size of where you 
  started your partition growing
- Allow excluding name.arch in kickstart (Dave Lehman, #158370)
- Don't spew an error if essid or wepkey isn't set (#158223)
- Add megaraid and other new drivers (#157420) 
- Left pad RAID uuid (clumens, #136051)
- synaptics tweak (pnasrat)
- Fix telnetd to use devpts instead of legacy ptys (#124248)

* Thu May 19 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.64-1
- Handle longer arch strings (notting)
- Fix traceback in network screen (#158134)
- Include synaptics for X config (pnasrat)
- Magic boot for mac vs mac64 on disc1/dvd (pnasrat)
- Bump point at which we use graphical stage2 for http/ftp (#157274)
- Use uuid in mdadm.conf, stop using copy of md.h (#136051)
- Support deletion of bootloader entries in text mode (#125358)
- Support RAID /boot on pSeries along with handling of multiple PReP 
  partitions (Dustin Kirkland)

* Tue May 17 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.63-1
- add arch to buildstamp (notting, #151927)
- Fix am.po format strings

* Tue May 17 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.62-1
- Fix execcon used for anaconda (pjones)
- Fix traceback on tui netstg2.img install (#157709)
- Fix various splittree bugs (clumens, #157722, #157721, #157723)
- Blacklist perl.i386 on x86_64 to be removed on upgrade (pnasrat, #156658)
- Fix drive sorting (clumens)
- Remove %%installclass support for kickstart since it's never worked (#149690)
- Fix name.arch in packages (pnasrat)
- Remove bogus pre-existing RAID info on kickstart installs (clumens, #88359)
- Pretend to have nano in the rescue environment
- Don't load stage2.img into RAM for rescue mode if booted 
  with 'linux text' (#155398)

* Thu May  5 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.61-1
- and fix pkgorder for the gfs stuff

* Thu May  5 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.60-1
- Better handling of the langsupport group (clumens)
- Don't install the gfs stuff for all kernel variants, that brings in 
  kernel-smp on an everything install (#156849)
- Don't grow a partition beyond the largest freespace on a drive
- HFS+ support
- Pull in more selinux policy files to try to get /home labeled right
- Fix typo causing segfault (pnasrat)

* Tue May  3 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.59-1
- Try to use the fb res on pmac
- Always reset terminal attrs on ppc (notting, #156411)
- Remove bogus preexisting LVM info when doing kickstart 
  installs (clumens, #156283)

* Mon May  2 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.58-1
- Beep on CD insertion, not after
- Fix language support selection (clumens)
- Fix nfsiso (clumens)
- Misc X config fixes for ppc.  Boot with "usefbx" to use fbdev 
  instead again (#149188)

* Thu Apr 28 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.57-1
- Fix bind mounts (clumens, #151458)
- Fix hard drive installs (clumens)
- Re-add bluecurve icons
- Attempt to fix Chinese

* Wed Apr 28 2005 Peter Jones <pjones@redhat.com> - 10.2.0.56-1
- Fix mediacheck calls from cdinstall.c, and make mediacheck.c include
  its own header so typechecking works.

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.55-1
- Don't spam about package downloads in cmdline mode (#155250)
- Apply jnovy's patch to fix space calculations for > 2 TB devices (#155709)
- Set default font for CJK better (clumens, #156052)
- Add --label for part in kickstart (clumens, #79832)
- Ensure decimal IP addrs (#156088)
- Apply patch from Joe Pruett for rpmarch= fixes (#101971)
- Don't set SUPPORTED unnecessarily (#115847)
- Give more room for cyl #s (#119767)
- Bump size of diskboot.img
- Add back button for required media message (#114770)
- Fix lvs showing up with a mountpoint of 0 (#153965)
- Nuke some debug code
- Don't try to unmount (tmpfs) /dev
- Write a minimal mtab to avoid fsck/mount complaints (pjones)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.54-1
- Only select kernel-smp that matches the arch of kernel (#149618)
- Apply the read of Dustin Kirkland's checkpoint fragment sum patch
- Fix order of retry/reboot (#155884)
- Probe macio (pnasrat, #154846)

* Tue Apr 26 2005 Chris Lumens <clumens@redhat.com> 10.2.0.53-1
- Beep at CD prompt and on install completion (katzj, #109264, #116681).
- Add kernel-smp-devel and kernel-hugemem-devel to exclude list (katzj).
- Fix buffer overflow when CD/DVD images are several directories deep
  (#154715).
- Fix media check (pjones).
- Set language on CD and no pass installs (#149688).
- Fix disappearing button bar (#151837).
- Upgrade PReP on iSeries (pnasrat).

* Thu Apr 21 2005 Chris Lumens <clumens@redhat.com> 10.2.0.52-1
- Allow mediacheck in kickstart (katzj, #116429)
- Check for a drive being selected in autopart (katzj, #124296)
- Fix traceback in language selection screen (#155103)
- Mark "Downloading" for translation (katzj, #155214)
- Applied Dustin Kirkland's checkpoint fragment sum patch for mediacheck.
- Make anaconda-ks.cfg ro (pnasrat)
- Ensure there are <= 27 RAID members (katzj, #155509)
- Fix fsoptions for preexisting partitions in kickstart (#97560).

* Fri Apr 15 2005 Chris Lumens <clumens@redhat.com> 10.2.0.51-1
- Decode source URL for writing to anaconda-ks.cfg (#154149).
- Add kernel-xen?-devel to the exclude list (katzj, #154819).
- Fix text wrapping (#153071, #154786).
- Various UI fixes.
- Select language packages for all selected languages (#153748, #154181).

* Wed Apr 13 2005 Peter Jones <pjones@redhat.com> - 10.2.0.50-1
- revert last week's nptl hack in upd-instroot

* Wed Apr 13 2005 Peter Jones <pjones@redhat.com> - 10.2.0.49-1
- Cut summaries off to avoid layout problems (katzj, #154459)
- Add script to update loader in initrd (katzj)
- Typo fixes in upgrade.py (katzj, #154522)
- Fix rescue mode network enabling (katz, #153961)
- Add libaudit to the graphical stage2 file list, for Xorg
- Various language fixes (clumens, #152404)

* Mon Apr 11 2005 Peter Jones <pjones@redhat.com> - 10.2.0.48-1
- Typo fixes in gui.py (menthos, #154324)
- Don't try to do early swap in test mode, and use yesno not okcancel (msw)
- If the install language is an unknown locale, use en_US.UTF_8
- Fix upgrade to make devices available in the changeroot

* Thu Apr  7 2005 Peter Jones <pjones@redhat.com> - 10.2.0.47-1
- put ncurses in the net images, too.
- (notting) put redhat-artwork in the GR images.

* Thu Apr  7 2005 Peter Jones <pjones@redhat.com> - 10.2.0.46-1
- put readline in the net images
- fix linxuthreads warnings in upd-instroot
- (clumens) fix build-locale-archive

* Wed Apr  6 2005 Elliot Lee <sopwith@redhat.com> - 10.2.0.45-1
- Deal with GUI-mode language traceback

* Wed Apr  6 2005 Elliot Lee <sopwith@redhat.com> - 10.2.0.44-1
- Deal with text-mode language traceback
- (clumens) Don't set SYSFONTACM 

* Wed Apr 06 2005 Peter Jones <pjones@redhat.com> - 10.2.0.43-1
- Don't remove libraries in stage2 that don't match the one from linuxthreads/

* Tue Apr 05 2005 Peter Jones <pjones@redhat.com> - 10.2.0.42-1
- Use linuxthreads libraries even if they're not the default, unless
  explicitly told to use nptl

* Tue Apr 05 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.41-1
- Make sure $LANG is set right for the second stage.
- Fix kickstart traceback trying to skip a nonexistant step.
- Import encodings.idna (sopwith, #153754).
- Fix image building problems.
- Fix kickstart traceback when using shortened forms of language names
  (#153656).

* Mon Apr 04 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.40-1
- Add locale information for 'C' to fix RPM building.

* Sat Apr  2 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.39-1
- fix makefile deps to fix build

* Fri Apr 01 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.38-1
- Set default language for /etc/sysconfig/i18n (#149688).
- Make sure hostname option isn't greyed out if using static IP (#149116).
- Remove unused packages, python library bits, and locale info (katzj).
- Add missing Indic font packages (katzj).
- Various language fixups.

* Wed Mar 30 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.37-1
- try not using maxcpus=1 for arches which still had it
- don't use the reserved variable name str (sopwith)
- various language fixups (clumens)

* Tue Mar 29 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.36-1
- tree build fix

* Tue Mar 29 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.35-1
- dead files can't really be installed (aka, fix the build)

* Tue Mar 29 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.34-1
- Adjust pcmcia module loading for new in-kernel ds (pjones, #151235)
- Make the rescue images identify which arch they're for (pjones, #151501)
- Delete LV snapshots before the parent LV (pjones, #151524)
- Check various forms of a language nick.
- Allow setting MTU on the command line (katzj, #151789)
- Remove dead code in config file handling and sparc booting (katzj)
- Product name and path simplification (katzj)
- Fixes for lang-table format change (katzj, clumens)

* Fri Mar 25 2005 Bill Nottingham <notting@redhat.com> - 10.2.0.33-1
- fix typo in partedUtils.py

* Thu Mar 24 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.32-1
- Switch theme to clearlooks
- Add new Solaris partition id
- Mark some more strings for translation
- Fix xfs fs creation (Lars Hamann, #151378)

* Wed Mar 23 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.31-1
- Add libgcc for images.
- Rewrite language handling.
- Fix readImageFromFile deprecation warning (katzj).
- Don't hide groups which just have metapkgs (katzj, #149182).
- Load SELinux booleans (katzj, #151896).

* Tue Mar 22 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.30-1
- Try harder on the libstdc++ include.
- Fix /etc/resolv.conf fir interactive kickstart installs (#151472).

* Mon Mar 21 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.29-1
- Fix beta nag translation
- Fix button growing (clumens, #151208)
- Add libstdc++ for images (clumens)
- Clean up congrats screen (clumens, #149526)
- Fix CD ejecting in loader (pnasrat, #151232)
- Exclude Xen kernels from everything install (#151490)
- Add reserve_size for ppc to leave room on disc1 (#151234)
- Add some more locales 

* Mon Mar 14 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.28-1
- fix swap detection on upgrade (pjones)
- don't use os.read to make a buffer of '\x00' (pjones)
- move availRaidLevels to raid.py from fsset.py (pjones)
- fix Xvnc parameters (clumens, #150498)
- unmount loopback-mounted ISO images to free loop0 (clumens, #150887)
- fix warnings about gtk.TRUE and gtk.FALSE, partly based on a patch
  from Colin Charles. (pjones)
- sqlite3->sqlite (pnasrat)
- support longer package names in hdlist (pnasrat, #146820)
- Fix handling of --debug (Ingo Pakleppa, #150920, #150925)
- Fix for font location changes (#150889)
- More cjk text shuffling (#149039)

* Mon Mar  7 2005 Peter Jones <pjones@redhat.com> - 10.2.0.27-1
- supress lvm fd warning messages
- fewer log messages when growing partitions
- clamp LVs to pesize during grow

* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.26-1
- urlgrabber stuff is in its own package now

* Sun Mar  6 2005 Peter Jones <pjones@redhat.com> - 10.2.0.25-1
- Empty blacklist in upgrade.py (notting, #142893)
- Add new font package names (katzj)
- Yet another fix of autopart with lvm (pjones)

* Tue Mar  1 2005 Peter Jones <pjones@redhat.com> - 10.2.0.24-1
- gcc4 fixes (clumens, pjones)
- build C files with -D_FORTIFY_SOURCE=2 (pjones)

* Mon Feb 28 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.23-1 
- Don't write out filesystems to fstab we haven't mounted (katzj, #149091).
- Deal with multiple Apple Bootstrap partitions (pnasrat).
- Set hostname sensitivity UI bug.
- Eject CD when failing (pnasrat, #147272).
- Better handling of Apple Bootstrap throughout (pjones).
- Do ethtool setup everywhere (pnasrat, #145522).
- Fix "debug" command line arg (pjones).
- Import new libkrb5support library (#149856).
- Add -once to ensure Xvnc exits (katzj, #137337).

* Sun Feb 20 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.22-1
- revert some of the ppc changes so that lvm is used (nasrat)
- Try to fix bogl stuff some more (#149039)
- x86_64 install fixes (#149040)

* Sun Feb 20 2005 Peter Jones <pjones@redhat.com> - 10.2.0.21-1
- get rid of lilo
- make grub work with raid1 /boot and /root

* Sat Feb 19 2005 Paul Nasrat <pnasrat@redhat.com> - 10.2.0.20-1
- Pull in translations
- s390 linuxrc silence nonexistant group warnings (karsten)
- ppc mac autopartitioning and G5 boot.iso (#121266) and (#149081)

* Sat Feb 12 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.19-1
- fix x86_64 installs for bad urlgrabber import
- Fix traceback with no %post (clumens)
- Put hostname in the text entry (clumens, #132826)

* Tue Feb  8 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.18-1
- Remove some old cruft
- Fix-up for new module naming in gnome-python2-canvas 2.9.x 
- Add needed requirements for rpm 4.4
- Fix segfault when rpm tries to write to non-existent fd during 
  transaction ordering
- Support --erroronfail as an option for %pre/%post (clumens, #124386)

* Tue Feb  8 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.17-1
- Use rhpl.archscore to fix iseries upgrades (pnasrat, #146915)
- Only configure ksdevice if no --device (pnasrat, #138852)
- Don't redraw help if disasbled on next button click (clumens, #145691)
- Fix exception in exception handler (msw)
- Rebuild for new librpm

* Fri Feb  4 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.16-1
- Support setting fs options in kickstart via --fsoptions  (#97560)
- Fix tracebacks

* Wed Feb  2 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.15-1
- Fix some bugs in the reduce-font changes
- Fix urlgrabber import
- Remove langsupport screen, base additional language support off of groups 
  selected

* Wed Feb  2 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.14-1
- Fix deprecation warnings for pygtk 2.5 (clumens)
- Fix bootloader --location=none (clumens, #146448)
- Use urlgrabber (clumens)
- Create reduced bogl font at upd-instroot time to include more 
  characters (#92146, #140208)
- Allow passing --src-discs=0 to get no srpm discs from splittree 
  (based on patch from Armijn Hemel, #119070)
- Mount pseudo-fs's with a more descriptive device name (#136820)
- Minor tweaks to completion message (#138688)

* Tue Jan 25 2005 Peter Jones <pjones@redhat.com> - 10.2.0.13-1
- Hopefully fix LVM size bug (#145183)
- Support multiple iso sets in the same directory (#146053)

* Wed Jan 19 2005 Chris Lumens <clumens@redhat.com> - 10.2.0.12-1 
- Fix partitioning bugs (#101432, #137119)
- Support --bytes-per-inode on a per-partition basis (#57550)

* Thu Jan 13 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.11-1
- Fix some tracebacks with the new glade code
- Use busybox ash instead of ash for netstg2.img/hdstg2.img
- Initialize terminals to avoid color palette change from 
  bterm (pjones, #137849)

* Thu Jan 13 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.10-1
- Handle /sbin/lvm not existing anymore
- Allow installclasses to turn off showing the upgrade option
- Ensure that Core exists in your comps file (#143930)
- Don't fall back to text mode if we fail to start graphics in test mode
- Display better error messages for HTTP/FTP errors (clumens, #144546)
- Switch main UI to use glade, set up infrastructure for use of glade
- Remove some old code
- Add buildprereq for intltool (fixed for b.g.o 163981)

* Wed Jan  5 2005 Jeremy Katz <katzj@redhat.com> - 10.2.0.9-1
- Fix some typos (#143257, #144006)
- Fix from Matthew Miller for multiple dns servers (#84409)
- Fix formatting of fcp disks (#144199)
- Include a README for x86_64 images (clumens, #143366)
- Make an x86_64 rescue image (clumens, #143366)
- Add libXfixes for new gtk2

* Thu Dec 23 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.8-1
- Use tmpfs not ramfs for /dev
- Blacklist "root" as a VG name (#142785)
- Better error message if swap can't be mounted (clumens, #143000)
- Some fixes to the new /dev handling in init
- Make more certain hwaddr gets written out (#143535)
- Handle new swap label format (#143447)
- Let the user know they're in rescue mode earlier (clumens, #136171)

* Mon Dec 20 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.7-1
- Better error handling on device creation (#142273)
- Reset package selection to defaults if selected (#142415)
- LVM on RAID1 fix (nasrat, #141781)
- Add support for biosdev in driverdisk from Rez Kabir (#142738)
- Some more SX8 fixes
- Create /dev as a tmpfs (#141570)
- Remove some old code
- Improve quoting of fstype in anaconda-ks.cfg (Danen Brücker)

* Wed Dec  8 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.6-1
- Write out wepkey better (#140645)
- Try to skip source isos with nfsiso (#106017)
- Don't traceback for bad/missing / in fstab (nasrat, #141174)
- Include pesize in generated ks.cfg (#141370)
- Loop less on shutdown
- Better handling of partial volume groups (#139058)

* Tue Nov 30 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.5-1
- CTCPROT fix (karsten, #133088)
- Fix LVM partitions becoming negative sized (nasrat, #141268)
- Fix removal/editing of zfcp devices in gui (#140559)
- Fix segfault (#140541, #140876)
- Fix handling of pre-existing parts on disks that we then ignore (#131333)

* Tue Nov 23 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.4-1
- Update python version in urllib hack
- /init in initramfs instead of /linuxrc
- Improved ppc console detection (nasrat, #134397)
- Better handling of going back when out of space (#133773)
- Better handling of LVM failures (#134263)
- Set a default when boot loader to upgrade is indeterminate (#139603)
- No more diet on i386

* Tue Nov 16 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.3-1
- Create initramfs images instead of initrds for boot media
- Remove some old code in a few places
- Allow passing --notksdevice in network lines of a ks.cfg to avoid 
  confusion with multiple network lines and a ksdevice= (#136903)
- Allow going back to change the network device if ksdevice= is 
  passed and isn't correct (#136903)
- Fix for console= to automatically imply serial as needed (#137971)

* Mon Nov 15 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.2-1
- Do some more unmounts if we run out of space (#133773)
- Fix for obsoletes E being long (nasrat, #138485)
- Make serial imply nofb (#134167)
- Set fstype to vfat if user selected /boot/efi in the 
  mountpoint dropdown (#138580)
- Copy the X log to the installed system
- Add fix from HJ Lu to fix hang with no bootloader install (#138932)
- Fix splittree error msg (nasrat, #139391)
- Ignore IBM *STMF disks (#137920)

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.1-1
- whrandom is deprecated in python 2.4, use random instead
- fix some syntax errors
- fallback to English for languages that can't do text-mode (#138308)
- More CTCPROT/PORTNAME tweaks (karsten)

* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 10.2.0.0-1
- Switch to python 2.4
- Clean up warning on network screen from pygtk
- Parse pxelinux IPAPPEND for loader network info, patch 
  from Bastien Nocera (#134054)
- Clean up handling of binaries busybox should override
- Do misc package selection earlier so we know all the CDs needed 
  when confirming the install (#122017)
- Mark some strings for translation (#137197)
- Don't reference boot disks in boot loader screen (#135851)
- Add hardware address information to network screen (#131814)
- Fix exception handling in label reading

* Thu Nov  4 2004 Jeremy Katz <katzj@redhat.com> - 10.1.1.4-1
- Fix traceback with CJK upgrades (#137345)
- Allow 128 bit WEP keys (#137447)
- Fix race condition with X client startup (krh, #108777)
- Fix segfault in hd kickstart install (twaugh, #137533)
- Better handling of errors reading labels (#137846)
- Try harder to find LCS interface names (karsten)
- Improve CTCPROT handling (karsten)
- Fix traceback going back in rescue mode network config (#137844)
- Don't use busybox shutdown, poweroff, reboot (#137948)
- Set permissions on anaconda logs
- Make autopartioning better with native storage on legacy iSeries
- Sync onboot behavior of gui/text network screens (#138011)
- Load some drivers later to try to avoid having FC disks be sda
- Sizes in ks.cfg need to be an integer (#138109)

* Tue Oct 26 2004 Jeremy Katz <katzj@redhat.com> - 10.1.1.3-1
- Pull in firefox on upgrade if mozilla/netscape were installed (#137244)
- Fix s390 tracebacks (#130123, #137239)

* Tue Oct 26 2004 Jeremy Katz <katzj@redhat.com> - 10.1.1.2-1
- Handle our LVM autopart lines slightly better (#137120)
- Use busybox sleep for s390 since sleep requires librt again (#131167)
- Handle onboot in ks.cfg properly in the loader (#136903)
- Punjabi shouldn't try to do text mode (#137030)
- Add sgiioc4 driver for Altix CD installs (#136730)
- pci.ids trimming (notting)

* Wed Oct 20 2004 Jeremy Katz <katzj@redhat.com> - 10.1.1.1-1
- Create a netboot.img again for ppc64 (#125129)

* Wed Oct 20 2004 Jeremy Katz <katzj@redhat.com> - 10.1.1.0-1
- Lowercase OSA addresses from the parm file too (karsten)

* Tue Oct 19 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.21-1
- Lowercase OSA addresses to make the kernel happy (#133190)
- Don't hard code the VG name used for auto-partitioning to avoid 
  colliding with existing ones
- Make sure that we don't do runlevel 5 if people don't have X, etc 
  installed (#135895)
- Update for new Indic font filenames

* Mon Oct 18 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.20-1
- Fix traceback with %post logging (Gijs Hollestelle, #136154)
- When using a local stage2.img for FTP/HTTP install, give an error earlier 
  if you point at an invalid tree (#135603, #117155, #120101)
- Add a trailing newline to /etc/sysconfig/kernel
- Try to fix the icon theme
- Rebuild against new dietlibc, hopefully fixes CJK text installs

* Sun Oct 17 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.19-1
- Fix font size to fit on disk display better (#135731)
- Write out part lines for autopart lvm correctly (#135714)
- Remove empty row in drive order for boot loader (#135944)
- Replace % in URLs to avoid format string weirdness (#135929)
- Bind mount /dev for rescue mode (#135860)
- Fix Dutch and Danish keyboard defaults (#135839)
- add s2io 10GbE driver

* Thu Oct 14 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.18-1
- Add fonts for ta, gu, bn, hi, pa (#119283)
- Re-enable bterm for testing (#113910)
- Fix segfault when using biospart with a ks hdinstall.  Patch from 
  Rez Kabir (#135609)
- Write out /etc/sysconfig/kernel for use with new-kernel-pkg changes (#135161)
- Fix telnet logins for s390 (karsten)
- Hardcode LCS as eth instead of tr (karsten)

* Tue Oct 12 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.17-1
- Only use "our" LVM partitions with auto-partitioning (#135440)
- Remove localboot option from syslinux.cfg for diskboot.img (#135263)
- Handle the great input method switch on upgrade (#129218)
- Don't save the hwaddr for qeth (#135023)
- Add rhgb boot loader arguments in postinstall (msw)
- Reverse Norwegian blacklisting (#129453) (notting)
- Add sata_nv, sata_sx4, ixgb, ahci, sx8 modules to the initrd (notting)

* Thu Oct  7 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.16-1
- s390/s390x: Fix traceback with unpartitioned disks (karsten)
- improve fit of bengali network screen (#134762)
- don't allow formatting of a pre-existing partition without also 
  mounting it (#134865)
- Don't show "0" as a mountpoint for an LV that's not being mounted (#134867)
- Add prelink config bits (#117867)
- Sort packages in text package group details (#123437)
- Don't traceback on upgrade if /dev/mapper/control exists (#124092)

* Tue Oct  5 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.15-1
- Fix creation of scsi device nodes (#134709)
- Fix multiple kickstart scriptlets with different interpreters (#134707)

* Mon Oct  4 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.14-1
- Some zfcp fixes
- Don't traceback if we have a %%include inside a scriptlet (#120252)
- Fix SELinux for text-mode ftp/http installs (#134549)

* Mon Oct  4 2004 Mike McLean <mikem@redhat.com> - 10.0.3.12-1
- add command line options to pkgorder (mikem)

* Mon Oct  4 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.11-1
- Handle 32 raid devs (#134438)
- Fix LCS PORTNAME (#134487)
- Add logging of kickstart scripts with --log to %post/%pre
- Copy /tmp/anaconda.log and /tmp/syslog to /var/log/anaconda.log 
  and /var/log/anaconda.syslog respectively (#124370)
- Fix Polish (#134554)
- Add arch-specific package removal (#133396)
- Include PPC PReP Boot partition in anaconda-ks.cfg (#133934)
- Fix changing of VG name going through to boot loader setup (#132213)
- Add support for > 128 SCSI disks (#134575)

* Fri Oct  1 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.10-1
- add kickstart zfcp configuration (#133288, #130070)
- Use NFSv3 for NFS installs.  Fixes NFSISO installs from DVD (#122032)
- Fix megaraid_mbox module name (#134369)
- Another uninitialized fix (#133996)
- Add the zh_CN font (#133330)

* Thu Sep 30 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.9-1
- translation updates
- Install compat-arch-support by default (#133514)
- Warn if an older version is chosen for upgrading if product is RHEL (#134523)
- Fix traceback on upgrade with possible lvm1 (#134258)
- Make changing the DNS server work (#122554)
- More fixes from pnasrat for arch handling on upgrade

* Thu Sep 30 2004 Paul Nasrat <pnasrat@redhat.com> - 10.0.3.8-1
- Fix missing rpm.ts (#133045)

* Wed Sep 29 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.7-1
- Don't ask about mouse type on remote X display (#133902)
- Label swap filesystems (#127892)
- Fix possible crash on hd kickstart installs (#133996)
- Improve multiarch upgrade (#133045)
- Avoid changing the default language when selecting additional 
  language support (#134040)
- Remove spurious blank option in upgrade combo (#134058)
- Fix driver disk hang (#131112, #122952)
- Fix detection of unformatted dasd (#130123)

* Mon Sep 27 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.6-1
- Fix traceback from auto-partitioning if you don't have enough space (#131325)
- Update FCP config for adding SCSI LUNs (#133290)

* Mon Sep 27 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.5-1
- Fix driver disk segfault when using a partition (#133036)
- Let driver disk images on ext2 partitions work
- Fix nonet/nostorage
- Allow name.arch syntax in ks.cfg (#124456)
- Fix traceback unselecting last language (#133164)
- Skip version 0 swap (#122101)
- Handle /dev being present in device names of ks.cfg (#121486)
- Use no instead of no-latin1 for Norwegian keyboard (#133757)
- include other dm modules (#132001)

* Fri Sep 24 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.4-1
- fix megaraid module name (notting)
- don't prompt for a driver disk on pSeries boxes with just 
  virtual devices (#135292)
- don't use PROBE_LOADED for cd probe (#131033)
- i2o devices don't use a "p" separator (#133379)
- switch back zh_CN font to default (#133330)
- add 3w-9xxx to modules.cgz (#133525)
- fix showing of freespace (#133425)

* Wed Sep 22 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.3-1
- fix going back unmount of /dev/pts (#133301)
- fix SRPMs disc (#122737)
- add localboot option to isolinux.cfg (#120687)
- fix tree build on ia64 and x86_64
- fix a syntax error for text mode selinux config 

* Tue Sep 21 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.2-1
- some fixes for Arabic (#122228)
- support using ksdevice=macaddr (#130605)
- add an images/pxeboot directory on ia64

* Tue Sep 21 2004 Jeremy Katz <katzj@redhat.com> - 10.0.3.1-1
- improve handling of non-physical consoles on some ppc and ia64 machines
- add Bengali(India) and Gujarati to the lang-table (#126108)
- add support for setting the CTC protocol on s/390 (#132324, #132325)
- don't offer to do vnc if we don't have active nwtorking (#132833)
- various typo/grammar fixes
- add support for 'nostorage' and 'nonet' command line options to avoid 
  auto-loading just network or storage devices
- fix editing of pre-existing lvm (#132217)
- fix going back from the partitions list on a driver disk (#132096)
- don't show login error if silent errors (#132673)

* Thu Jun  3 2004 Jeremy Katz <katzj@redhat.com>
- require system-logos and anaconda-help, obsolete anaconda-images

* Fri Apr 30 2004 Jeremy Katz <katzj@redhat.com>
- Update description, remove prereq on stuff that was only needed 
  for reconfig mode 

* Tue Feb 24 2004 Jeremy Katz <katzj@redhat.com>
- buildrequire libselinux-devel

* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com>
- require booty (#109272)

* Tue Oct  8 2002 Jeremy Katz <katzj@redhat.com>
- back to mainstream rpm instead of rpm404

* Mon Sep  9 2002 Jeremy Katz <katzj@redhat.com>
- can't buildrequire dietlibc and kernel-pcmcia-cs since they don't always
  exist

* Wed Aug 21 2002 Jeremy Katz <katzj@redhat.com>
- added URL

* Thu May 23 2002 Jeremy Katz <katzj@redhat.com>
- add require and buildrequire on rhpl

* Tue Apr 02 2002 Michael Fulbright <msf@redhat.com>
- added some more docs

* Fri Feb 22 2002 Jeremy Katz <katzj@redhat.com>
- buildrequire kernel-pcmcia-cs as we've sucked the libs the loader needs 
  to there now

* Thu Feb 07 2002 Michael Fulbright <msf@redhat.com>
- goodbye reconfig

* Thu Jan 31 2002 Jeremy Katz <katzj@redhat.com>
- update the BuildRequires a bit

* Fri Jan  4 2002 Jeremy Katz <katzj@redhat.com>
- ddcprobe is now done from kudzu

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

