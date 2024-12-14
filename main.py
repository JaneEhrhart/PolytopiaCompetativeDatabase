from logic import *
def main()->None:
    """
    Method handles starting and closing of aplication
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
   main()
