clc;
clear;

[x, fs] = audioread('guitar1.wav');
room = 1;
mix = 0.6;

y = reverb(x, room, mix);

sound(y, fs);
