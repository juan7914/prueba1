from datetime import datetime , timedelta

hora = datetime.now()
horaDos= hora + timedelta(hours=2)
print ("dentro de dos horas sera las: ",  horaDos.strftime('%d/%m/%Y  %H:%M:%S'))