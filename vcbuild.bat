@echo off
SET GYP_MSVS_VERSION=2013
cmd /c "..\gyp\gyp softhsm2.gyp --depth=."
REM ..\..\gyp\gyp -G GYP_MSVS_VERSION=2013 softhsm2.gyp --depth=.
msbuild softhsm2.sln