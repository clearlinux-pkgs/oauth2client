#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauth2client
Version  : 4.1.3
Release  : 42
URL      : https://files.pythonhosted.org/packages/a6/7b/17244b1083e8e604bf154cf9b716aecd6388acd656dd01893d0d244c94d9/oauth2client-4.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/7b/17244b1083e8e604bf154cf9b716aecd6388acd656dd01893d0d244c94d9/oauth2client-4.1.3.tar.gz
Summary  : OAuth 2.0 client library
Group    : Development/Tools
License  : Apache-2.0
Requires: oauth2client-license = %{version}-%{release}
Requires: oauth2client-python = %{version}-%{release}
Requires: oauth2client-python3 = %{version}-%{release}
Requires: httplib2
Requires: pyasn1
Requires: pyasn1-modules
Requires: rsa
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : httplib2
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : rsa
BuildRequires : six

%description
[![Build Status](https://travis-ci.org/google/oauth2client.svg?branch=master)](https://travis-ci.org/google/oauth2client)
[![Coverage Status](https://coveralls.io/repos/google/oauth2client/badge.svg?branch=master&service=github)](https://coveralls.io/github/google/oauth2client?branch=master)
[![Documentation Status](https://readthedocs.org/projects/oauth2client/badge/?version=latest)](https://oauth2client.readthedocs.io/)

%package license
Summary: license components for the oauth2client package.
Group: Default

%description license
license components for the oauth2client package.


%package python
Summary: python components for the oauth2client package.
Group: Default
Requires: oauth2client-python3 = %{version}-%{release}

%description python
python components for the oauth2client package.


%package python3
Summary: python3 components for the oauth2client package.
Group: Default
Requires: python3-core
Provides: pypi(oauth2client)

%description python3
python3 components for the oauth2client package.


%prep
%setup -q -n oauth2client-4.1.3
cd %{_builddir}/oauth2client-4.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583188915
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oauth2client
cp %{_builddir}/oauth2client-4.1.3/LICENSE %{buildroot}/usr/share/package-licenses/oauth2client/a7b6feb97b476557d3d699fa1f20090fb956d662
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oauth2client/a7b6feb97b476557d3d699fa1f20090fb956d662

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
