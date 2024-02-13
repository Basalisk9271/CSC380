% sum_of_squares program

sumsquares(1, 1).

sumsquares(N, Result) :-
    N > 1,
    NMinus1 is N - 1,
    sumsquares(NMinus1, SumMinus1),
    Result is SumMinus1 + N * N.
