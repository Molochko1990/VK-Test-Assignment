# update_registry.py

import winreg as reg
from reg_parser import extract_values_from_reg_file

class RegistryUpdater:
    def __init__(self, base_key, sub_key):
        self.base_key = base_key
        self.sub_key = sub_key

    def set_reg_value(self, value_name, value_data):
        try:
            # Открываем ключ реестра или создаем его, если не существует
            key = reg.CreateKeyEx(self.base_key, self.sub_key, 0, reg.KEY_WRITE)

            # Устанавливаем значение для заданного ключа
            reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value_data)

            # Закрываем ключ
            reg.CloseKey(key)
            print(f"{value_name} успешно добавлен/обновлен.")
        except Exception as e:
            print(f"Ошибка при добавлении/обновлении {value_name}: {e}")

    def update_registry(self, values):
        for value_name, value_data in values.items():
            self.set_reg_value(value_name, value_data)


# Путь к файлу .reg и другие параметры
file_path = 'path_to_your_file.reg'  # Замени на реальный путь к твоему файлу
base_key = reg.HKEY_CURRENT_USER
sub_key = r"SOFTWARE\Gaggle Studios INC\Goose Goose Duck"

# Извлекаем значения из файла .reg
values = extract_values_from_reg_file(file_path)

# Создаем экземпляр класса и обновляем реестр
updater = RegistryUpdater(base_key, sub_key)
updater.update_registry(values)
