from splinter import Browser
import winsound,time,os

url = "https://siteseguro.inatel.br/PortalAcademico/Matricula/Webmatricula.aspx"


tcurso = "ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$dropSubCurso"
tmatricula = "ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$tbMatricula"
tsenha = "ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$Password"
tentrar = "ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$LoginButton"

#Verificando vaga em NP 004 turma 'A'
materia = 12#materia de enteresse
nturma = 2 #turma de enteresse
curso = 2 #1-eletrica 2-computacao 3-telecomunicações 4-Biomedica 5-Automação
matricula = 0 
senha = ""

def logar():
    global browser,tcurso,tmatricula,tsenha,tentrar,curso,matricula,senha
    button = browser.find_by_name(tentrar)
    print 'Preenchendo dados'
    browser.find_by_name(tcurso).select(curso) #curso
    browser.find_by_name(tmatricula).fill(matricula)#matricula
    browser.find_by_name(tsenha).fill(senha)#senha
    button.click()
    print 'Clikando no input -Continuar-'

def tmat(n):
    n=n+1
    if n <10:
        tmat = "ctl00_Corpo_UCMatricula1_GridMatriculada_ctl0"+str(n)+"_imgAlterarTurma"
    else:
        tmat = "ctl00_Corpo_UCMatricula1_GridMatriculada_ctl"+str(n)+"_imgAlterarTurma"
    return tmat

def tturma(n):
    n=n+1
    if n <10:
        
        tturma =  "ctl00_Corpo_UCAlterarTurma1_GridTurma_ctl0"+str(n)+"_Label4"
    else:
        tturma =  "ctl00_Corpo_UCAlterarTurma1_GridTurma_ctl0"+str(n)+"_Label4"
    return tturma

if __name__ == '__main__':
    browser = Browser()
    browser.wait_time = 0.3 

    print 'Entrando no Portal Academico.'
    browser.visit(url)
    print 'Checando usuario..'

    while True:
        try:
            if browser.title.find("gina de Autentica")>0:
                print 'Usuario Deslogado..'
                logar()
                
            print 'Selecionando Materia..'
            buttonMat = browser.find_by_id(tmat(materia))
            buttonMat.click()
            print 'Checando Turma..'
            findturma = browser.find_by_id(tturma(nturma)).first
            if findturma.html.find("com vaga") !=-1:
                print 'Turma com vaga !!!'
                break
            else:
                print 'Turma sem vaga'
                print 'Esperando 30 segundos para verificar novamente!'
                time.sleep(30)
                os.system("cls")
                print '-------------------------------'
                print time.ctime()
                print ''
                browser.visit(url)
        except:
            pass
            

    for i in range(100):
        print 'TEM VAGA'
        winsound.Beep(1000,300)


