import difflib
import string


def LerTexto(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo: # lê o conteúdo do arquivo
        palavra = arquivo.read()    # aloca em palavra o conteudo lido em caminho                   
        return palavra 


def LimparTexto(texto):
    texto = texto.lower() # deixa os caracteres todos minusculos
    texto = texto.translate(str.maketrans('', '', string.punctuation)) # remove pontuações
    return texto
    

def similaridadeTextos (textoUm, textoDois): # aqui comparamos a similaridade dos textos para ves se esta igual
     return difflib.SequenceMatcher(None, textoUm, textoDois).ratio()
     
     
def NovaPalavra(texto):
    
    stopwords = ['a', 'à', 'ao', 'aos', 'as', 'às', 'com', 'como', 'da', 'das', 'de', 'do', 'dos',
    'e', 'em', 'entre', 'esse', 'essa', 'isso', 'isto', 'ele', 'ela', 'eles', 'elas',
    'foi', 'para', 'por', 'que', 'se', 'sem', 'sendo', 'ser', 'sua', 'suas', 'tem',
    'tendo', 'ter', 'teu', 'teus', 'tua', 'tuas', 'um', 'uma', 'umas', 'uns', 'o', 'os',
    'na', 'nas', 'no', 'nos', 'eu', 'você', 'vocês', 'me', 'minha', 'meu', 'nós', 'nosso',
    'nossos', 'nossa', 'nossas', 'já', 'não', 'sim']

    palavra = texto.split()
    Nova = []

    for x in palavra:
        if x not in stopwords:
            Nova.append(x)
 
    return ' '.join(Nova) # transforma a lista, em uma só string.


textoUm = LerTexto('texto1.txt')
textoDois = LerTexto('texto2.txt')

textoUm = LimparTexto(textoUm)
textoDois = LimparTexto(textoDois)

textoUm = NovaPalavra(textoUm)
textoDois = NovaPalavra(textoDois)


similaridade = similaridadeTextos(textoUm, textoDois)
print(f"A similaridade dos textos apresentados é de: {similaridade:.2%}")







