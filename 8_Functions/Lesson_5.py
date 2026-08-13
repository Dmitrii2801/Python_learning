# Получение отдельных байтов информации из MAC-адреса и ip-адреса
# Создать функцию, принимающую тип информации (MAC-адрес или ip-адрес). В зависимости от типа
# информации и разделителя между байтами адреса функция записывает отдельные байты информации в кортеж

def byte_count(type, address):
    match type:
        case 'MAC-адрес': separator='-';
        case 'ip-адрес': separator='.';
    byte_list = address.split(separator);
    return byte_list;

# Ввод типа адреса
address_type = input('Введите тип запрашиваемого адреса (MAC-адрес / ip-адрес): ');
address = input('Введите запрашиваемый адрес: ');

byte_tuple = tuple(byte_count(address_type, address)); # преобразование списка байтов в кортеж

print(f'Отдельные байты информации в {address_type}е: {byte_tuple}');