Summary:	Polish dictionaries for VIMspell
Summary(pl.UTF-8):	Polskie słowniki dla VIMspella
Name:		vim-spell-pl
Version:	20090211
Release:	1
License:	Creative Commons License
Group:		Applications/Editors/Vim
Source0:	http://sjp.pl/slownik/ort/sjp-myspell-pl-%{version}.zip
# Source0-md5:	b40c883974ead372444560fd56ced70d
# vim-7.0/vim70/runtime/spell/pl/pl_PL.diff
Patch0:		%{name}-pl_PL.diff
URL:		http://www.sjp.pl/slownik/ort/
BuildRequires:	unzip
BuildRequires:	vim >= 4:7.0
Requires:	vim-rt >= 4:7.0.017-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Polish dictionaries for VIMspell.

%description -l pl.UTF-8
Polskie słowniki dla VIMspella.

%prep
%setup -q -c
unzip pl_PL.zip
%patch0 -p0

%build
vim -u NONE -c 'set enc=iso-8859-2' -c 'mkspell! pl pl_PL' -c q
vim -u NONE -c 'set enc=utf-8' -c 'mkspell! pl pl_PL' -c q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/spell

install *.spl $RPM_BUILD_ROOT%{_vimdatadir}/spell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_pl_PL.txt
%{_vimdatadir}/spell/pl.*.spl
