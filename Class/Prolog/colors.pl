different(red,green). different(red,blue). different(red,yellow).
different(green,red). different(green, blue). different(green, yellow).
different(blue,red). different(blue, green). different(blue, yellow).
different(yellow, red). different(yellow, green). different(yellow, blue).

coloring(One, Two, Three, Four, Five) :-
different(One, Two),
different(One, Three),
different(One, Four),
different(One, Five),
different(Two, One),
different(Two, Three),
different(Two, Four),
different(Three, One),
different(Three, Two),
different(Three, Four),
different(Four, One),
different(Four, Two),
different(Four, Three),
different(Four, Five),
different(Five, One),
different(Five, Four).
