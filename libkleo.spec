#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkleo
Version  : 23.08.3
Release  : 66
URL      : https://download.kde.org/stable/release-service/23.08.3/src/libkleo-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/libkleo-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/libkleo-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0
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
BuildRequires : kpimtextedit-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n libkleo-23.08.3
cd %{_builddir}/libkleo-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702018005
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702018005
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkleo
cp %{_builddir}/libkleo-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkleo/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/libkleo-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkleo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkleo-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkleo/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkleo-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libkleo/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/libkleo-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkleo/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libkleo-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkleo/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/libkleo-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkleo/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libkleo-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libkleo/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libkleopatra
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/KPim5/Libkleo/Libkleo/Algorithm
/usr/include/KPim5/Libkleo/Libkleo/Assuan
/usr/include/KPim5/Libkleo/Libkleo/AuditLogEntry
/usr/include/KPim5/Libkleo/Libkleo/AuditLogViewer
/usr/include/KPim5/Libkleo/Libkleo/ChecksumDefinition
/usr/include/KPim5/Libkleo/Libkleo/Chrono
/usr/include/KPim5/Libkleo/Libkleo/Classify
/usr/include/KPim5/Libkleo/Libkleo/Compat
/usr/include/KPim5/Libkleo/Libkleo/Compliance
/usr/include/KPim5/Libkleo/Libkleo/CryptoConfig
/usr/include/KPim5/Libkleo/Libkleo/CryptoConfigModule
/usr/include/KPim5/Libkleo/Libkleo/DNAttributeOrderConfigWidget
/usr/include/KPim5/Libkleo/Libkleo/Debug
/usr/include/KPim5/Libkleo/Libkleo/DefaultKeyFilter
/usr/include/KPim5/Libkleo/Libkleo/DefaultKeyGenerationJob
/usr/include/KPim5/Libkleo/Libkleo/DirectoryServicesWidget
/usr/include/KPim5/Libkleo/Libkleo/Dn
/usr/include/KPim5/Libkleo/Libkleo/DocAction
/usr/include/KPim5/Libkleo/Libkleo/EditDirectoryServiceDialog
/usr/include/KPim5/Libkleo/Libkleo/Enum
/usr/include/KPim5/Libkleo/Libkleo/ExpiryChecker
/usr/include/KPim5/Libkleo/Libkleo/ExpiryCheckerConfig
/usr/include/KPim5/Libkleo/Libkleo/ExpiryCheckerSettings
/usr/include/KPim5/Libkleo/Libkleo/FileNameRequester
/usr/include/KPim5/Libkleo/Libkleo/FileSystemWatcher
/usr/include/KPim5/Libkleo/Libkleo/Formatting
/usr/include/KPim5/Libkleo/Libkleo/GnuPG
/usr/include/KPim5/Libkleo/Libkleo/Hex
/usr/include/KPim5/Libkleo/Libkleo/KConfigBasedKeyFilter
/usr/include/KPim5/Libkleo/Libkleo/KeyApprovalDialog
/usr/include/KPim5/Libkleo/Libkleo/KeyCache
/usr/include/KPim5/Libkleo/Libkleo/KeyFilter
/usr/include/KPim5/Libkleo/Libkleo/KeyFilterManager
/usr/include/KPim5/Libkleo/Libkleo/KeyGroup
/usr/include/KPim5/Libkleo/Libkleo/KeyGroupConfig
/usr/include/KPim5/Libkleo/Libkleo/KeyGroupImportExport
/usr/include/KPim5/Libkleo/Libkleo/KeyHelpers
/usr/include/KPim5/Libkleo/Libkleo/KeyList
/usr/include/KPim5/Libkleo/Libkleo/KeyListModel
/usr/include/KPim5/Libkleo/Libkleo/KeyListModelInterface
/usr/include/KPim5/Libkleo/Libkleo/KeyListSortFilterProxyModel
/usr/include/KPim5/Libkleo/Libkleo/KeyListView
/usr/include/KPim5/Libkleo/Libkleo/KeyRearrangeColumnsProxyModel
/usr/include/KPim5/Libkleo/Libkleo/KeyRequester
/usr/include/KPim5/Libkleo/Libkleo/KeyResolver
/usr/include/KPim5/Libkleo/Libkleo/KeyResolverCore
/usr/include/KPim5/Libkleo/Libkleo/KeySelectionCombo
/usr/include/KPim5/Libkleo/Libkleo/KeySelectionDialog
/usr/include/KPim5/Libkleo/Libkleo/KeyserverConfig
/usr/include/KPim5/Libkleo/Libkleo/KleoException
/usr/include/KPim5/Libkleo/Libkleo/MessageBox
/usr/include/KPim5/Libkleo/Libkleo/NavigatableTreeView
/usr/include/KPim5/Libkleo/Libkleo/NavigatableTreeWidget
/usr/include/KPim5/Libkleo/Libkleo/NewKeyApprovalDialog
/usr/include/KPim5/Libkleo/Libkleo/OidMap
/usr/include/KPim5/Libkleo/Libkleo/Predicates
/usr/include/KPim5/Libkleo/Libkleo/ProgressDialog
/usr/include/KPim5/Libkleo/Libkleo/QtStlHelpers
/usr/include/KPim5/Libkleo/Libkleo/ReaderPortSelection
/usr/include/KPim5/Libkleo/Libkleo/SCDaemon
/usr/include/KPim5/Libkleo/Libkleo/Stl_Util
/usr/include/KPim5/Libkleo/Libkleo/StringUtils
/usr/include/KPim5/Libkleo/Libkleo/SubkeyListModel
/usr/include/KPim5/Libkleo/Libkleo/SystemInfo
/usr/include/KPim5/Libkleo/Libkleo/Test
/usr/include/KPim5/Libkleo/Libkleo/UniqueLock
/usr/include/KPim5/Libkleo/Libkleo/UserIDListModel
/usr/include/KPim5/Libkleo/libkleo/algorithm.h
/usr/include/KPim5/Libkleo/libkleo/assuan.h
/usr/include/KPim5/Libkleo/libkleo/auditlogentry.h
/usr/include/KPim5/Libkleo/libkleo/auditlogviewer.h
/usr/include/KPim5/Libkleo/libkleo/checksumdefinition.h
/usr/include/KPim5/Libkleo/libkleo/chrono.h
/usr/include/KPim5/Libkleo/libkleo/classify.h
/usr/include/KPim5/Libkleo/libkleo/compat.h
/usr/include/KPim5/Libkleo/libkleo/compliance.h
/usr/include/KPim5/Libkleo/libkleo/cryptoconfig.h
/usr/include/KPim5/Libkleo/libkleo/cryptoconfigmodule.h
/usr/include/KPim5/Libkleo/libkleo/debug.h
/usr/include/KPim5/Libkleo/libkleo/defaultkeyfilter.h
/usr/include/KPim5/Libkleo/libkleo/defaultkeygenerationjob.h
/usr/include/KPim5/Libkleo/libkleo/directoryserviceswidget.h
/usr/include/KPim5/Libkleo/libkleo/dn.h
/usr/include/KPim5/Libkleo/libkleo/dnattributeorderconfigwidget.h
/usr/include/KPim5/Libkleo/libkleo/docaction.h
/usr/include/KPim5/Libkleo/libkleo/editdirectoryservicedialog.h
/usr/include/KPim5/Libkleo/libkleo/enum.h
/usr/include/KPim5/Libkleo/libkleo/expirychecker.h
/usr/include/KPim5/Libkleo/libkleo/expirycheckerconfig.h
/usr/include/KPim5/Libkleo/libkleo/expirycheckerconfigbase.h
/usr/include/KPim5/Libkleo/libkleo/expirycheckersettings.h
/usr/include/KPim5/Libkleo/libkleo/filenamerequester.h
/usr/include/KPim5/Libkleo/libkleo/filesystemwatcher.h
/usr/include/KPim5/Libkleo/libkleo/formatting.h
/usr/include/KPim5/Libkleo/libkleo/gnupg.h
/usr/include/KPim5/Libkleo/libkleo/hex.h
/usr/include/KPim5/Libkleo/libkleo/kconfigbasedkeyfilter.h
/usr/include/KPim5/Libkleo/libkleo/keyapprovaldialog.h
/usr/include/KPim5/Libkleo/libkleo/keycache.h
/usr/include/KPim5/Libkleo/libkleo/keyfilter.h
/usr/include/KPim5/Libkleo/libkleo/keyfiltermanager.h
/usr/include/KPim5/Libkleo/libkleo/keygroup.h
/usr/include/KPim5/Libkleo/libkleo/keygroupconfig.h
/usr/include/KPim5/Libkleo/libkleo/keygroupimportexport.h
/usr/include/KPim5/Libkleo/libkleo/keyhelpers.h
/usr/include/KPim5/Libkleo/libkleo/keylist.h
/usr/include/KPim5/Libkleo/libkleo/keylistmodel.h
/usr/include/KPim5/Libkleo/libkleo/keylistmodelinterface.h
/usr/include/KPim5/Libkleo/libkleo/keylistsortfilterproxymodel.h
/usr/include/KPim5/Libkleo/libkleo/keylistview.h
/usr/include/KPim5/Libkleo/libkleo/keyrearrangecolumnsproxymodel.h
/usr/include/KPim5/Libkleo/libkleo/keyrequester.h
/usr/include/KPim5/Libkleo/libkleo/keyresolver.h
/usr/include/KPim5/Libkleo/libkleo/keyresolvercore.h
/usr/include/KPim5/Libkleo/libkleo/keyselectioncombo.h
/usr/include/KPim5/Libkleo/libkleo/keyselectiondialog.h
/usr/include/KPim5/Libkleo/libkleo/keyserverconfig.h
/usr/include/KPim5/Libkleo/libkleo/kleo_export.h
/usr/include/KPim5/Libkleo/libkleo/kleoexception.h
/usr/include/KPim5/Libkleo/libkleo/messagebox.h
/usr/include/KPim5/Libkleo/libkleo/navigatabletreeview.h
/usr/include/KPim5/Libkleo/libkleo/navigatabletreewidget.h
/usr/include/KPim5/Libkleo/libkleo/newkeyapprovaldialog.h
/usr/include/KPim5/Libkleo/libkleo/oidmap.h
/usr/include/KPim5/Libkleo/libkleo/predicates.h
/usr/include/KPim5/Libkleo/libkleo/progressdialog.h
/usr/include/KPim5/Libkleo/libkleo/qtstlhelpers.h
/usr/include/KPim5/Libkleo/libkleo/readerportselection.h
/usr/include/KPim5/Libkleo/libkleo/scdaemon.h
/usr/include/KPim5/Libkleo/libkleo/stl_util.h
/usr/include/KPim5/Libkleo/libkleo/stringutils.h
/usr/include/KPim5/Libkleo/libkleo/subkeylistmodel.h
/usr/include/KPim5/Libkleo/libkleo/systeminfo.h
/usr/include/KPim5/Libkleo/libkleo/test.h
/usr/include/KPim5/Libkleo/libkleo/uniquelock.h
/usr/include/KPim5/Libkleo/libkleo/useridlistmodel.h
/usr/include/KPim5/Libkleo/libkleo_version.h
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoConfig.cmake
/usr/lib64/cmake/KF5Libkleo/KF5LibkleoConfigVersion.cmake
/usr/lib64/cmake/KF5Libkleo/KPim5LibkleoTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Libkleo/KPim5LibkleoTargets.cmake
/usr/lib64/cmake/KPim5Libkleo/KPim5LibkleoConfig.cmake
/usr/lib64/cmake/KPim5Libkleo/KPim5LibkleoConfigVersion.cmake
/usr/lib64/cmake/KPim5Libkleo/KPim5LibkleoTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Libkleo/KPim5LibkleoTargets.cmake
/usr/lib64/libKPim5Libkleo.so
/usr/lib64/qt5/mkspecs/modules/qt_Libkleo.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Libkleo.so.5.24.3
/usr/lib64/libKPim5Libkleo.so.5
/usr/lib64/libKPim5Libkleo.so.5.24.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkleo/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libkleo/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libkleo/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libkleo/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/libkleo/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libkleo/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkleo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkleo/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkleopatra.lang
%defattr(-,root,root,-)

