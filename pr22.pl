can_fly(sparrow).
can_fly(pigeon).
cannot_fly(penguin).

can_bird_fly(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

can_bird_fly(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).
