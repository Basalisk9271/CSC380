animal(dog)  :- is_true('has fur'), is_true('says woof').
animal(cat)  :- is_true('has fur'), is_true('says meow'), is_true('eats fish').
animal(giraffe)  :- is_true('has fur'), is_true('has long neck'), is_true('has spots').
animal(bear)  :- is_true('has fur'), is_true('is large'), is_true('eats fish'), is_true('hibernates').
animal(snake) :- is_true('Has scales'), is_true('hisses').
animal(duck) :- is_true('has feathers'), is_true('says quack').
animal(mouse) :- is_true('is small'), is_true('says squeak').

is_true(Q) :-
        format("~w?\n", [Q]),
        read(yes).
