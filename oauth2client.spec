#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauth2client
Version  : 4.1.1
Release  : 14
URL      : http://pypi.debian.net/oauth2client/oauth2client-4.1.1.tar.gz
Source0  : http://pypi.debian.net/oauth2client/oauth2client-4.1.1.tar.gz
Summary  : OAuth 2.0 client library
Group    : Development/Tools
License  : Apache-2.0
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
[![Build Status](https://travis-ci.org/google/oauth2client.svg?branch=master)](https://travis-ci.org/google/oauth2client)
[![Coverage Status](https://coveralls.io/repos/google/oauth2client/badge.svg?branch=master&service=github)](https://coveralls.io/github/google/oauth2client?branch=master)
[![Documentation Status](https://readthedocs.org/projects/oauth2client/badge/?version=latest)](https://oauth2client.readthedocs.io/)

%package python
Summary: python components for the oauth2client package.
Group: Default

%description python
python components for the oauth2client package.


%prep
%setup -q -n oauth2client-4.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496774297
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1496774297
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
