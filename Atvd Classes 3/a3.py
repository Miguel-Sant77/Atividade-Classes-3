class Motor:
    def __init__(self, potencia, tipo, modelo="Modelo Padrão"):
        self._potencia = potencia
        self._tipo = tipo
        self._modelo = modelo

    def get_potencia(self):
        return self._potencia

    def get_tipo(self):
        return self._tipo

    def get_modelo(self):
        return self._modelo

    def set_potencia(self, potencia):
        self._potencia = potencia

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def descricao_motor(self):
        return f"Motor {self._modelo}: {self._potencia} HP, Tipo: {self._tipo}"


class Navio:
    def __init__(self, nome, ano, motor):
        self._nome = nome
        self._ano = ano
        self._motor = motor

    def get_nome(self):
        return self._nome

    def get_ano(self):
        return self._ano

    def get_motor(self):
        return self._motor

    def set_nome(self, nome):
        self._nome = nome

    def set_ano(self, ano):
        self._ano = ano

    def set_motor(self, motor):
        self._motor = motor

    def descricao_navio(self):
        return f"Navio {self._nome} {self._ano} com {self._motor.descricao_motor()}"

if __name__ == "__main__":



    motor1 = Motor(5000, "Diesel", "MD5000")
    motor2 = Motor(7500, "Nuclear")
    motor3 = Motor(3000, "Elétrico", "ME3000")

    navio1 = Navio("Titanic", 1912, motor1)
    navio2 = Navio("Enterprise", 2021, motor2)
    navio3 = Navio("Aurora", 2023, motor3)

    print("Descrição dos motores:")
    print(motor1.descricao_motor())
    print(motor2.descricao_motor())
    print(motor3.descricao_motor())

    print("\nDescrição dos navios:")
    print(navio1.descricao_navio())
    print(navio2.descricao_navio())
    print(navio3.descricao_navio())

    navio1.set_nome("RMS Titanic")
    print("\nNome do navio1 após alteração:")
    print(navio1.get_nome())

    motor1.set_potencia(5500)
    print("\nPotência do motor1 após alteração:")
    print(motor1.get_potencia())

