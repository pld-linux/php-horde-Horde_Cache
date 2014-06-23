%define		status		stable
%define		pearname	Horde_Cache
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Caching API
Name:		php-horde-Horde_Cache
Version:	1.0.5
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	301b46849b96698077a569dcdb238851
URL:		https://github.com/horde/horde/tree/master/framework/Cache/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(hash)
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-eaccelerator
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Log
Suggests:	php-horde-Horde_Memcache
# http://bugs.horde.org/ticket/10031
Suggests:	php(apc)
Suggests:	php(lzf)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Db.*) pear(Horde/Log.*) pear(Horde/Memcache.*) pear(lzf.*)

%description
This package provides a simple, functional caching API, with the
option to store the cached data on the filesystem, in one of the PHP
opcode cache systems (APC, eAcclerator, XCache, or Zend Performance
Suite's content cache), memcached, or an SQL table.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Cache
%{php_pear_dir}/Horde/Cache.php
%{php_pear_dir}/data/Horde_Cache
