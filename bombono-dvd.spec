%global  boost_flags \\\
    -DBOOST_SYSTEM_NO_DEPRECATED -DBOOST_FILESYSTEM_VERSION=3
%global warn_flags  \
    -Wno-reorder -Wno-unused-variable
%global  scons       \
    scons  %{?jobs:-j%{jobs}}                              \\\
    BUILD_CFG=debug                                        \\\
    BUILD_BRIEF=false                                      \\\
    BUILD_QUICK=false                                      \\\
    CC="%__cc"                                             \\\
    CXX="%__cxx"                                           \\\
    CFLAGS=""                                              \\\
    CPPFLAGS="%{optflags} %{warn_flags} %{boost_flags}"    \\\
    PREFIX=%{_prefix}                                      \\\
    TEST=false                                             \\\
    TEST_BUILD=false                                       \\\
    USE_EXT_BOOST=true                                     


Name:		bombono-dvd
Version:	1.2.2
Release:	1
Summary:	DVD authoring program with nice and clean GUI
License:	GPLv2
Group:		Video
URL:		http://www.bombono.org
Source0:	http://sourceforge.net/projects/bombono/files/bombono-dvd/1.2/%{name}-%{version}.tar.bz2
Patch0:         filesys-include-path.patch
Patch1:         0001-ffmpeg-has-renamed-CodecID-AVCodecID.patch

BuildRequires:  gettext
BuildRequires:  stdc++-devel
BuildRequires:  desktop-file-utils
BuildRequires:	scons 
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(gdkmm-2.4)
BuildRequires:  boost-devel
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(mjpegtools) 
BuildRequires:	ffmpeg-devel
Requires:	dvdauthor 
Requires:       mjpegtools 
Requires:       dvd+rw-tools 
Requires:       twolame 
Requires:       enca
Requires:       dvdauthor

%description
 Bombono DVD is easy to use program for making DVD-Video.
 The main features of Bombono DVD are:
  * excellent MPEG viewer: Timeline and Monitor
  * real WYSIWYG Menu Editor with live thumbnails
  * comfortable Drag-N-Drop support
  * you can author to folder, make ISO-image or burn directly to DVD
  * reauthoring: you can import video from DVD discs.

%prep
%setup -q	
%patch0 -p1
%patch1 -p1
sed -i '\;#![ ]*/usr/bin/env;d'  $(find . -name SCons\*)
rm -r debian libs/boost-lib src/mlib/tests libs/mpeg2dec ./libs/asl/adobe

%build
scons  build

%install
rm config.opts
scons DESTDIR=%{buildroot} install

%find_lang %name

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/bombono-dvd.desktop

%files -f %{name}.lang
%doc README COPYING docs
%{_bindir}/*
%{_datadir}/bombono
%{_datadir}/applications/bombono-dvd.desktop
%{_datadir}/pixmaps/bombono-dvd.png
%{_datadir}/icons/hicolor/*/apps/bombono-dvd.png
%{_datadir}/mime/packages/bombono.xml
%{_mandir}/man1/*
