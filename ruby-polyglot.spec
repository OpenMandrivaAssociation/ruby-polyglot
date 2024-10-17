%define rname	polyglot

Name:		ruby-%{rname}
Summary:	Ruby library allowing a module to register a file type loader
Version:	0.3.3
Release:	2
License:	MIT
Group:		Development/Ruby
URL:		https://rubygems.org/gems/polyglot
Source0:	http://rubygems.org/downloads/polyglot-0.3.3.gem
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
The Polyglot library allows a Ruby module to register a loader for the file
type associated with a filename extension, and it augments 'require' to find
and load matching files.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{rname}-%{version}


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.3.3-1
+ Revision: 796026
- imported package ruby-polyglot

