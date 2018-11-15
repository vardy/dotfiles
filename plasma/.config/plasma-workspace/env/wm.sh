# Disable KWin and use i3gaps as WM
export KDEWM=/usr/bin/i3
#export KDEWM=$HOME/Documents/Repositories/uwurawrxdwm/uwurawrxdwm

# Compositor (Animations, Shadows, Transparency)
# xcompmgr -C
compton -b --config ~/.config/compton/compton.conf
