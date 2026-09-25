START hilow_game

    PRINT "Welcome to the higher/lower game!"
    
    REPEAT
        PRINT "Enter the lower bound: "
        INPUT lower_bound
        PRINT "Enter the upper bound: "
        INPUT upper_bound
        
        IF lower_bound >= upper_bound THEN
            PRINT "Error: The lower bound must be less than the upper bound."
        ENDIF
    UNTIL lower_bound < upper_bound

    secret_number = GENERATE_RANDOM_INTEGER_BETWEEN(lower_bound, upper_bound)
    
    PRINT "Guess a number between " + lower_bound + " and " + upper_bound + ":"
    INPUT user_guess

    WHILE user_guess IS NOT EQUAL TO secret_number DO
        
        IF user_guess > secret_number THEN
            PRINT "Nope, too high."
        ELSE IF user_guess < secret_number THEN
            PRINT "Nope, too low."
        ENDIF
        
        PRINT "Guess another number:"
        INPUT user_guess
        
    ENDWHILE

    PRINT "You got it!"

END hilow_game
