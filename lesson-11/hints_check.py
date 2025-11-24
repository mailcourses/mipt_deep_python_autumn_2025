from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import (
    Any,
    Generator,
    NewType,
    Protocol,
    runtime_checkable,
    TypeVar,
    TYPE_CHECKING,
)


type UserData = dict[str, str | int | None]
type OptUserData = UserData | None


@dataclass
class User:
   user_id: str
   name: str
   age: int

   def __bool__(self) -> bool:
       return not not self.user_id


@dataclass
class Student(User):
    pass


def fetch_user(user_id: str) -> UserData:
    return {
       "user_id": user_id,
       "name": "Steve",
       "age": 99,
    }


def get_user_data(user: User) -> OptUserData:
    if not user:
        return None

    data = fetch_user(user.user_id)

    return data


def run_user() -> None:
    user = User("123", "steve", 99)
    res: OptUserData = get_user_data(user)
    print(f"111: {res=} for {user=}")

    user = User("", "", 0)
    res = get_user_data(user)
    print(f"222: {res=} for {user=}")

    user = Student("456", "stud", 239)
    res = get_user_data(user)
    print(f"333: {res=} for {user=}")


Celcius = NewType("Celcius", float)
Fareng = NewType("Fareng", float)


def convert_celcius_to_fareng(temp: Celcius) -> Fareng:
    return Fareng(temp * 9 / 5 + 32)


def gen_celcius_temps(start: Celcius) -> Generator[Celcius, None, str]:
    # if False:
    #     yield start
    yield start
    yield Celcius(start + 7)
    yield Celcius(start + 10)

    return "finished"


# def get_max_temp(temps: tuple[Celcius, ...]) -> Celcius | None:

def get_max_temp(temps: Iterable[Celcius]) -> Celcius | None:
    if not temps:
        return None

    return max(temps)


def get_first_temp(temps: Sequence[Celcius]) -> Celcius | None:
    if not temps:
        return None

    return temps[0]


def run_temp() -> None:
    temp = Celcius(36.6)
    res: float = convert_celcius_to_fareng(temp)
    print(f"111: {res=} for {temp=}, {type(res)=}")

    temp = Celcius(-40)
    res = convert_celcius_to_fareng(temp)
    print(f"222: {res=} for {temp=}, {type(res)=}")

    temps: Iterable[Celcius] = [Celcius(-40), Celcius(5), Celcius(0)]
    max_temp = get_max_temp(temps)
    print(f"333: {max_temp=} for {temps=}")

    temps = []
    max_temp = get_max_temp(temps)
    print(f"444: {max_temp=} for {temps=}")

    temps = (Celcius(8), Celcius(5), Celcius(0))
    max_temp = get_max_temp(temps)
    print(f"555: {max_temp=} for {temps=}")

    temps = gen_celcius_temps(Celcius(25))
    max_temp = get_max_temp(temps)
    print(f"666: {max_temp=} for {temps=}")

    temps = [Celcius(-40), Celcius(5), Celcius(0)]
    first_temp = get_first_temp(temps)
    print(f"777: {first_temp=} for {temps=}")

    # temps = gen_celcius_temps(Celcius(25))
    # first_temp = get_first_temp(temps)
    # print(f"888: {first_temp=} for {temps=}")


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self: "T", other: "T") -> bool: ...
    def __gt__(self: "T", other: "T") -> bool: ...


T = TypeVar("T", bound=Comparable)


def get_max_temp_generic(temps: Iterable[T]) -> T | None:
    if not temps:
        return None

    return max(temps)


def get_first_temp_generic[V](temps: Sequence[V]) -> V | None:
    if not temps:
        return None

    return temps[0]


def run_generic() -> None:
    temps = [Celcius(-40), Celcius(5), Celcius(0)]
    max_temp = get_max_temp_generic(temps)
    print(f"111: {max_temp=} for Celcius {temps=}")

    fareng_temps = [Fareng(-40), Fareng(5), Fareng(0)]
    max_f_temp = get_max_temp_generic(fareng_temps)
    print(f"222: {max_f_temp=} for Farengs {fareng_temps=}")

    print(f"333: {isinstance(Celcius(-40), Comparable)=}, {isinstance('qwert', Comparable)=}")

    temps = [Celcius(-40), Celcius(5), Celcius(0)]
    first_temp = get_first_temp_generic(temps)
    print(f"444: {first_temp=} for Celcius {temps=}")

    fareng_temps = [Fareng(-40), Fareng(5), Fareng(0)]
    first_f_temp = get_first_temp_generic(fareng_temps)
    print(f"555: {first_f_temp=} for Farengs {fareng_temps=}")


@runtime_checkable
class Predictable(Protocol):
    def predict(self) -> float:
        pass


class RandomForest:
    def predict(self) -> float:
        return 0.95


class NoPredict:
    def no_predict(self) -> float:
        return 0.1


def calc_prediction(model: Predictable) -> float:
    # return model.predict()
    return 0.5


def run_protocol() -> None:
    model = RandomForest()
    score = calc_prediction(model)
    print(f"{score=}, {isinstance(model, Predictable)=}")

    model2 = NoPredict()
    print(f"{isinstance(model2, Predictable)=}")
    score = calc_prediction(model2)


if __name__ == "__main__":
    print(f"{TYPE_CHECKING=}")

    run_user()
    print()

    run_temp()
    print()

    run_generic()
    print()

    run_protocol()

    print("ok")
