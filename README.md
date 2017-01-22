#PyTimer, a simple egg (countdown) timer in Python/Tk

![screenshot](https://github.com/mdoege/PyTimer/raw/master/screenshot.png "PyBrite screenshot")

##Usage

Enter the number of minutes into the text entry widget, then press Return or click the Start button. When the countdown is over, the Start button turns into a Quit button.

On Linux, the Start button will also turn yellow during the final 30 seconds and red at the end.

There is no way to reset, pause, or restart the timer (on purpose, so disabling it by accident is impossible, unless you close the window), so you need to restart the program in that event.

Note that the timer uses an absolute alarm time, so even if you suspend the system during the countdown for some time, it will not affect the alarm time. (This is different from a naive timer which would ignore time spent in suspend mode.)
