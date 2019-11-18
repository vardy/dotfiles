export ZSH="/home/pants/.oh-my-zsh"

ZSH_THEME="robbyrussell"
ZSH_THEME="spaceship"

HYPHEN_INSENSITIVE="true"
ENABLE_CORRECTION="true"

plugins=(
  git
  archlinux
  docker
  tmux
)

source $ZSH/oh-my-zsh.sh

setxkbmap -option caps:escape

# Aliases
alias _weather="curl wttr.in/Singapore"
alias _scr="escrotum"
alias _ip="curl ifconfig.me"
alias _loc="bash ~/.scripts/ip_loc.sh"
alias _vpn="expressvpn status"
alias _bdl="beautifuldiscord --css ~/.scripts/.discord.css"
alias _bdr="beautifuldiscord --revert"
alias _hibernate="betterlockscreen -s"
alias _shutdown="sudo shutdown -h now"
alias _reboot="sudo reboot"
alias _lock="betterlockscreen -l"
alias _poly="bash ~/.config/polybar/startup.sh"

# Setting fpath
fpath=($fpath "/home/pants/.zfunctions")

# Set Spaceship ZSH as a prompt
autoload -U promptinit; promptinit
prompt spaceship

# Loads scripts
. ~/.scripts/z.sh
