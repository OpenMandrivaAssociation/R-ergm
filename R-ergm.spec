%global packname  ergm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.0.3
Release:          1
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Networks
Group:            Sciences/Mathematics
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ergm_3.0-3.tar.gz
Requires:         R-network R-nlme R-trust 
Requires:         R-coda R-KernSmooth R-sna R-Rglpk R-robustbase R-Matrix 
Requires:         R-latticeExtra
Requires:         R-networkDynamic
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-network R-nlme R-trust
BuildRequires:    R-coda R-KernSmooth R-sna R-Rglpk R-robustbase R-Matrix 
BuildRequires:    R-latticeExtra
BuildRequires:    R-networkDynamic

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGM). "ergm" is a part of the
"statnet" suite of packages for network analysis.  For a list of functions
type: help(package='ergm')

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/help


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4_3-1
+ Revision: 777184
- Import R-ergm
- Import R-ergm


