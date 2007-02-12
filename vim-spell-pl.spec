Summary:	Polish dictionaries for VIMspell
Summary(pl.UTF-8):   Polskie słowniki dla VIMspella
Name:		vim-spell-pl
Version:	20060706
Release:	1
License:	Creative Commons License
Group:		Applications/Editors/Vim
Source0:	http://www.kurnik.pl/slownik/ort/alt-myspell-pl-%{version}.tar.bz2
# Source0-md5:	220ed496783615896d35d057342ac5e9
# vim-7.0/vim70/runtime/spell/pl/pl_PL.diff
Patch0:		%{name}-pl_PL.diff
URL:		http://www.kurnik.pl/slownik/ort/
BuildRequires:	vim >= 4:7.0
Requires:	vim >= 4:7.0.017-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish dictionaries for VIMspell.

%description -l pl.UTF-8
Polskie słowniki dla VIMspella.

%prep
%setup -q -n alt-myspell-pl-%{version}
%patch0 -p0

%build
vim -u NONE -c 'set enc=iso-8859-2' -c 'mkspell! pl pl_PL' -c q
vim -u NONE -c 'set enc=utf-8' -c 'mkspell! pl pl_PL' -c q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/spell

install *.spl $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/spell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_pl_PL.txt
%{_datadir}/vim/vimfiles/spell/pl.*.spl
