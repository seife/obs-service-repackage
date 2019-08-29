#
# spec file for package obs-service-repackage
#
# Copyright (c) 2019 Stefan Seyfried
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           obs-service-repackage
Version:        0
Release:        0
Summary:        OBS source service that repackages binary rpms
License:        0BSD
Group:          Development/Tools/Building
Url:            https://github.wdf.sap.corp/d064615/obs-service-repackage
Source:         obs-service-repackage-%{version}.tar
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This OBS source service repackages binary rpms inside OBS.

%prep
%setup -q

%build

%install
%make_install

%files
%defattr(-,root,root)
/usr/lib/obs/service/*

%changelog

