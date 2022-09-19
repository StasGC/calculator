from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_base_main():
    response = client.get("/")
    assert response.status_code == 200, "Тест на соединение не прошел"
    assert response.json() == "Hello world!", "Тест на соединение не прошел"


def test_math_addition_id_main():
    response = client.post(
        "/solver/",
        json={"expression": "5+3"}
    )
    assert response.status_code == 200, "Тест на сложение с проверкой id не прошел"
    assert response.json() == {
        "expression": "5+3=8",
        "id": response.json()["id"]
    }, "Тест на сложение с проверкой id не прошел"


def test_math_addition_1_main():
    response = client.post(
        "/solver/",
        json={"expression": "2+7"}
    )
    assert response.status_code == 200, "Тест на сложение положительных чисел не прошел"
    assert response.json()["expression"] == "2+7=9", "Тест на сложение положительных чисел не прошел"


def test_math_addition_2_main():
    response = client.post(
        "/solver/",
        json={"expression": "-2+(-7)"}
    )
    assert response.status_code == 200, "Тест на сложение положительных чисел не прошел"
    assert response.json()["expression"] == "-2+(-7)=-9", "Тест на сложение положительных чисел не прошел"


def test_math_difference_1_main():
    response = client.post(
        "/solver/",
        json={"expression": "10-5"}
    )
    assert response.status_code == 200, "Тест на положительную разность не прошел"
    assert response.json()["expression"] == "10-5=5", "Тест на положительную разность не прошел"


def test_math_difference_2_main():
    response = client.post(
        "/solver/",
        json={"expression": "3-7"}
    )
    assert response.status_code == 200, "Тест на отрицательную разность не прошел"
    assert response.json()["expression"] == "3-7=-4", "Тест на отрицаткльную разность не прошел"


def test_math_multiplication_1_main():
    response = client.post(
        "/solver/",
        json={"expression": "5*5"}
    )
    assert response.status_code == 200, "Тест на целочисленное умножение не прошел"
    assert response.json()["expression"] == "5*5=25", "Тест на целочисленное умножение не прошел"


def test_math_multiplication_2_main():
    response = client.post(
        "/solver/",
        json={"expression": "6.5*7.5"}
    )
    assert response.status_code == 200, "Тест на умножение с точкой не прошел"
    assert response.json()["expression"] == "6.5*7.5=48.75", "Тест на умножение с точкой не прошел"


def test_math_division_1_main():
    response = client.post(
        "/solver/",
        json={"expression": "10/5"}
    )
    assert response.status_code == 200, "Тест на целочисленное деление не прошел"
    assert response.json()["expression"] == "10/5=2.0", "Тест на целочисленное деление не прошел"


def test_math_division_2_main():
    response = client.post(
        "/solver/",
        json={"expression": "5/2"}
    )
    assert response.status_code == 200, "Тест на деление с плавующей точкой не прошел"
    assert response.json()["expression"] == "5/2=2.5", "Тест на деление с плаваующей точкей не прошел"


def test_math_division_zero_1_main():
    response = client.post(
        "/solver/",
        json={"expression": "10/0"}
    )
    assert response.status_code == 400, "Тест на целочисленное деление на ноль не прошел"
    assert response.json()["message"] == "10/0: Invalid expression. Error: division by zero", "Тест на " \
                                                                                              "целочисленное деление на ноль не прошел"


def test_math_division_zero_2_main():
    response = client.post(
        "/solver/",
        json={"expression": "5.0/0"}
    )
    assert response.status_code == 400, "Тест на деление с плавующей точкой на ноль не прошел"
    assert response.json()["message"] == "5.0/0: Invalid expression. Error: float division by zero", "Тест на " \
                                                                                                     "деление с плаваующей точкей на ноль не прошел"


def test_math_equality_main():
    response = client.post(
        "/solver/",
        json={"expression": "2"}
    )
    assert response.status_code == 200, "Тест на равенство не прошел"
    assert response.json()["expression"] == "2=2", "Тест равенство не прошел"


def test_math_equality_free_main():
    response = client.post(
        "/solver/",
        json={"expression": "="}
    )
    assert response.status_code == 400, "Тест на пустое равенство не прошел"
    assert response.json()["message"] == "=: Invalid expression. Error: unexpected EOF while parsing" \
                                         " (<string>, line 1)", "Тест на пустое равенство не прошел"


def test_history_main():
    response = client.get("/history/")
    assert response.status_code == 200, "Тест на соединение не прошел"
