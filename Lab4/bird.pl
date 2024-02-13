% Predicates
hassize(bluebird, small).
hascovering(bird, feathers).
hascolor(bluebird, blue).
hasproperty(bird, flies).
isa(bluebird, bird).
isa(bird, vertebrate).

% Rule for isbird
isbird(Animal) :-
    isa(Animal, bird);
    hascovering(Animal, feathers),
    hasproperty(Animal, flies).