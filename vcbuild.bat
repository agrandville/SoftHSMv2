@echo off
echo initializing submodule ...
git submodule init
git submodule update

if "%VS120COMNTOOLS%"=="" goto checkvs2014
call "%VS120COMNTOOLS%vsvars32.bat"
SET GYP_MSVS_VERSION=2013
goto launch

:checkvs2014
if "%VS140COMNTOOLS%"=="" goto novs
call "%VS120COMNTOOLS%vsvars32.bat"
SET GYP_MSVS_VERSION=2014
goto launch

:novs
echo "no visual studio found"
goto end

:launch
echo "generating ..."
cmd /c "third_party\gyp\gyp softhsm2.gyp --depth=."
REM ..\..\gyp\gyp -G GYP_MSVS_VERSION=2013 softhsm2.gyp --depth=.
msbuild softhsm2.sln
:end
