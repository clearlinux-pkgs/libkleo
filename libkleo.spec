#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkleo
Version  : 21.08.2
Release  : 34
URL      : https://download.kde.org/stable/release-service/21.08.2/src/libkleo-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/libkleo-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/libkleo-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: libkleo-data = %{version}-%{release}
Requires: libkleo-lib = %{version}-%{release}
Requires: libkleo-license = %{version}-%{release}
Requires: libkleo-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : gpgme-dev gpgme-extras
BuildRequires : gpgme-extras
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kitemmodels-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
# Fixture for KeyResolverTest
## Setup
Set the `GNUPGHOME` environment variable to this folder:
```
export GNUPGHOME=$(pwd)
```

%package data
Summary: data components for the libkleo package.
Group: Data

%description data
data components for the libkleo package.


%package dev
Summary: dev components for the libkleo package.
Group: Development
Requires: libkleo-lib = %{version}-%{release}
Requires: libkleo-data = %{version}-%{release}
Provides: libkleo-devel = %{version}-%{release}
Requires: libkleo = %{version}-%{release}

%description dev
dev components for the libkleo package.


%package lib
Summary: lib components for the libkleo package.
Group: Libraries
Requires: libkleo-data = %{version}-%{release}
Requires: libkleo-license = %{version}-%{release}

%description lib
lib components for the libkleo package.


%package license
Summary: license components for the libkleo package.
Group: Default

%description license
license components for the libkleo package.


%package locales
Summary: locales components for the libkleo package.
Group: Default

%description locales
locales components for the libkleo package.


%prep
%setup -q -n libkleo-21.08.2
cd %{_builddir}/libkleo-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634404035
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634404035
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkleo
cp %{_builddir}/libkleo-21.08.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkleo/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/libkleo-21.08.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkleo/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/libkleo-21.08.2/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libkleo/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/libkleo-21.08.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkleo/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/libkleo-21.08.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkleo/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/libkleo-21.08.2/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libkleo/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libkleopatra

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/libkleopatra/pics/chiasmus_chi.png
/usr/share/libkleopatra/pics/hi16-app-gpg.png
/usr/share/libkleopatra/pics/hi16-app-gpgsm.png
/usr/share/libkleopatra/pics/hi22-app-gpg.png
/usr/share/libkleopatra/pics/hi22-app-gpgsm.png
/usr/share/libkleopatra/pics/hi32-app-gpg.png
/usr/share/libkleopatra/pics/hi32-app-gpgsm.png
/usr/share/libkleopatra/pics/key.png
/usr/share/libkleopatra/pics/key_bad.png
/usr/share/libkleopatra/pics/key_ok.png
/usr/share/libkleopatra/pics/key_unknown.png
/usr/share/libkleopatra/pics/smartcard.xpm
/usr/share/qlogging-categories5/libkleo.categories
/usr/share/qlogging-categories5/libkleo.renamecategories
/usr/share/xdg/libkleopatrarc

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Libkleo/Algorithm
/usr/include/KF5/Libkleo/ChecksumDefinition
/usr/include/KF5/Libkleo/Classify
/usr/include/KF5/Libkleo/Compat
/usr/include/KF5/Libkleo/CryptoConfig
/usr/include/KF5/Libkleo/CryptoConfigModule
/usr/include/KF5/Libkleo/DNAttributeOrderConfigWidget
/usr/include/KF5/Libkleo/Debug
/usr/include/KF5/Libkleo/DefaultKeyFilter
/usr/include/KF5/Libkleo/DefaultKeyGenerationJob
/usr/include/KF5/Libkleo/DirectoryServicesWidget
/usr/include/KF5/Libkleo/Dn
/usr/include/KF5/Libkleo/EditDirectoryServiceDialog
/usr/include/KF5/Libkleo/Enum
/usr/include/KF5/Libkleo/FileNameRequester
/usr/include/KF5/Libkleo/FileSystemWatcher
/usr/include/KF5/Libkleo/Formatting
/usr/include/KF5/Libkleo/GnuPG
/usr/include/KF5/Libkleo/KConfigBasedKeyFilter
/usr/include/KF5/Libkleo/KDHorizontalLine
/usr/include/KF5/Libkleo/KeyApprovalDialog
/usr/include/KF5/Libkleo/KeyCache
/usr/include/KF5/Libkleo/KeyFilter
/usr/include/KF5/Libkleo/KeyFilterManager
/usr/include/KF5/Libkleo/KeyGroup
/usr/include/KF5/Libkleo/KeyList
/usr/include/KF5/Libkleo/KeyListModel
/usr/include/KF5/Libkleo/KeyListModelInterface
/usr/include/KF5/Libkleo/KeyListSortFilterProxyModel
/usr/include/KF5/Libkleo/KeyRearrangeColumnsProxyModel
/usr/include/KF5/Libkleo/KeyRequester
/usr/include/KF5/Libkleo/KeyResolver
/usr/include/KF5/Libkleo/KeyResolverCore
/usr/include/KF5/Libkleo/KeySelectionCombo
/usr/include/KF5/Libkleo/KeySelectionDialog
/usr/include/KF5/Libkleo/KeyserverConfig
/usr/include/KF5/Libkleo/KleoException
/usr/include/KF5/Libkleo/MessageBox
/usr/include/KF5/Libkleo/NewKeyApprovalDialog
/usr/include/KF5/Libkleo/OidMap
/usr/include/KF5/Libkleo/Predicates
/usr/include/KF5/Libkleo/ProgressDialog
/usr/include/KF5/Libkleo/Stl_Util
/usr/include/KF5/Libkleo/SubkeyListModel
/usr/include/KF5/Libkleo/Test
/usr/include/KF5/Libkleo/UserIDListModel
/usr/include/KF5/libkleo/algorithm.h
/usr/include/KF5/libkleo/checksumdefinition.h
/usr/include/KF5/libkleo/classify.h
/usr/include/KF5/libkleo/compat.h
/usr/include/KF5/libkleo/cryptoconfig.h
/usr/include/KF5/libkleo/cryptoconfigmodule.h
/usr/include/KF5/libkleo/debug.h
/usr/include/KF5/libkleo/defaultkeyfilter.h
/usr/include/KF5/libkleo/defaultkeygenerationjob.h
/usr/include/KF5/libkleo/directoryserviceswidget.h
/usr/include/KF5/libkleo/dn.h
/usr/include/KF5/libkleo/dnattributeorderconfigwidget.h
/usr/include/KF5/libkleo/editdirectoryservicedialog.h
/usr/include/KF5/libkleo/enum.h
/usr/include/KF5/libkleo/filenamerequester.h
/usr/include/KF5/libkleo/filesystemwatcher.h
/usr/include/KF5/libkleo/formatting.h
/usr/include/KF5/libkleo/gnupg.h
/usr/include/KF5/libkleo/kconfigbasedkeyfilter.h
/usr/include/KF5/libkleo/kdhorizontalline.h
/usr/include/KF5/libkleo/keyapprovaldialog.h
/usr/include/KF5/libkleo/keycache.h
/usr/include/KF5/libkleo/keyfilter.h
/usr/include/KF5/libkleo/keyfiltermanager.h
/usr/include/KF5/libkleo/keygroup.h
/usr/include/KF5/libkleo/keylist.h
/usr/include/KF5/libkleo/keylistmodel.h
/usr/include/KF5/libkleo/keylistmodelinterface.h
/usr/include/KF5/libkleo/keylistsortfilterproxymodel.h
/usr/include/KF5/libkleo/keyrearrangecolumnsproxymodel.h
/usr/include/KF5/libkleo/keyrequester.h
/usr/include/KF5/libkleo/keyresolver.h
/usr/include/KF5/libkleo/keyresolvercore.h
/usr/include/KF5/libkleo/keyselectioncombo.h
/usr/include/KF5/libkleo/keyselectiondialog.h
/usr/include/KF5/libkleo/keyserverconfig.h
/usr/include/KF5/libkleo/kleo_export.h
/usr/include/KF5/libkleo/kleoexception.h
/usr/include/KF5/libkleo/messagebox.h
/usr/include/KF5/libkleo/newkeyapprovaldialog.h
/usr/include/KF5/libkleo/oidmap.h
/usr/include/KF5/libkleo/predicates.h
/usr/include/KF5/libkleo/progressdialog.h
/usr/include/KF5/libkleo/stl_util.h
/usr/include/KF5/libkleo/subkeylistmodel.h
/usr/include/KF5/libkleo/test.h
/usr/include/KF5/libkleo/useridlistmodel.h
/usr/include/KF5/libkleo_version.h
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoConfig.cmake
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoConfigVersion.cmake
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoTargets.cmake
/usr/lib64/libKF5Libkleo.so
/usr/lib64/qt5/mkspecs/modules/qt_Libkleo.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Libkleo.so.5
/usr/lib64/libKF5Libkleo.so.5.18.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkleo/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libkleo/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libkleo/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libkleo/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libkleo/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkleo/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkleopatra.lang
%defattr(-,root,root,-)

