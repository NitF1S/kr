try:
    def Dec(sch):
        def S():
            sch()
            S = ((v+v_0)*t)/2
            print(S)
        return S

    @Dec
    def sch():
            a = (v-v_0)/t
            print(a)
            return a


    v = int(input('v - '))
    v_0 = int(input('v_0 -'))
    t = int(input('t - '))
      
except ZeroDivisionError:
      print('t!=0')

except ValueError:
    print('Присутствует что-то кроме цифр')
        
print(sch())


