N=int(input())

hora=int(N//3600)
minuto=int((N-(hora*3600))/60)
segundos=int((N-(hora*3600)-(minuto*60)))



print(f"{hora}:{minuto}:{segundos}")