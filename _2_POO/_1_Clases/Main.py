class Auto:
    marca="Honda"#Esto es un atributo de la clase auto
    modelo=1000#atributo dde la clase auto
    placa="PHV-96-04"

if __name__ == '__main__':
    taxi=Auto()#esto es una instancia de la clase auto
    miauto=Auto()#otra instacnia de la clase auto

    print(taxi.placa)#se invoca uno de los atributos de de la clase auto
    miauto.placa="TCV-963-12"
    print(miauto.placa)