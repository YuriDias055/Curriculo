arquivo = open('curriculo.html', encoding='utf-8', mode='w')
def cabecalho():
    arquivo.write("<!DOCTYPE html>" + "\n" + "<html lang=\"pt-br\">" + "\n" + "<head>" + "\n" + "  <meta charset=\"UTF-8\">" + "\n" + 
    "  <title>" + "Curriculo" + "</title>" + "\n" + "  <link rel=\"stylesheet\" href=\"estilo.css\">" + "\n" + "</head>" + "\n" + "<body>" + "\n")
    nome = input("Digite o seu nome completo:")
    arquivo.write("<div class=\"cabecalho\">" + "\n" "  <h1>" + nome + "</h1>" + "\n")
    cargo = input("Digite sua posição atual na área:")
    arquivo.write("  <h2>" + cargo + "</h2>" + "\n" + "</div>" + "\n")
    

def lateral():
    
    arquivo.write("<div class=\"lateral\">" + "\n" + "  <img src=\"img/perfil.png\" alt=\"Imagem de perfil\">" + "\n")
    telefone = input("Digite o seu telefone de contato:")
    email = input("Digite o seu e-mail:")
    arquivo.write("  <h2>" + "Contato" + "</h2>" + "\n")
    arquivo.write("  <h3>" + "Telefone: " + "<br>" + telefone + "</h3>" + "\n")
    arquivo.write("  <h3>" + "E-mail: " + "<br>"  + email + "</h3>" + "\n")
    arquivo.write("  <h2>" + "Endereço" + "</h2>" + "\n")
    rua = input("Digite a sua rua:")
    bairro = input("Digite o seu bairro:")
    cidade = input("Digite a sua cidade:")
    num = input("Digite o número da sua casa:")
    arquivo.write("  <h3>" + "Rua: " + "<br>" + rua + "</h3>" + "\n")
    arquivo.write("  <h3>" + "Bairro: " + "<br>"  + bairro + "</h3>" + "\n")
    arquivo.write("  <h3>" + "Número: " + "<br>"  + num + "</h3>" + "\n")
    arquivo.write("  <h3>" + "Cidade: " + "<br>"  + cidade + "</h3>" + "\n" + "</div>" + "\n")
    
def central():
    arquivo.write("<div class=\"central\">" + "\n" + "  <h2>" + "Habilidades" + "</h2>" + "\n" + "  <ul>" + "\n")
    i = 1
    while i == 1:
        habilidades = input("Digite uma linguagem de programação em que você possui conhecimento:")
        arquivo.write("    <li>" + habilidades + "</li>" + "\n")
        i = int(input("Digite 1 para digitar mais ou 0 para sair:"))
    arquivo.write("  </ul>" + "\n")

def central2():
    arquivo.write("  <h2>" + "Línguas estrangeiras" + "</h2>" + "\n" + "  <ul>" + "\n")
    b = 1
    while b == 1:
        linguas = input("Caso você possua conhecimento com alguma língua estrangeira, digite a mesma:")
        arquivo.write("    <li>" + linguas + "</li>" + "\n")
        b = int(input("Digite 1 para digitar mais ou 0 para sair:"))
    arquivo.write("  </ul>" + "\n" + "</div>")

def formacao():
    arquivo.write("<div class=\"formacao\">" + "\n" + "  <h2>" + "Formação" + "</h2>" + "\n")
    c = 1
    while c == 1:
        formacao = input("Digite primeiro o instituto de ensino:")
        curso = input("Agora digite a formação:")
        arquivo.write("  <h3> -" + formacao + "</h3>" + "\n" + "  <ul>" + "\n")
        arquivo.write("    <li>" + curso + "</li>" + "\n" + "  </ul>")
        c = int(input("Digite 1 para digitar mais ou 0 para sair:"))
    arquivo.write("</div>" + "\n")
          

cabecalho()
lateral()
central()
central2()
formacao()