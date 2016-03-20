rem @echo off
echo initializing submodule ...
git submodule init
git submodule update

if "%VS120COMNTOOLS%"=="" goto checkvs2014
call "%VS120COMNTOOLS%vsvars32.bat"
SET GYP_MSVS_VERSION=2013
goto OpenSSLdepends

:checkvs2014
if "%VS140COMNTOOLS%"=="" goto novs
call "%VS140COMNTOOLS%vsvars32.bat"
SET GYP_MSVS_VERSION=2014
goto OpenSSLdepends

:novs
echo "no visual studio found"
goto end

:OpenSSLdepends
if exist third_party\openssl goto CPPunitdepends
powershell Invoke-WebRequest http://grandville.net/download/OpenSSL1.0.2g.vs120.MTd.noSymbols.zip -out third_party\OpenSSL1.0.2g.vs120.MTd.noSymbols.zip
powershell Expand-Archive third_party\OpenSSL1.0.2g.vs120.MTd.noSymbols.zip third_party\


:CPPunitdepends
if exist third_party\cppunit goto Build
powershell Invoke-WebRequest http://grandville.net/download/CppUnit1.14.0.vs120.zip -out third_party\CppUnit1.14.0.vs120.zip
powershell Expand-Archive third_party\CppUnit1.14.0.vs120.zip third_party\

:Build
echo "generating ..."
cmd /c "third_party\gyp\gyp softhsm2.gyp --depth=."
REM ..\..\gyp\gyp -G GYP_MSVS_VERSION=2013 softhsm2.gyp --depth=.
msbuild softhsm2.sln
:end
