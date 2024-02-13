% Facts
is_in_class(toby, csc380).
is_in_class(bob, csc480).
is_in_class(toby, csc480).
is_in_class(alice, csc380).
is_in_class(john, math215).
is_in_class(gabe, csc380).
is_in_class(gabe, math320).

is_in_room(csc480, wsc100).
is_in_room(csc380, wsc238).
is_in_room(math320, wsc110).
is_in_room(math215, wsc135).

has_temperature(wsc100, 65).
has_temperature(wsc238, 92).
has_temperature(wsc110, 75).
has_temperature(wsc135, 68).

% Rule
is_hot(Person) :-
    is_in_class(Person, _),
    is_in_room(_, _),
    has_temperature(_, Temp),
        Temp > 80.
