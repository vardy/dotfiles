# Default directory
tmux new -A -s Main
cd ~

# Oh-My-ZSH Setup
export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="spaceship"
plugins=(tmux z colored-man-pages docker)

ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="true"

SPACESHIP_CHAR_SYMBOL="♪ "

source $ZSH/oh-my-zsh.sh

# Configuration
HIST_STAMPS="yyyy/mm/dd"
export MANPATH="/usr/local/man:$MANPATH"
export LANG=en_US.UTF-8
export EDITOR="vim"

# Aliases
alias docker="/mnt/c/Program\ Files/Docker/Docker/Resources/bin/docker.exe"
alias docker-compose="/mnt/c/Program\ Files/Docker/Docker/Resources/bin/docker-compose.exe"
alias dck="/mnt/c/Program\ Files/Docker/Docker/Resources/bin/docker.exe"
alias dckc="/mnt/c/Program\ Files/Docker/Docker/Resources/bin/docker-compose.exe"

alias gs="git status"
alias gaa="git add ."
alias gc="git commit"
