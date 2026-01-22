Name:           imv
Version:        4.5.0
Release:        6
Summary:        Image viewer for X11 and Wayland
License:        GPL-2.0-or-later
Group:          Graphics/Viewers
URL:            https://git.sr.ht/~exec64/imv
Source0:        https://git.sr.ht/~exec64/imv/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0:		imv-4.5.0-icu76.patch

BuildRequires:  a2x
BuildRequires:  asciidoc
BuildRequires:  freeimage-devel
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(inih)
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(fontconfig)
# Package is in restricted repository
#BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xcb)

# libnsgif is optional and provides animated GIF support. Disable it for now. Package not yet in cooker.

%description
imv is a command line image viewer intended for use with tiling window managers.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson   \
          -Dlibnsgif=disabled \
          -Dlibheif=disabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_mandir}/man*/%{name}*
%{_sysconfdir}/%{name}_config
