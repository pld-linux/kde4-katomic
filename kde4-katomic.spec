%define		_state		stable
%define		orgname		katomic
%define		qtver		4.8.0

Summary:	KDE Sokoban clone
Summary(pl.UTF-8):	Klon gry Sokoban dla KDE
Summary(pt_BR.UTF-8):	Jogo semelhante ao Sokoban mas o objetivo é formar moléculas
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	930e9fd1f267dce503c053991248ec50
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description -l pl.UTF-8
Atomic to mała gra podobna do gry Sokoban. Celem gry jest zbudowanie
cząsteczek chemicznych na planszy podobnej do tej z gry Sokoban.

%description -l pt_BR.UTF-8
Jogo semelhante ao Sokoban mas o objetivo é formar moléculas.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_desktopdir}/kde4/katomic.desktop
%{_datadir}/apps/katomic
%{_datadir}/config/katomic.knsrc
%{_datadir}/apps/kconf_update/katomic-levelset-upd.pl
%{_datadir}/apps/kconf_update/katomic-levelset.upd
%{_iconsdir}/*/*/apps/katomic.png
