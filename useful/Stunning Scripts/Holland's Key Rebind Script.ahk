#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Control::Send, {Control}
return

F5::
Send, {Click}
return

F4::
Send, {Delete Down}
KeyWait, %A_ThisHotkey%
Send, {Delete Up}
return

F6::Reload
return
