import kivy
dxd=1
x=0
y=0
h="да"
while dxd==1:
    print("Первый уровень")
    from colorama import init
    from colorama import Fore, Back, Style
    init()
    text_menu=input('чтобы начать игру напишите - "старт"\nЧтобы завершить игру воспользуйтесь командой - "стоп"\n')
    comand1="старт"
    comand2="игра"
    comand3="назад"
    comand4="стоп"
    complete2="к1"
    complete3="к2"
    complete4="к3"
    if text_menu==complete2:
        dxd+=1
    if text_menu==complete3:
        dxd+=2
    if text_menu==complete4:
        dxd+=3
    if text_menu==comand1:
       dxd-=1
       print("ПЕРВЫЙ УРОВЕНЬ")
       while x<2 and y<2:
#органы
            import random
            random_number=random. randint(1, 2)
            user_number=input("введите число от 1 до 2: ")
        #скелет
            if user_number==comand4:
                dxd+=1
                break
            if user_number=="1" and random_number==1:
                x+=1
                print(f"Вы угадали!\n{random_number} ")
            elif not user_number=="1" and random_number==1:
                y+=1
                print(f"Вв не угадали!\nПравльное число {random_number}")
            elif user_number=="2" and random_number==2:
                x+=1
                print(f"Вы угадали! {random_number}")
            elif not user_number=="2" and random_number==2:
                y+=1
                print(f"Вы не угадали правильное число было {random_number}")
            if x==0 and y==2:
                y-=1
            if y==2 and x==1:
                print("Вы проиграли! вернуться в главное меню?\n(Да/Нет) ")
                game_over=input("")
                if game_over==h:
                        dxd+=1
                        y-=2
                        if x==1:
                            x-=1
                        break
            if x==2:
                
                dxd+=2
            if x==2:
                x-=2
            if y==1:
                y-=1
           
            
            
h="да"
while dxd==2:
    from colorama import init
    from colorama import Fore, Back, Style
    init()
    print("2 УРОВЕНЬ")
    text_menu=input('чтобы начать игру напишите - "старт"\nЧтобы завершить игру воспользуйтесь командой - "стоп"\nЧтобы вернуться в начало напишите" начало"\n')
    comand1="старт"
    comand2="игра"
    comand3="начало"
    comand4="стоп"
    if text_menu==comand3:
        dxd-=1
        print("пшол нах! Это дэмка. Имей совесть! ")
        break
    if text_menu==comand1:
        dxd=-2
        x=0
        y=0
        while x<2 and y<3:
            #огран
            import random
            random_number=random. randint(1, 3)
            user_number=input("введите число от 1 до 3: ")
        #скелет
            if user_number==comand4:
                dxd+=2
                break
            if user_number=="1" and random_number==1:
                x+=1
                print(f"Вы угадали!\n{random_number} ")
            elif not user_number=="1" and random_number==1:
                y+=1
                print(f"Вв не угадали!\nПравльное число {random_number}")
            elif user_number=="2" and random_number==2:
                x+=1
                print(f"Вы угадали! {random_number}")
            elif not user_number=="2" and random_number==2:
                y+=1
                print(f"Вы не угадали правильное число было {random_number}")
            elif user_number=="3" and random_number==3:
                x+=1
                print(f"Вы угадали! число 3")
            elif not user_number=="3" and random_number==3:
                y+=1
                print("Вы не угадали! Правильное число 3")
            
            if x==0 and y==2:
                y-=2
            if y==2 and x==1:
                print("Вы проиграли! вернуться в главное меню?\n(Да/Нет) ")
                game_over=input("")
                if game_over==h:
                        dxd+=2
                        y-=2
                        if x==1:
                            x-=1
                            break
            if x==2:
                
                dxd+=3
            
            
            
while dxd==3:
    print("Третий уровень")
    from colorama import init
    from colorama import Fore, Back, Style
    init()
    text_menu=input('чтобы начать игру напишите - "старт"\nЧтобы завершить игру воспользуйтесь командой - "стоп"\nЧтобы вернуться на предыдущий уровень используй команду "назад"\nЕсли хотите вернуться в начало используйте команду "начало"\n')
    comand1="старт"
    comand2="игра"
    comand3="назад"
    comand4="начало"
    comand5="стоп"
    x=0
    y=0
    h="да"
    if text_menu==comand3:
        dxd-=1
    if text_menu==comand4:
        dxd-=2
    if text_menu==comand1:
        while x<2 and y<5:
            dxd-=3
        #органы
            import random
            random_number=random. randint(1, 4)
            user_number=input("введите число от 1 до 4: ")
        #скелет
            if user_number==comand5:
                dxd+=3
                break
            if user_number=="1" and random_number==1:
                x+=1
                print(f"Вы угадали!\n{random_number} ")
            elif not user_number=="1" and random_number==1:
                y+=1
                print(f"Вв не угадали!\nПравльное число {random_number}")
            elif user_number=="2" and random_number==2:
                x+=1
                print(f"Вы угадали! {random_number}")
            elif not user_number=="2" and random_number==2:
                y+=1
                print(f"Вы не угадали правильное число было {random_number}")
            elif user_number=="3" and random_number==3:
                x+=1
                print(f"Вы угадали! число 3")
            elif not user_number=="3" and random_number==3:
                y+=1
                print("Вы не угадали! Правильное число 3")
            elif user_number=="4" and random_number==4:
                x+=1
                print("Правильно, число 4")
            elif not user_number=="4" and random_number==4:
                y+=1
                print("Вы не угадали! Правильное число 4")
                
                
            
            if x==0 and y==2:
                y-=1
            if y==2 and x==1:
                print("Вы проиграли! вернуться в главное меню?\n(Да/Нет) ")
                game_over=input("")
                if game_over==h:
                        dxd+=3
                        y-=2
                        if x==1:
                            x-=1
                        break
            if x==2:
                
                dxd+=4
                
            
while dxd==4:
    print("Четвертый уровень")
    from colorama import init
    from colorama import Fore, Back, Style
    init()
    text_menu=input('чтобы начать игру напишите - "старт"\nЧтобы завершить игру воспользуйтесь командой - "стоп"\nЧтобы перейти на предыдущий уровень есть команда "назад"\nЕсли хотите вернуться в начало то напишите "начало"\n')
    x=0
    y=0
    h="да"
    comand1="старт"
    comand2="игра"
    comand3="назад"
    comand4="начало"
    comand5="стоп"
    if text_menu==comand3:
        dxd-=1
    if text_menu==comand4:
        dxd-=3
    if text_menu==comand1:
            
        while x<1 and y<5:
            dxd-=4
            #органы
            import random
            random_number=random. randint(1, 5)
            user_number=input("введите число от 1 до 5: ")
        #скелет
            if user_number==comand5:
                dxd+=4
                break
            if user_number=="1" and random_number==1:
                x+=1
                print(f"Вы угадали!\n{random_number} ")
            elif not user_number=="1" and random_number==1:
                y+=1
                print(f"Вв не угадали!\nПравльное число {random_number}")
            elif user_number=="2" and random_number==2:
                x+=1
                print(f"Вы угадали! {random_number}")
            elif not user_number=="2" and random_number==2:
                y+=1
                print(f"Вы не угадали правильное число было {random_number}")
            elif user_number=="3" and random_number==3:
                x+=1
                print(f"Вы угадали! число 3")
            elif not user_number=="3" and random_number==3:
                y+=1
                print("Вы не угадали! Правильное число 3")
            elif user_number=="4" and random_number==4:
                x+=1
                print("Правильно, число 4")
            elif not user_number=="4" and random_number==4:
                y+=1
                print("Вы не угадали! Правильное число 4")
            elif user_number=="5" and random_number==5:
                x+=1
                print("Вы угадали! \nЧисло 5")
            elif not user_number=="5" and random_number==5:
                y+=1
                print("Вы не угадали, Загаданое число было 5")
            
            
            if y==5:
                print("Вы проиграли! вернуться в главное меню?\n(Да/Нет) ")
                game_over=input("")
                if game_over==h:
                        dxd+=4
                        y-=5
                        
                        break
            if x==1:
                print("Конец демо версии игры. Тут пока нет и 50℅ из всей задумки")
                