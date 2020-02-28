#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : weakrefmethod
Version  : 1.0.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/99/82/73a21e3eab9a1ff76d12375f7301fba5c6325b9598eed0ae5b0cf5243656/weakrefmethod-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/99/82/73a21e3eab9a1ff76d12375f7301fba5c6325b9598eed0ae5b0cf5243656/weakrefmethod-1.0.3.tar.gz
Summary  : A WeakMethod class for storing bound methods using weak references.
Group    : Development/Tools
License  : Python-2.0
Requires: weakrefmethod-license = %{version}-%{release}
Requires: weakrefmethod-python = %{version}-%{release}
Requires: weakrefmethod-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : unittest2

%description
Python 3.4 include a ``WeakMethod`` class, for storing bound methods using weak references
(see the `Python weakref module <http://docs.python.org/library/weakref.html>`_).

This project is a backport of the WeakMethod class, and tests, for Python 2.6. The tests
require the `unittest2 package <http://pypi.python.org/pypi/unittest2>`_.

* Github repository & issue tracker: https://github.com/twang817/weakrefmethod

%package license
Summary: license components for the weakrefmethod package.
Group: Default

%description license
license components for the weakrefmethod package.


%package python
Summary: python components for the weakrefmethod package.
Group: Default
Requires: weakrefmethod-python3 = %{version}-%{release}

%description python
python components for the weakrefmethod package.


%package python3
Summary: python3 components for the weakrefmethod package.
Group: Default
Requires: python3-core
Provides: pypi(weakrefmethod)

%description python3
python3 components for the weakrefmethod package.


%prep
%setup -q -n weakrefmethod-1.0.3
cd %{_builddir}/weakrefmethod-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582903844
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/weakrefmethod
cp %{_builddir}/weakrefmethod-1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/weakrefmethod/903854d1e304992e931b07e4c076491e35e35e71
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/weakrefmethod/903854d1e304992e931b07e4c076491e35e35e71

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
