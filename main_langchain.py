from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

num = input("Digite um número: ")
letra = input("Digite uma letra: ").lower()
tentativas = 1

modelo = "gpt-4o-mini"

def valida_palavra(palavra, numero, letra):
  if len(palavra) == int(numero) and palavra.lower().startswith(letra):
    return True
  else:
    return False

template_incial = PromptTemplate.from_template(
  "Digite uma palavra que tenha {numero} de letras, que comece com a letra {letra}. só a palvra e mais nada."
)
template_correcao = PromptTemplate.from_template(
  "A palavra {palavra} não possui {numero} letras. Escolha outra palavra que comece com {letra} e possui {numero} de letras. só a palvra e mais nada."
)

prompt = template_incial.format(numero=num, letra=letra)

llm = ChatOpenAI(
  model=modelo,
  temperature=0.7
)

resposta = llm.invoke(prompt)
palavra = resposta.content
resultado = valida_palavra(palavra, num, letra)
if resultado is False:
    while resultado is False:
      tentativas += 1
      prompt2 = template_correcao.format(palavra=palavra, numero=num, letra=letra)
      resposta = llm.invoke(prompt2)
      palavra = resposta.content
      resultado = valida_palavra(palavra, num, letra)
    print(f"{palavra} - {len(palavra)}\ntentativas: {tentativas}")
else:
    print(f"{palavra} - {len(palavra)}\ntentativas: {tentativas}")