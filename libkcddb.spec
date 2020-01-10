Name:    libkcddb
Version: 4.10.5
Release: 1%{?dist}
Summary: CDDB retrieval library

License: LGPLv2+ and GPLv2+
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# query/use pkg-config libmusicbrainz5 info
Patch50: libkcddb-4.9.98-libmusicbrainz5_cflags.patch

BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: pkgconfig(libmusicbrainz5)

Requires: kdelibs4%{?_isa} >= %{_kde4_version}
# kcmshell4
Requires: kde-runtime%{?_isa} >= %{_kde4_version}

# when split occured
Conflicts: kdemultimedia-libs < 6:4.8.80

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel
# when split occured
Conflicts: kdemultimedia-devel < 6:4.8.80
%description devel
%{summary}.


%prep
%setup -q

%patch50 -p1 -b .libmusicbrainz5_cflags


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# fix documentation multilib conflict in index.cache
bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/cddbretrieval/index.cache.bz2
sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/cddbretrieval/index.cache
sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/cddbretrieval/index.cache
bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/cddbretrieval/index.cache

%find_lang %{name} --with-kde --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc TODO
%{_kde4_datadir}/config.kcfg/libkcddb.kcfg
%{_kde4_datadir}/kde4/services/libkcddb.desktop
%{_kde4_libdir}/libkcddb.so.4*
%{_kde4_libdir}/kde4/kcm_cddb.so

%files devel
%{_kde4_includedir}/libkcddb/
%{_kde4_libdir}/libkcddb.so
%{_kde4_libdir}/cmake/libkcddb/


%changelog
* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Thu Apr 25 2013 Than Ngo <than@redhat.com> - 4.10.2-2
- fix multilib issue

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sat Jan 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95
- BR: pkgconfig(libmusicbrainz5)

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Fri Jun 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-1
- 4.8.90

* Thu May 31 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-1
- initial try
