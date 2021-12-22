#!/usr/bin/env zsh
# 打印颜色

for i in {0..255}
  do
    print -Pn "%K{$i}  %k%F{$i}${(l:3::0:)i}%f "${${(M)$((i%6)):#3}:+$'\n'}
  done
