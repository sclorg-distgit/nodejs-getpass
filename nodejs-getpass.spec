%{?scl:%scl_package nodejs-getpass}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name getpass

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.1.6
Release:    2%{?dist}
Summary:    getpass for node
License:    MIT
URL:        https://github.com/arekinath/node-getpass.git
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
getpass for node.js

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Fri Sep 23 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.6-2
- Built with scl macros

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.6-1
- Initial build

