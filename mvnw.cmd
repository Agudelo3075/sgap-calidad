@REM ----------------------------------------------------------------------------
@REM Maven Wrapper script for Windows
@REM ----------------------------------------------------------------------------
@echo off
setlocal
call mvn %*
if %ERRORLEVEL% NEQ 0 (
    echo Asegurese de tener Maven instalado y en el PATH.
)
endlocal

