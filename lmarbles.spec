%define Summary Atomix-style arcade game

Summary:	%{Summary}
Name:		lmarbles
Version:	1.0.8
Release:	%mkrel 1
Epoch:		1
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://lgames.sourceforge.net/index.php?project=LMarbles
Source0:	http://lgames.sourceforge.net/marbleslgames/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	libSDL_mixer-devel
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
