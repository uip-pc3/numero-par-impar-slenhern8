
def par_impar(n):
    """
        Par Impar
        Admite un numero y evalua si es par 
        Parameters
        -----------
        n : int
            Numero a evaluar
        Returns
        -------
        bool
            Resultado de evaluar si es par el numero  
        """
    if n%2 == 0 :
        return True
    else:
        return False

if __name__ == "__main__":
    flag = True
    while flag:
        try:
            n = int(input("Numero: "))
            flag = False
        except ValueError:
            print("Buen intento prof. Eso no es un numero")
        except:
            print("Error")
    if par_impar(n):
        print("Es par")
    else:
        print("No es par")
