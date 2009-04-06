%define Summary Atomix-style arcade game

Summary:	%{Summary}
Name:		lmarbles
Version:	1.0.7
Release:	%mkrel 8
Epoch:		1
License:	GPL
Group:		Games/Boards
URL:		http://lgames.sourceforge.net/index.php?project=LMarbles
Source0:	http://lgames.sourceforge.net/marbleslgames/%{name}-%{version}.tar.bz2
Source1:	%{name}16.png
Source2:	%{name}32.png
Source3:	%{name}48.png
BuildRequires:	SDL-devel libSDL_mixer-devel
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

install -D -m644 %SOURCE1 %{buildroot}%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE2 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE3 %{buildroot}%{_liconsdir}/%{name}.png

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Marbles
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
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
%{_iconsdir}/*
%{_miconsdir}/*
%{_liconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
