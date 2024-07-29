# Comparador de Bulas

Este projeto utiliza Streamlit para criar uma interface web que permite o upload de arquivos PDF, extrai o texto desses PDFs usando PyMuPDF, e compara as bulas utilizando a API do Google Generative AI.

## Requisitos

- Python 3.8 ou superior
- Streamlit
- PyMuPDF
- Google Generative AI

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/comparador-de-bulas.git
   cd comparador-de-bulas
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure a API Key do Google Generative AI no código:
   ```python
   genai.configure(api_key="SUA_API_KEY_AQUI")
   ```

## Uso

1. Execute o aplicativo Streamlit:
   ```sh
   streamlit run app.py
   ```

2. Na interface web, faça o upload de duas bulas no formato PDF.

3. O aplicativo irá:
   - Salvar os arquivos PDFs no diretório temporário.
   - Carregar os arquivos para a API do Google Generative AI.
   - Extrair o texto dos PDFs.
   - Comparar os textos das bulas e listar as diferenças importantes entre elas.

4. Você pode fazer perguntas sobre as bulas carregadas e o modelo responderá com base nos documentos.

## Manual do Usuário

### Iniciando o Aplicativo

1. **Abra o terminal** e navegue até o diretório onde o projeto foi clonado.
2. **Execute o comando** `streamlit run app.py` para iniciar o aplicativo.

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

### Configurações Avançadas

- **Configurações de Segurança:**
  O aplicativo está configurado para bloquear conteúdo potencialmente inadequado como assédio, discurso de ódio, conteúdo sexual e perigoso. Essas configurações podem ser ajustadas no código-fonte conforme necessário.

- **Configurações de Geração:**
  As configurações como `temperature`, `top_p`, `top_k` e `max_output_tokens` controlam o comportamento do modelo de geração de texto. Essas configurações podem ser ajustadas para modificar a resposta do modelo.

## Estrutura do Código

- `app.py`: Contém o código principal do aplicativo.
- `tempDir/`: Diretório temporário onde os arquivos PDF carregados são salvos.

## Funções Principais

- `save_uploaded_file(uploaded_file)`: Salva o arquivo PDF carregado no diretório temporário.
- `upload_to_gemini(file_path, mime_type=None)`: Faz o upload do arquivo PDF para a API do Google Generative AI.
- `wait_for_files_active(files)`: Espera até que os arquivos sejam processados pela API.
- `extract_text_from_pdf(file_path)`: Extrai o texto dos arquivos PDF.
- `main()`: Função principal que inicializa a interface e lida com as interações do usuário.


Desenvolvido por [Seu Nome](https://github.com/seu-usuario)
