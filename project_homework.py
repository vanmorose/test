from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float,
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Вывод сообщения"""
        return (
            f"Тип тренировки: {self.training_type}; "
            f"Длительность: {self.duration:.3f} ч.; "
            f"Дистанция: {self.distance:.3f} км; "
            f"Ср. скорость: {self.speed:.3f} км/ч; "
            f"Потрачено ккал: {self.calories:.3f}."
        )


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65  # длина шага
    M_IN_KM: int = 1000  # для перевода в километры

    def __init__(self, action: int, duration: float, weight: int) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1: int = 18
    coeff_calorie_2: int = 20
    M_IN_H: int = 60  # для перевода в часы

    def get_spent_calories(self) -> float:
        spent_calories = (
            (self.coeff_calorie_1 * self.get_mean_speed()
             - self.coeff_calorie_2)
            * self.weight
            / self.M_IN_KM
            * (self.duration * self.M_IN_H)
        )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    M_IN_H: int = 60  # для перевода в часы
    K_1: float = 0.035
    K_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: int,
                 height: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        spent_calories = (
            self.K_1 * self.weight
            + (self.get_mean_speed() ** 2 // self.height) * self.K_2
            * self.weight) * (self.duration * self.M_IN_H)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38

    def __init__(
        self,
        action: int,
        duration: float,
        weight: int,
        length_pool: int,
        count_pool: int,
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_data: Dict[str, type[Training]] = dict()
    if workout_type == "SWM":
        dict_data[workout_type] = Swimming
    if workout_type == "RUN":
        dict_data[workout_type] = Running
    if workout_type == "WLK":
        dict_data[workout_type] = SportsWalking
    return dict_data[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
