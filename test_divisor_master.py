import divisor_master
import dirty_function


def test_simple():
    assert divisor_master.simple(2) == True
    assert divisor_master.simple(908) == False


def test_divisor():
    assert len(divisor_master.divisor(3)) == 2
    assert len(divisor_master.divisor(642)) != 2


def test_simple_divisor():
    assert divisor_master.simple_divisor(831) == [1, 3, 277]


def test_max_simple_div():
    assert divisor_master.max_simple_div(500) == 5


def test_canonical_decomposition():
    assert divisor_master.canonical_decomposition(420) == [2, 2, 3, 5, 7]


def test_max_div():
    assert divisor_master.max_div(854) == 427


name = ['Форрест', 'Джулс', 'Джон', 'Джеймс', 'Вито', 'Элен', 'Джек', 'Джеффри', 'Индиана',
        'Хан', 'Тайлер', 'Рик', 'Арагорн', 'Тони', 'Марти', 'Майкл', 'Феррис', 'Уолтер', 'Рокки']

# Тест на формирование списка заданной длины
def test_1_func():
    assert len(dirty_function.func(35, *name)) == 35

# Тест на случайность формирования списка, а не извлечение исходного по порядку
def test_2_func():
    assert len(dirty_function.func(19, *name)) != ['Форрест', 'Джулс', 'Джон', 'Джеймс', 'Вито', 'Элен', 'Джек',
                                                   'Джеффри', 'Индиана', 'Хан', 'Тайлер', 'Рик', 'Арагорн', 'Тони',
                                                   'Марти', 'Майкл', 'Феррис', 'Уолтер', 'Рокки']