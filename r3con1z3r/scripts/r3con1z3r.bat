:://///////////////////////////////////////////////////////
::				AUTOMATIC RUN SCRIPT
::	This script is to be visible on PATH. It gets stored
::		in Python/Scripts and makes the program into a command line 
:: argument
:://////////////////////////////////////////////////////////
@echo OFF
:: Get python variable
FOR /F "delims=" %i IN ('where python') DO set PYTHON=%i
cls
%PYTHON% -m r3con1z3r.main %* || python -m r3con1z3r.main %* || python2 -m r3con1z3r.main %* || python3 -m r3con1z3r.main %*
pause
