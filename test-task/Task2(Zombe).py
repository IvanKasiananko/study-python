def battle(zombi,plant):
    strength_zombi=sum(zombi)
    strength_plant=sum(plant)
    zombi_win=0
    plant_win=0
    len_zombil=len(zombi)
    len_plant=len(plant)
    if len_zombil>len_plant:
        Razn=len_zombil-len_plant
        Max_zombi_plant=len_plant
        zombi_win=zombi_win+Razn
    else:
        Razn=len_plant-len_zombil
        Max_zombi_plant=len_zombil
        plant_win=plant_win+Razn

    for a in range(Max_zombi_plant):
        if zombi[a]>plant[a]:
            zombi_win=zombi_win+1
        elif plant[a]>zombi[a]:
            plant_win=plant_win+1
    if zombi_win>plant_win:
        f=False
    elif zombi_win==plant_win:
        if strength_zombi>strength_plant:
            f=False
        else:
            f=True
    else:
        f=True
    return f

zombi_team_list=[[1,3,5,7],[1,3,5,7],[1,3,5,7],[2,1,1,1]]
plant_team_list=[[2,4,6,8],[2,4],[2,4,0,8],[1,2,1,1]]
for i in range(4):
    win = battle(zombi_team_list[i], plant_team_list[i])
    print("Зомби", zombi_team_list[i], "Растения ",plant_team_list[i], "--->", win)



