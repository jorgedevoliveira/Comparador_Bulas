import streamlit as st
import google.generativeai as genai
import time
import os
import fitz  # PyMuPDF

# Configurando a API Key do GEMINI AI
genai.configure(api_key="AIzaSyCk282dAS15LSTOU7GOjsmWOkoFhmMoUlI")

st.title("Comparador de Bulas :page_with_curl:")

# Funções definidas antes do uso
def save_uploaded_file(uploaded_file):
    # Salvar o arquivo no diretório temporário
    temp_path = os.path.join("tempDir", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return temp_path

def upload_to_gemini(file_path, mime_type=None):
    file = genai.upload_file(file_path, mime_type=mime_type)
    st.write(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def wait_for_files_active(files):
    st.write("Waiting for file processing...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            st.write(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    st.write("...all files ready")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# File upload
uploaded_files = st.file_uploader("Faça o upload de duas bulas (no formato PDF)", accept_multiple_files=True, key="file_uploader_1")

if uploaded_files:
    # Criar diretório temporário se não existir
    os.makedirs("tempDir", exist_ok=True)
    
    file_paths = [save_uploaded_file(file) for file in uploaded_files]
    files = [upload_to_gemini(path, mime_type="application/pdf") for path in file_paths]
    wait_for_files_active(files)
    
    # Extrair texto dos PDFs
    pdf_texts = [extract_text_from_pdf(path) for path in file_paths]

    # Define model and safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    system_instruction = "Responda no idioma pt-br, restrinja a busca de informações aos documentos carregados. Se a pergunta não for relacionada aos documentos, peça ao usuário para refazer a pergunta com base no conteúdo dos documentos."

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=system_instruction,
        safety_settings=safety_settings
    )

    # Inicialização da conversa
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        pdf_texts[0],
                        pdf_texts[1],
                        "Compare estas duas bulas e liste as diferenças importantes entre elas:",
                    ],
                }
            ]
        )
        
        # Enviar a mensagem inicial e armazenar a resposta
        with st.spinner("Processando a comparação inicial..."):
            response = st.session_state.chat.send_message("Compare estas duas bulas e liste as diferenças importantes entre elas:")
        st.session_state.messages = [{"role": "assistant", "content": response.text}]

    def main():
        st.markdown("Faça uma pergunta. :speech_balloon:")

        # Exibe as mensagens anteriores
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Entrada do usuário
        if prompt := st.chat_input("Digite sua pergunta:"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Responde à pergunta
            with st.spinner("Processando sua pergunta..."):
                response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)

    if __name__ == "__main__":
        main()