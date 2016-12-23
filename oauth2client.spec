#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauth2client
Version  : 4.0.0
Release  : 11
URL      : http://pypi.debian.net/oauth2client/oauth2client-4.0.0.tar.gz
Source0  : http://pypi.debian.net/oauth2client/oauth2client-4.0.0.tar.gz
Summary  : OAuth 2.0 client library
Group    : Development/Tools
License  : Apache-2.0
Requires: oauth2client-python
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
Requires: httplib2

%description python
python components for the oauth2client package.


%prep
%setup -q -n oauth2client-4.0.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
