from models import Programador ,Habilidade, Programador_Habilidade


def insere_programador():
    programador= Programador(nome='Daniel',email= 'daniel@poppymidia.com.br')
    print(programador)
    programador.save()

def consulta_programador():
    programador= Programador.query.all()
    print(programador)

def altera_programador():
    programador = Programador.query.filter_by(nome='Daniel').first()
    programador.nome= 'Joaquim'
    programador.save()

def exclui_programdor():
    programador = Programador.query.filter_by(nome= 'Joaquim').first()
    programador.delete()


def inserir_habilidade():
    habilidade= Habilidade(nome="PHP")

    habilidade.save()
    print(habilidade)

def consultar_habilidade():
    habilidade = Habilidade.query.all()
    print(habilidade)

def alterar_habilidade():
    habilidade = Habilidade.query.filter_by(nome='Python').first()
    habilidade.nome = 'java script'
    habilidade.save()

def deletar_habilidade():
    habilidade = Habilidade.query.filter_by(nome= 'Python').first()
    habilidade.deletar()

if __name__ == '__main__':
    #insere_programador()
    #altera_programador()
    #exclui_programdor()
    #consulta_programador()
    #inserir_habilidade()
    #alterar_habilidade()
    deletar_habilidade()
    consultar_habilidade()