#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libassuan
Version  : 2.4.2
Release  : 5
URL      : ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.4.2.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.4.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: libassuan-bin
Requires: libassuan-lib
Requires: libassuan-doc
BuildRequires : libgpg-error-dev

%description
Libassuan
===========
This is a general purpose IPC library which is for example used
GnuPG, GPGME and some other software.

%package bin
Summary: bin components for the libassuan package.
Group: Binaries

%description bin
bin components for the libassuan package.


%package dev
Summary: dev components for the libassuan package.
Group: Development
Requires: libassuan-lib
Requires: libassuan-bin
Provides: libassuan-devel

%description dev
dev components for the libassuan package.


%package doc
Summary: doc components for the libassuan package.
Group: Documentation

%description doc
doc components for the libassuan package.


%package lib
Summary: lib components for the libassuan package.
Group: Libraries

%description lib
lib components for the libassuan package.


%prep
%setup -q -n libassuan-2.4.2

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libassuan-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
