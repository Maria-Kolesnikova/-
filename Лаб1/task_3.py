list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

summ = len(set(list_players))
num_team = summ / 2
team_1 = list_players[:int(num_team)]
#team_2 = set(list_players) - set(team_1)
team_2 = list_players[int(num_team):]
print(team_1)
print(team_2)