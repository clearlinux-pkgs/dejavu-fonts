Name     : dejavu-fonts
Version  : 2.37
Release  : 3
URL      : http://sourceforge.net/projects/dejavu/files/dejavu/2.37/dejavu-fonts-ttf-2.37.tar.bz2
Source0  : http://sourceforge.net/projects/dejavu/files/dejavu/2.37/dejavu-fonts-ttf-2.37.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.0

%description
dejavu fonts

%prep
%setup -n dejavu-fonts-ttf-2.37

%install
install -D -m 0644 ttf/DejaVuMathTeXGyre.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuMathTeXGyre.ttf
install -D -m 0644 ttf/DejaVuSans-BoldOblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSans-BoldOblique.ttf
install -D -m 0644 ttf/DejaVuSans-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSans-Bold.ttf
install -D -m 0644 ttf/DejaVuSansCondensed-BoldOblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansCondensed-BoldOblique.ttf
install -D -m 0644 ttf/DejaVuSansCondensed-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansCondensed-Bold.ttf
install -D -m 0644 ttf/DejaVuSansCondensed-Oblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansCondensed-Oblique.ttf
install -D -m 0644 ttf/DejaVuSansCondensed.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansCondensed.ttf
install -D -m 0644 ttf/DejaVuSans-ExtraLight.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSans-ExtraLight.ttf
install -D -m 0644 ttf/DejaVuSansMono-BoldOblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansMono-BoldOblique.ttf
install -D -m 0644 ttf/DejaVuSansMono-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansMono-Bold.ttf
install -D -m 0644 ttf/DejaVuSansMono-Oblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansMono-Oblique.ttf
install -D -m 0644 ttf/DejaVuSansMono.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSansMono.ttf
install -D -m 0644 ttf/DejaVuSans-Oblique.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSans-Oblique.ttf
install -D -m 0644 ttf/DejaVuSans.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSans.ttf
install -D -m 0644 ttf/DejaVuSerif-BoldItalic.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerif-BoldItalic.ttf
install -D -m 0644 ttf/DejaVuSerif-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerif-Bold.ttf
install -D -m 0644 ttf/DejaVuSerifCondensed-BoldItalic.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-BoldItalic.ttf
install -D -m 0644 ttf/DejaVuSerifCondensed-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-Bold.ttf
install -D -m 0644 ttf/DejaVuSerifCondensed-Italic.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-Italic.ttf
install -D -m 0644 ttf/DejaVuSerifCondensed.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerifCondensed.ttf
install -D -m 0644 ttf/DejaVuSerif-Italic.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerif-Italic.ttf
install -D -m 0644 ttf/DejaVuSerif.ttf %{buildroot}/usr/share/fonts/X11/TTF/DejaVuSerif.ttf
install -D -m 0644 LICENSE %{buildroot}/usr/share/package-licenses/dejavu-fonts/LICENSE

%files
%defattr(-,root,root,-)
/usr/share/fonts/X11/TTF/DejaVuMathTeXGyre.ttf
/usr/share/fonts/X11/TTF/DejaVuSans-BoldOblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSans-Bold.ttf
/usr/share/fonts/X11/TTF/DejaVuSansCondensed-BoldOblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSansCondensed-Bold.ttf
/usr/share/fonts/X11/TTF/DejaVuSansCondensed-Oblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSansCondensed.ttf
/usr/share/fonts/X11/TTF/DejaVuSans-ExtraLight.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMono-BoldOblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMono-Bold.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMono-Oblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMono.ttf
/usr/share/fonts/X11/TTF/DejaVuSans-Oblique.ttf
/usr/share/fonts/X11/TTF/DejaVuSans.ttf
/usr/share/fonts/X11/TTF/DejaVuSerif-BoldItalic.ttf
/usr/share/fonts/X11/TTF/DejaVuSerif-Bold.ttf
/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-BoldItalic.ttf
/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-Bold.ttf
/usr/share/fonts/X11/TTF/DejaVuSerifCondensed-Italic.ttf
/usr/share/fonts/X11/TTF/DejaVuSerifCondensed.ttf
/usr/share/fonts/X11/TTF/DejaVuSerif-Italic.ttf
/usr/share/fonts/X11/TTF/DejaVuSerif.ttf
/usr/share/package-licenses/dejavu-fonts/LICENSE
