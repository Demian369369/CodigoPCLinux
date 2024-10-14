from machine import RTC
class tiempo:
    def __init__(self):
        (year, month, mday, weekday, hour, minute, second, milisecond)=RTC().datetime()                
        RTC().init((year, month, mday, weekday, hour-6, minute, second, milisecond))   

    def imprimeHora(self):
        tiempo_actual = "{:02d}:{:02d}:{:02d}".format(RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6])
        #$tiempo_actual = str(tiempo[3]) + ":" + str(tiempo[4]) + ":" + str(tiempo[5])
        return tiempo_actual
    def imprimeFecha(self):
        fecha = "{:02d}/{:02d}/{}".format(RTC().datetime()[2],RTC().datetime()[1],RTC().datetime()[0])
        #fecha = str(self.dia) + " | " + str(self.mes) + " | " + str(self.año)
        return fecha