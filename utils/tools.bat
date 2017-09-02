@echo off
set OLDDIR=%CD%

call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
call "C:\Qt\Qt5.9.0\5.9.1\msvc2017_64\bin\qtenv2.bat"
doskey nmake="C:\Qt\Qt5.9.0\Tools\QtCreator\bin\jom.exe" $*

chdir /d %OLDDIR%
