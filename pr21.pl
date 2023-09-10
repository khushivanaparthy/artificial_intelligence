hanoi(1, Source, _, Target, Moves) :-format('Move disk 1 from ~w to ~w~n', [Source, Target]),Moves = 1.

hanoi(N, Source, Auxiliary, Target, Moves) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Target, Auxiliary, Moves1),
    format('Move disk ~w from ~w to ~w~n', [N, Source, Target]),
    hanoi(M, Auxiliary, Source, Target, Moves2),
    Moves is Moves1 + 1 + Moves2.
solve_hanoi(Disks) :-
    hanoi(Disks, 'Source', 'Auxiliary', 'Target', Moves),
    format('Total moves: ~w~n', [Moves]).
