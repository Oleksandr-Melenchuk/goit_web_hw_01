from controller import  Controller
from objects import AddresBook
from view import ConsoleView


view = ConsoleView()
book = AddresBook.load_data()


def main():
    controller = Controller(view, book)
    controller.run()


if __name__  == '__main__':
    main()
    