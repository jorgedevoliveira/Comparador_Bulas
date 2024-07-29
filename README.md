# Comparador de Bulas

Este projeto utiliza Streamlit para criar uma interface web que permite o upload de arquivos PDF, extrai o texto desses PDFs usando PyMuPDF, e compara as bulas utilizando a API do Google Generative AI.

1. Na interface web, faça o upload de duas bulas no formato PDF.

2. O aplicativo irá:
   - Salvar os arquivos PDFs no diretório temporário.
   - Carregar os arquivos para a API do Google Generative AI.
   - Extrair o texto dos PDFs.
   - Comparar os textos das bulas e listar as diferenças importantes entre elas.

3. Você pode fazer perguntas sobre as bulas carregadas e o modelo responderá com base nos documentos.

## Manual do Usuário

### Iniciando o Aplicativo

Acesse através do seguinte link:

[Comparador de Bulas](https://comparadordebulas.streamlit.app/)


### Carregando as Bulas

1. Na interface web do aplicativo, **clique em "Browse files"** para selecionar e fazer o upload de duas bulas em formato PDF.
2. Aguarde até que os arquivos sejam carregados e processados. Você verá mensagens de status indicando o progresso.

### Comparando as Bulas

1. Após o processamento, o aplicativo exibirá uma comparação inicial das bulas carregadas.
2. **Faça perguntas** sobre as bulas no campo de entrada fornecido na interface. Por exemplo, você pode perguntar:
   - "Quais são as principais diferenças entre as duas bulas?"
   - "A bula A menciona algum efeito colateral específico?"
3. **Veja as respostas** geradas pelo modelo na área de chat abaixo do campo de entrada.

### Perguntas e Respostas

- **Pergunta:** "Posso carregar mais de dois PDFs?"
  **Resposta:** Atualmente, o aplicativo suporta apenas o upload de dois PDFs por vez para comparação.

- **Pergunta:** "O que acontece se eu carregar arquivos que não são PDFs?"
  **Resposta:** O aplicativo só aceita arquivos em formato PDF. Outros tipos de arquivos não serão processados.

- **Pergunta:** "Como faço para reiniciar a comparação?"
  **Resposta:** Para reiniciar, você pode simplesmente recarregar a página do aplicativo e fazer o upload de novos arquivos PDF.
