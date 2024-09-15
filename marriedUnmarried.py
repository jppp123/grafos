def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                     
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                     
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                      
  
   # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                     
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]      
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences:list = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]        

        #caso solteira atribui o homem a mulher/::-1 depois deleta o homem
        if currentHusband is None:
            manSpouse[he] = she
            womanSpouse[she] = he
            del unmarriedMen[0]
        else:
            #mulher casada, verificar se ela aceita o novo homem ou prefere o atual
            #se o index do atual for menor que o index do novo homem, ela ficará com o atual, 
            #então atualizar as tentativas do novo homem
            if herPreferences.index(currentHusband) < herPreferences.index(he):
                nextManChoice[he] += 1
            else:
                #caso ela aceite, trocar as referencias do homem e da mulher
                #o ex fica sem esposa e entra na fila de unmarried
                manSpouse[he] = she
                womanSpouse[she] = he
                manSpouse[currentHusband] = None
                unmarriedMen.append(currentHusband)

    return manSpouse
  
# You might want to test your implementation on the following two tests:
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
