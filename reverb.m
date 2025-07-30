function y = reverb(x, room, mix)
    load('rooms.mat');

    if room == 1
        ya = conv(x, h1);
    elseif room == 2
        ya = conv(x, h2);
    elseif room == 3
        ya = conv(x, h3);
    else
        error('Room must be 1, 2, or 3.');
    end

    len = min(length(x), length(ya));
    y = mix * ya(1:len) + (1 - mix) * x(1:len);
end
