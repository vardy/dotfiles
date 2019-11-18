#!/usr/bin/env bash

killall -q polybar

if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do

    # pkill used to kill system tray provided by KDE
    pkill xembedsniproxy

    MONITOR=$m polybar --reload main &
    MONITOR=$m polybar --reload invis_bottom &
  done
else

  # pkill used to kill system tray provided by KDE
  pkill xembedsniproxy

  polybar --reload main &
  polybar --reload invis_bottom &
fi

#while pgrep -u $UID -x polybar >/dev/nul ; do sleep 1; done
#polybar main -q -r &

