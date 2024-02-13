% factorial program

fact(0, 1).
fact(1, 1).

fact(N, NFact) :-
    N > 1,
    NMinus1 is N - 1,
    fact(NMinus1, FactMinus1),
    NFact is N * FactMinus1.