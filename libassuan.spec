#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6
#
Name     : libassuan
Version  : 2.5.3
Release  : 19
URL      : https://gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2
Source1 : https://gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2.sig
Summary  : IPC library for the GnuPG components
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: libassuan-bin = %{version}-%{release}
Requires: libassuan-info = %{version}-%{release}
Requires: libassuan-lib = %{version}-%{release}
Requires: libassuan-license = %{version}-%{release}
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras

%description
Libassuan
===========
This is a general purpose IPC library which is for example used
GnuPG, GPGME and some other software.

%package bin
Summary: bin components for the libassuan package.
Group: Binaries
Requires: libassuan-license = %{version}-%{release}

%description bin
bin components for the libassuan package.


%package dev
Summary: dev components for the libassuan package.
Group: Development
Requires: libassuan-lib = %{version}-%{release}
Requires: libassuan-bin = %{version}-%{release}
Provides: libassuan-devel = %{version}-%{release}
Requires: libassuan = %{version}-%{release}

%description dev
dev components for the libassuan package.


%package info
Summary: info components for the libassuan package.
Group: Default

%description info
info components for the libassuan package.


%package lib
Summary: lib components for the libassuan package.
Group: Libraries
Requires: libassuan-license = %{version}-%{release}

%description lib
lib components for the libassuan package.


%package license
Summary: license components for the libassuan package.
Group: Default

%description license
license components for the libassuan package.


%prep
%setup -q -n libassuan-2.5.3
cd %{_builddir}/libassuan-2.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573789393
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573789393
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libassuan
cp %{_builddir}/libassuan-2.5.3/COPYING %{buildroot}/usr/share/package-licenses/libassuan/842745cb706f8f2126506f544492f7a80dbe29b3
cp %{_builddir}/libassuan-2.5.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/libassuan/9a1929f4700d2407c70b507b3b2aaf6226a9543c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libassuan-config

%files dev
%defattr(-,root,root,-)
/usr/include/assuan.h
/usr/lib64/libassuan.so
/usr/lib64/pkgconfig/libassuan.pc
/usr/share/aclocal/*.m4

%files info
%defattr(0644,root,root,0755)
/usr/share/info/assuan.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libassuan.so.0
/usr/lib64/libassuan.so.0.8.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libassuan/842745cb706f8f2126506f544492f7a80dbe29b3
/usr/share/package-licenses/libassuan/9a1929f4700d2407c70b507b3b2aaf6226a9543c
