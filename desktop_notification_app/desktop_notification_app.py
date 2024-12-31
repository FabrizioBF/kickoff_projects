import time
from plyer import notification

if __name__ == "__main__":
    interval = int(input("Insira o intervalo em segundos: "))
    try:
        while True:
            notification.notify(
                title="ALERTA!!!",
                message="Faça uma pausa!",
                timeout=5)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")
