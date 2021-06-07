dim fso
dim curDir
dim WinScriptHost
set fso = CreateObject("Scripting.FileSystemObject")
curDir = fso.GetAbsolutePathName(".")
set fso = nothing
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run curDir & "/start/starter.bat", 1
set WinScriptHost = nothing