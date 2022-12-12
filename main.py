from Vehiculo.Vehiculo import Coche
import pickle


def main():
    f = open('D:\\Nico\\objetoAuto', 'rb')
    autito = pickle.load(f)
    f.close()
    print(autito)

    """
    auto1 = Coche(1234,4,4)
    print(auto1)
    print(auto1.arrancar())

    f = open('D:\\Nico\\objetoAuto', 'wb')
    pickle.dump(auto1, f)
    f.close()"""


if __name__ == "__main__":
    main()
