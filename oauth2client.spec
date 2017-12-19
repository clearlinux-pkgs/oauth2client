#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauth2client
Version  : 4.1.2
Release  : 20
URL      : http://pypi.debian.net/oauth2client/oauth2client-4.1.2.tar.gz
Source0  : http://pypi.debian.net/oauth2client/oauth2client-4.1.2.tar.gz
Summary  : OAuth 2.0 client library
Group    : Development/Tools
License  : Apache-2.0
Requires: oauth2client-legacypython
Requires: oauth2client-python3
Requires: oauth2client-python
Requires: httplib2
Requires: pyasn1
Requires: pyasn1-modules
Requires: rsa
Requires: six
BuildRequires : httplib2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : rsa
BuildRequires : setuptools
BuildRequires : six

%description
oauth2client is a client library for OAuth 2.0.

%package legacypython
Summary: legacypython components for the oauth2client package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the oauth2client package.


%package python
Summary: python components for the oauth2client package.
Group: Default
Requires: oauth2client-legacypython
Requires: oauth2client-python3

%description python
python components for the oauth2client package.


%package python3
Summary: python3 components for the oauth2client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oauth2client package.


%prep
%setup -q -n oauth2client-4.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507163383
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507163383
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
