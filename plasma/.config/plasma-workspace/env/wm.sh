# Disable KWin and use i3gaps as WM
export KDEWM=/usr/bin/i3
#export KDEWM=$HOME/Documents/Repositories/uwurawrxdwm/uwurawrxdwm
#export KDEWM=/usr/bin/herbstluftwm

# Compositor (Animations, Shadows, Transparency)
# xcompmgr -C
compton -b --config ~/.config/compton/compton.conf
