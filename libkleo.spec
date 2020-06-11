#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkleo
Version  : 20.04.2
Release  : 23
URL      : https://download.kde.org/stable/release-service/20.04.2/src/libkleo-20.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.2/src/libkleo-20.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.2/src/libkleo-20.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libkleo-data = %{version}-%{release}
Requires: libkleo-lib = %{version}-%{release}
Requires: libkleo-license = %{version}-%{release}
Requires: libkleo-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kitemmodels-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

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
%setup -q -n libkleo-20.04.2
cd %{_builddir}/libkleo-20.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591890590
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591890590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkleo
cp %{_builddir}/libkleo-20.04.2/COPYING %{buildroot}/usr/share/package-licenses/libkleo/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/libkleo-20.04.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkleo/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/include/KF5/Libkleo/ChecksumDefinition
/usr/include/KF5/Libkleo/Classify
/usr/include/KF5/Libkleo/CryptoConfigDialog
/usr/include/KF5/Libkleo/CryptoConfigModule
/usr/include/KF5/Libkleo/DNAttributeOrderConfigWidget
/usr/include/KF5/Libkleo/DefaultKeyFilter
/usr/include/KF5/Libkleo/DefaultKeyGenerationJob
/usr/include/KF5/Libkleo/DirectoryServicesWidget
/usr/include/KF5/Libkleo/Dn
/usr/include/KF5/Libkleo/Enum
/usr/include/KF5/Libkleo/Exception
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
/usr/include/KF5/Libkleo/KeyListModel
/usr/include/KF5/Libkleo/KeyListModelInterface
/usr/include/KF5/Libkleo/KeyListSortFilterProxyModel
/usr/include/KF5/Libkleo/KeyRearrangeColumnsProxyModel
/usr/include/KF5/Libkleo/KeyRequester
/usr/include/KF5/Libkleo/KeyResolver
/usr/include/KF5/Libkleo/KeySelectionCombo
/usr/include/KF5/Libkleo/KeySelectionDialog
/usr/include/KF5/Libkleo/MessageBox
/usr/include/KF5/Libkleo/NewKeyApprovalDialog
/usr/include/KF5/Libkleo/OidMap
/usr/include/KF5/Libkleo/Predicates
/usr/include/KF5/Libkleo/ProgressDialog
/usr/include/KF5/Libkleo/Stl_Util
/usr/include/KF5/Libkleo/SubkeyListModel
/usr/include/KF5/Libkleo/UserIDListModel
/usr/include/KF5/libkleo/checksumdefinition.h
/usr/include/KF5/libkleo/classify.h
/usr/include/KF5/libkleo/cryptoconfigdialog.h
/usr/include/KF5/libkleo/cryptoconfigmodule.h
/usr/include/KF5/libkleo/defaultkeyfilter.h
/usr/include/KF5/libkleo/defaultkeygenerationjob.h
/usr/include/KF5/libkleo/directoryserviceswidget.h
/usr/include/KF5/libkleo/dn.h
/usr/include/KF5/libkleo/dnattributeorderconfigwidget.h
/usr/include/KF5/libkleo/enum.h
/usr/include/KF5/libkleo/exception.h
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
/usr/include/KF5/libkleo/keylistmodel.h
/usr/include/KF5/libkleo/keylistmodelinterface.h
/usr/include/KF5/libkleo/keylistsortfilterproxymodel.h
/usr/include/KF5/libkleo/keyrearrangecolumnsproxymodel.h
/usr/include/KF5/libkleo/keyrequester.h
/usr/include/KF5/libkleo/keyresolver.h
/usr/include/KF5/libkleo/keyselectioncombo.h
/usr/include/KF5/libkleo/keyselectiondialog.h
/usr/include/KF5/libkleo/kleo_export.h
/usr/include/KF5/libkleo/messagebox.h
/usr/include/KF5/libkleo/newkeyapprovaldialog.h
/usr/include/KF5/libkleo/oidmap.h
/usr/include/KF5/libkleo/predicates.h
/usr/include/KF5/libkleo/progressdialog.h
/usr/include/KF5/libkleo/stl_util.h
/usr/include/KF5/libkleo/subkeylistmodel.h
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
/usr/lib64/libKF5Libkleo.so.5.14.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkleo/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/libkleo/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libkleopatra.lang
%defattr(-,root,root,-)

