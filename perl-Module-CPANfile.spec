#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-CPANfile
Version  : 1.1004
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-1.1004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-1.1004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-cpanfile-perl/libmodule-cpanfile-perl_1.1004-1.debian.tar.xz
Summary  : 'Parse cpanfile'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-CPANfile-bin = %{version}-%{release}
Requires: perl-Module-CPANfile-license = %{version}-%{release}
Requires: perl-Module-CPANfile-man = %{version}-%{release}
Requires: perl-Module-CPANfile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::pushd)

%description
NAME
Module::CPANfile - Parse cpanfile
SYNOPSIS
use Module::CPANfile;

my $file = Module::CPANfile->load("cpanfile");
my $prereqs = $file->prereqs; # CPAN::Meta::Prereqs object

my @features = $file->features; # CPAN::Meta::Feature objects
my $merged_prereqs = $file->prereqs_with(@identifiers); # CPAN::Meta::Prereqs

$file->merge_meta('MYMETA.json');

%package bin
Summary: bin components for the perl-Module-CPANfile package.
Group: Binaries
Requires: perl-Module-CPANfile-license = %{version}-%{release}

%description bin
bin components for the perl-Module-CPANfile package.


%package dev
Summary: dev components for the perl-Module-CPANfile package.
Group: Development
Requires: perl-Module-CPANfile-bin = %{version}-%{release}
Provides: perl-Module-CPANfile-devel = %{version}-%{release}
Requires: perl-Module-CPANfile = %{version}-%{release}

%description dev
dev components for the perl-Module-CPANfile package.


%package license
Summary: license components for the perl-Module-CPANfile package.
Group: Default

%description license
license components for the perl-Module-CPANfile package.


%package man
Summary: man components for the perl-Module-CPANfile package.
Group: Default

%description man
man components for the perl-Module-CPANfile package.


%package perl
Summary: perl components for the perl-Module-CPANfile package.
Group: Default
Requires: perl-Module-CPANfile = %{version}-%{release}

%description perl
perl components for the perl-Module-CPANfile package.


%prep
%setup -q -n Module-CPANfile-1.1004
cd %{_builddir}
tar xf %{_sourcedir}/libmodule-cpanfile-perl_1.1004-1.debian.tar.xz
cd %{_builddir}/Module-CPANfile-1.1004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Module-CPANfile-1.1004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-CPANfile
cp %{_builddir}/Module-CPANfile-1.1004/LICENSE %{buildroot}/usr/share/package-licenses/perl-Module-CPANfile/e2bf2b3ac4866a03601003b6ce3da0658f45b720
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Module-CPANfile/7f14f95fb6443ecb2ab0f2d92f8c172c836007ec
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cpanfile-dump
/usr/bin/mymeta-cpanfile

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::CPANfile.3
/usr/share/man/man3/cpanfile-faq.3
/usr/share/man/man3/cpanfile.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-CPANfile/7f14f95fb6443ecb2ab0f2d92f8c172c836007ec
/usr/share/package-licenses/perl-Module-CPANfile/e2bf2b3ac4866a03601003b6ce3da0658f45b720

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpanfile-dump.1
/usr/share/man/man1/mymeta-cpanfile.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Module/CPANfile.pm
/usr/lib/perl5/vendor_perl/5.30.2/Module/CPANfile/Environment.pm
/usr/lib/perl5/vendor_perl/5.30.2/Module/CPANfile/Prereq.pm
/usr/lib/perl5/vendor_perl/5.30.2/Module/CPANfile/Prereqs.pm
/usr/lib/perl5/vendor_perl/5.30.2/Module/CPANfile/Requirement.pm
/usr/lib/perl5/vendor_perl/5.30.2/cpanfile-faq.pod
/usr/lib/perl5/vendor_perl/5.30.2/cpanfile.pod
