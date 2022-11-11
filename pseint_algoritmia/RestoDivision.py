unidades=int(input('dime las unidades a repartir '))
personas=int(input('dime las personas a repartir'))
if unidades % personas ==0:
    print('el reparto es ok, no sobra nada')
else:
    print('cuidado porque alguna unidad hay que partirla')