def end(trouver, essai_rate, mot, loop) :
    if trouver == True :
        print("Gagnéé !!!!!")
        loop=False
    
    if essai_rate == 1 :
        print(
        """                       
                               
                               
                               
                               
                               
                               
                               
                               
        _______________________""")
    elif essai_rate == 2 :
        print(
        """
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 3 :
        print(
        """
                    +---------
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 4 :
        print(
        """
                    +----------
                    ! /        
                    !/         
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    
    elif essai_rate == 5 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 6 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 7 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !         !
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 8 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !        /!
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 9 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 10 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!
                    !        / 
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 11 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!/
                    !        / 
                    !          
                    !          
                    !          
        ____________+__________""")

        print("perdu le mot était :", mot)
        loop = False
    return loop
