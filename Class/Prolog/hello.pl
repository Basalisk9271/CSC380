windy.   /* Fact 1 */
likes(mickey, programming). /* Fact 2 */
likes(minnie, programming). /* Fact 3 */
likes(mickey, swimming).    /* Fact 4 */
likes(goofy, fishing).      /* Fact 5 */
human(socrates).            /* Fact 6 */
animated(mickey).           /* Fact 7 */
animated(minnie).           /* Fact 8 */
parent(mary, tom).          /* Fact 9 */
parent(mary, alice).        /* Fact 10 */
parent(john, tom).          /* Fact 11 */
parent(john, alice).        /* Fact 12 */

mortal(X) :- human(X).      /* Rule 1 */
friend(X, Y) :- likes(X, Z), likes(Y, Z), \+(X = Y).  /* Rule 2 */
