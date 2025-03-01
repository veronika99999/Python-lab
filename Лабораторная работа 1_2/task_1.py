from abc import ABC, abstractmethod
from typing import List, Union, Optional
class ElectronicDevice(ABC):
"""абстрактный базовый класс для электронных устройств.
    атрибуты:
        brand (str): марка устройства.
        model (str): модель устройства.
        power_consumption (int): потребляемая мощность в ваттах. должна быть положительным числом.
    raises:
        valueError: если `power_consumption` не является положительным числом."""

    def __init__(self, brand: str, model: str, power_consumption: int) -> None:
        """конструктор класса ElectronicDevice."""
        self.brand = brand
        self.model = model
        if power_consumption <= 0:
            raise ValueError("Power consumption must be a positive number.")
        self.power_consumption = power_consumption

    @abstractmethod
    def turn_on(self) -> None:
        """абстрактный метод для включения устройства."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """абстрактный метод для выключения устройства."""
        pass

    def get_power_consumption(self) -> int:
        """возвращает потребляемую мощность устройства.
        >>> device = ElectronicDevice("Brand", "Model", 50)
        Traceback (most recent call last):
          ...
        TypeError: Can't instantiate abstract class ElectronicDevice with abstract methods turn_off, turn_on """
        return self.power_consumption
class Display(ABC):
    """абстрактный базовый класс для дисплеев.
    атрибуты:
        resolution_x (int): разрешение по горизонтали. Должно быть положительным числом.
        resolution_y (int): разрешение по вертикали. Должно быть положительным числом.
        display_type (str): тип дисплея (LCD, LED, OLED и т.д.).
    raises:
        valueError: если `resolution_x` или `resolution_y` не являются положительными числами."""

    def __init__(self, resolution_x: int, resolution_y: int, display_type: str) -> None:
        """конструктор класса Display."""
        if resolution_x <= 0 or resolution_y <= 0:
            raise ValueError("Resolution must be a positive number.")
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.display_type = display_type

    @abstractmethod
    def adjust_brightness(self, brightness_level: int) -> None:
        """абстрактный метод для регулировки яркости дисплея.
           args:
            brightness_level (int): Уровень яркости (от 0 до 100)."""
        pass

    @abstractmethod
    def set_color_profile(self, profile_name: str) -> None:
        """абстрактный метод для установки цветового профиля.
           args:
            profile_name (str): название цветового профиля."""
        pass

    def get_resolution(self) -> tuple[int, int]:
        """возвращает разрешение дисплея в виде кортежа (resolution_x, resolution_y).
        >>> display = Display(1920, 1080, "LCD")
        Traceback (most recent call last):
          ...
        TypeError: Can't instantiate abstract class Display with abstract methods adjust_brightness, set_color_profile"""
        return (self.resolution_x, self.resolution_y)
class NetworkDevice(ABC):
    """абстрактный базовый класс для сетевых устройств.
    атрибуты:
        mac_address (str): MAC-адрес устройства.  должен соответствовать формату "XX:XX:XX:XX:XX:XX".
        ip_address (Optional[str]): IP-адрес устройства. может быть None, если IP не назначен.
        is_connected (bool): флаг, указывающий, подключено ли устройство к сети.
    raises:
        valueError: если `mac_address` не соответствует формату."""

    def __init__(self, mac_address: str, ip_address: Optional[str], is_connected: bool) -> None:
        """конструктор класса NetworkDevice."""
        import re
        if not re.match(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", mac_address):
            raise ValueError("Invalid MAC address format.")
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.is_connected = is_connected

    @abstractmethod
    def connect(self) -> None:
        """абстрактный метод для подключения к сети."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """абстрактный метод для отключения от сети."""
        pass

    def get_mac_address(self) -> str:
        """возвращает MAC-адрес устройства.
        >>> device = NetworkDevice("00:11:22:33:44:55", "192.168.1.1", True)
        Traceback (most recent call last):
          ...
        TypeError: Can't instantiate abstract class NetworkDevice with abstract methods connect, disconnect
        """
        return self.mac_address

if __name__ == "__main__":
    import doctest
    doctest.testmod()
