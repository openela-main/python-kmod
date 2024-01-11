%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-kmod
License:        LGPLv2+
Group:          Development/Libraries
Summary:        Python module to work with kernel modules
Version:        0.9
Release:        20%{?dist}
URL:            https://github.com/agrover/python-kmod/
Source0:        https://github.com/downloads/agrover/%{name}/%{name}-%{version}.tar.gz


%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-Cython
%endif # with python2

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython

BuildRequires:  kmod-devel

%if %{with python2}
%{?filter_setup:
%filter_provides_in %{python2_sitearch}.*\.so$
%filter_setup
}
%endif # with python2

%global _description\
Python module to allow listing, loading, and unloading\
Linux kernel modules, using libkmod.

%description %_description

%if %{with python2}
%package -n python2-kmod
Summary: %summary
%{?python_provide:%python_provide python2-kmod}

%description -n python2-kmod %_description
%endif # with python2

%package -n python3-kmod
Group:          Development/Libraries
Summary:        Python module to work with kernel modules
%{?python_provide:%python_provide python3-kmod}

%description -n python3-kmod
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

%prep
%setup -q

%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install

%if %{with python2}
%files -n python2-kmod
%{python2_sitearch}/kmod/
%{python2_sitearch}/kmod*.egg-info
%doc README
%license COPYING.LESSER
%endif # with python2

%files -n python3-kmod
%{python3_sitearch}/kmod/
%{python3_sitearch}/kmod*.egg-info
%doc README
%license COPYING.LESSER

%changelog
* Fri Jun 08 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.9-20
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 0.9-17
- Fix directory ownership

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-16
- Python 2 binary package renamed to python2-kmod
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9-13
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Andy Grover <agrover@redhat.com> - 0.9-6
- Initial Python 3 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Andy Grover <agrover@redhat.com> - 0.9-1
- Update for new upstream release
- Add build dep on Cython

* Wed Aug 1 2012 Andy Grover <agrover@redhat.com> - 0.1-4
- Update for new upstream release location

* Fri May 4 2012 Andy Grover <agrover@redhat.com> - 0.1-3
- Update for new upstream release location

* Tue Apr 17 2012 Andy Grover <agrover@redhat.com> - 0.1-2
- Correct License field to LGPLv2+
- Remove explicit Requires for kmod-libs

* Thu Apr 12 2012 Andy Grover <agrover@redhat.com> - 0.1-1
- Initial packaging
