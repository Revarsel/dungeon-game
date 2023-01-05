class weapon:
    class ray_gun:
        name = "ray_gun"
        reload = 0.8
        damage = 100

    class sword:
        name = "sword"
        reload = 0.6
        damage = 50

    class pistol:
        name = "pistol"
        reload = 0.2
        damage = 10

    class hand:
        name = "hand"
        reload = 1
        damage= 20

weapon_list = [weapon.ray_gun(), weapon.sword(), weapon.pistol(), weapon.hand()]