from operator import itemgetter
 
class Pupil:
    """Ученик"""
    def __init__(self, id, fio, average_score, clas_id):
        self.id = id
        self.fio = fio
        self.avr = average_score
        self.clas_id = clas_id
 
class Clas:
    """Номер класса"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class PupClass:
    """Соединение для связи многие ко многим"""
    def __init__(self, clas_id, pupil_id):
        self.clas_id = clas_id
        self.pupil_id = pupil_id

clases = [Clas(1, 'А1'),
    Clas(2, 'Б2'),
    Clas(3, 'В3'),   
    Clas(11, '1 класс (продленка)'),
    Clas(22, '2 класс (продленка)'),
    Clas(33, '3 класс (продленка)')]

pupils = [Pupil(1, 'Сиденко', 4.5, 1),
    Pupil(2, 'Волков', 3.75, 3),
    Pupil(3, 'Ананьев', 5.0, 2),
    Pupil(4, 'Варина', 4.33, 1),
    Pupil(5, 'Верешко', 4.69, 3)]


pupclases = [PupClass(1,1),
    PupClass(3,2),
    PupClass(2,3),
    PupClass(1,4),
    PupClass(3,5),
 
    PupClass(11,4),
    PupClass(22,1),
    PupClass(33,5),
    PupClass(22,3),
    PupClass(33,2)]
 
def main():
    one_to_many = [(pup.fio, pup.avr, cl.name) 
        for cl in clases 
        for pup in pupils 
        if pup.clas_id == cl.id]
    
    many_to_many_temp = [(cl.name, pupcl.clas_id, pupcl.pupil_id) 
        for cl in clases 
        for pupcl in pupclases 
        if cl.id == pupcl.clas_id]
    
    many_to_many = [(pup.fio, pup.avr, clas) 
        for clas, clas_id, pupil_id in many_to_many_temp
        for pup in pupils if pup.id == pupil_id]
 
    print('Задание Г1:')
    res_11 = [(cl.name, list(fio for fio, avr, name in one_to_many if name == cl.name))
              for cl in clases if cl.name[0] == 'А']
    print(res_11) 
    
    print('Задание Г2:')
    res_12_unsorted = []
    # Перебираем все классы
    for cl in clases:
        # Список учеников в данном классе
        clpupils = list(filter(lambda x: x[2] == cl.name, one_to_many))
        # Если есть хоть один ученик
        if len(clpupils) > 0:
            res_12_unsorted.append((cl.name, max(clpupils, key = lambda x: x[1])[1]))
 
    # Сортировка по среднему баллу
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse = True)
    print(res_12)
 
    print('Задание Г3:')
    res_13 = []
    # Выделяем по одному человеку в список
    for fio, avr, clas in many_to_many:
        res_13.append((fio, clas))
    # Сортируем список по первому ключу - названию класса
    res_13 = sorted(res_13, key = itemgetter(1))
    print(res_13)
 
if __name__ == '__main__':
    main()
