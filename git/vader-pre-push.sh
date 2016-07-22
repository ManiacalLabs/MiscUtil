#!/bin/sh
# Written by Adam Haile - Maniacal Labs (adam@maniacallabs.com)
# Inspired by: https://gist.github.com/pixelhandler/5718585
# Install: cp vader-pre-push.sh <GITREPO>/.git/hooks/pre-push
#          chmod +x <GITREPO>/.git/hooks/pre-push
# Prints the following whenever a force push is attempted
#  _________________________________
# |:::::::::::::;;::::::::::::::::::|
# |:::::::::::'~||~~~``:::::::::::::|
# |::::::::'   .':     o`:::::::::::|
# |:::::::' oo | |o  o    ::::::::::|
# |::::::: 8  .'.'    8 o  :::::::::|
# |::::::: 8  | |     8    :::::::::|
# |::::::: _._| |_,...8    :::::::::|
# |::::::'~--.   .--. `.   `::::::::|
# |:::::'     =8     ~  \ o ::::::::|
# |::::'       8._ 88.   \ o::::::::|
# |:::'   __. ,.ooo~~.    \ o`::::::|
# |:::   . -. 88`78o/:     \  `:::::|
# |::'     /. o o \ ::      \88`::::|
# |:;     o|| 8 8 |d.        `8 `:::|
# |:.       - ^ ^ -'           `-`::|
# |::.                          .:::|
# |:::::.....           ::'     ``::|
# |_________________________________|
#
# The force (push) is strong with this one...


push_command=$(ps -ocommand= -p $PPID)
is_force='force|\-f'

if [[ $push_command =~ $is_force ]]
then
    echo "ICAgICBfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18NCiAgICB8Ojo6Ojo6Ojo6Ojo6Ojs7Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6fA0KICAgIHw6Ojo6Ojo6Ojo6Oid+fHx+fn5gYDo6Ojo6Ojo6Ojo6Ojp8DQogICAgfDo6Ojo6Ojo6JyAgIC4nOiAgICAgb2A6Ojo6Ojo6Ojo6OnwNCiAgICB8Ojo6Ojo6Oicgb28gfCB8byAgbyAgICA6Ojo6Ojo6Ojo6fA0KICAgIHw6Ojo6Ojo6IDggIC4nLicgICAgOCBvICA6Ojo6Ojo6Ojp8DQogICAgfDo6Ojo6OjogOCAgfCB8ICAgICA4ICAgIDo6Ojo6Ojo6OnwNCiAgICB8Ojo6Ojo6OiBfLl98IHxfLC4uLjggICAgOjo6Ojo6Ojo6fA0KICAgIHw6Ojo6Ojonfi0tLiAgIC4tLS4gYC4gICBgOjo6Ojo6Ojp8DQogICAgfDo6Ojo6JyAgICAgPTggICAgIH4gIFwgbyA6Ojo6Ojo6OnwNCiAgICB8Ojo6OicgICAgICAgOC5fIDg4LiAgIFwgbzo6Ojo6Ojo6fA0KICAgIHw6OjonICAgX18uICwub29vfn4uICAgIFwgb2A6Ojo6Ojp8DQogICAgfDo6OiAgIC4gLS4gODhgNzhvLzogICAgIFwgIGA6Ojo6OnwNCiAgICB8OjonICAgICAvLiBvIG8gXCA6OiAgICAgIFw4OGA6Ojo6fA0KICAgIHw6OyAgICAgb3x8IDggOCB8ZC4gICAgICAgIGA4IGA6Ojp8DQogICAgfDouICAgICAgIC0gXiBeIC0nICAgICAgICAgICBgLWA6OnwNCiAgICB8OjouICAgICAgICAgICAgICAgICAgICAgICAgICAuOjo6fA0KICAgIHw6Ojo6Oi4uLi4uICAgICAgICAgICA6OicgICAgIGBgOjp8DQogICAgfF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX3wNCg0KICAgIFRoZSBmb3JjZSAocHVzaCkgaXMgc3Ryb25nIHdpdGggdGhpcyBvbmUuLi4NCg==" | base64 -d
    echo ""
    echo ""
fi

exit 0
