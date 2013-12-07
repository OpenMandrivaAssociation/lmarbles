Summary:	Summary Atomix-style arcade game
Name:		lmarbles
Epoch:		1
Version:	1.0.8
Release:	9
License:	GPLv2+
Group:		Games/Puzzles
Url:		http://lgames.sourceforge.net/index.php?project=LMarbles
Source0:	http://lgames.sourceforge.net/marbleslgames/%{name}-%{version}.tar.gz
Buildrequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
Provides:	marbles

%description
LMarbles is very similar to Atomix and was heavily inspired by it. Goal is to
create a more or less complex figure out of single marbles within a time limit
to reach the next level. Sounds easy? Well, there is a problem:	If a marble
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
desktop-file-install \
	--add-category=LogicGame \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README
%attr(2755,root,games) %{_gamesbindir}/*
%attr(0664,games,games) %{_localstatedir}/lib/games/%{name}.prfs
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_mandir}/man6/*

