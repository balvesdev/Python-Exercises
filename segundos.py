segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos//86400
dias2 = dias * 86400
horas = (segundos-dias2)//3600
seg = segundos % 3600
minutos = seg//60
seg_final = seg % 60

print(dias, "dias, ", horas ,"horas,", minutos, "minutos e", seg_final, "segundos.")