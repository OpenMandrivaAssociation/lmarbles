%define Summary Atomix-style arcade game

Summary:	%{Summary}
Name:		lmarbles
Version:	1.0.8
Release:	%mkrel 6
Epoch:		1
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://lgames.sourceforge.net/index.php?project=LMarbles
Source0:	http://lgames.sourceforge.net/marbleslgames/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	imagemagick
Buildrequires:	desktop-file-utils
Provides:	marbles
Obsoletes:	marbles
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
LMarbles is very similar to Atomix and was heavily inspired by it. Goal is to
create a more or less complex figure out of single marbles within a time limit
to reach the next level. Sounds easy? Well, there is a problem: If a marble
starts to move it will not stop until it hits a wall or marble. And to make it
even more interesting there are obstacles like arrows, crumbling walls and
teleports!

%prep
%setup -q

%build
%configure2_5x \
    --localstatedir=%{_localstatedir}/lib/games \
    --datadir=%{_gamesdatadir} \
    --bindir=%{_gamesbindir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Correct icon and .desktop paths
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/48x48/apps}
mv %{buildroot}%{_gamesdatadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_gamesdatadir}/icons/%{name}48.gif %{buildroot}%{_iconsdir}/hicolor/48x48/apps

# convert icon
convert %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}48.gif  %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
rm -f %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}48.gif

# fix desktop file
sed -i -e "s/\/usr\/share\/games\/icons\/%{name}48.gif/%{name}/g" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --add-category=LogicGame \
		     --dir %{buildroot}%{_datadir}/applications/ \
		     %{buildroot}%{_datadir}/applications/%{name}.desktop

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%update_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(2755,root,games) %{_gamesbindir}/*
%attr(0664,games,games) %{_localstatedir}/lib/games/%{name}.prfs
%{_gamesdatadir}/%{name}
%{_mandir}/man6/*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1:1.0.8-3mdv2011.0
+ Revision: 672774
- fix br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.8-2mdv2011.0
+ Revision: 606415
- rebuild

* Fri Nov 13 2009 Jérôme Brenier <incubusss@mandriva.org> 1:1.0.8-1mdv2010.1
+ Revision: 465866
- BR desktop-file-utils
- update to new version 1.0.8
- fix license tag
- use desktop file and icon provided with the source package
- BR imagemagick (icon conversion from gif to png)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.0.7-9mdv2010.0
+ Revision: 425995
- rebuild

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 1:1.0.7-9mdv2009.1
+ Revision: 364391
- new rpm group

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 1:1.0.7-8mdv2009.1
+ Revision: 364302
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:1.0.7-7mdv2009.0
+ Revision: 223119
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1:1.0.7-6mdv2008.1
+ Revision: 152860
- rebuild
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Mar 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-4mdv2007.1
+ Revision: 146621
- fix summary

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.7-3mdv2007.1
+ Revision: 146108
- Import lmarbles

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdv2007.1
- use the %%mrel macro
- fix the xdg menu stuff

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0.7-2mdk
- Rebuild

* Thu Jan 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.0.7-1mdk
- New version.
- Renamed to lmarbles.

* Tue Aug 17 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.0.5-4mdk
- Fix menu again

* Sat Aug 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.0.5-3mdk
- rebuild.
- change menu section.

