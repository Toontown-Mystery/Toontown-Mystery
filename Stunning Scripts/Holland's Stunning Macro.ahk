#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance, Force

Control::Send, {Control}
return

`:: 
    Send, {Control Down}
    Sleep, 10
    Send {V}
    Sleep, 10
    Send, {Control Up}

F7::
    {
        Loop
        {
         Send, {Delete}
         Sleep, 2
        }
    }
return

F6::Reload
return

F5::
    while GetKeyState("F5","P")
    {
        Send, {Delete}
        Sleep, 2
    }
return

F4::
    Send, {Delete Down}
    Sleep, 195
    Send, {Delete Up}
return

F3::
    Send, {Delete Down}
    Sleep, 180
    Send, {Delete Up}
return

F2::
    Send, {Delete Down}
    Sleep, 150
    Send, {Delete Up}
   
return

F1::
    Send, {Delete Down}
    Sleep, 120
    Send, {Delete Up}
return

^`::
    ExitApp