import streamlit as st

st.set_page_config(
    layout= 'wide',
    page_title= 'Camppo AI Solutions',
)

st.title('Camppo AI Solutions')
st.divider()
st.header('Olá, sejam bem vindos! Nessa página temos vídeos mostrando alguns exemplos de como funcionam nossos serviços para esclarecer possíveis dúvidas.')
st.divider()

abertura = 'https://www.youtube.com/watch?v=qMuGFPgxNDs'

apresentacao = 'https://youtu.be/_r7nqhNtezU'

analise1 = 'https://youtu.be/6ErIPit1YCA'

analise2 = 'https://youtu.be/4V1KrC4s0jU'

chatbot = 'https://youtu.be/Lk71ibkSfzo'

rag = 'https://youtu.be/hCjZKtfsm8s'

encerramento = 'https://youtu.be/yODbrXalNIM'

st.header('**Abertura**')
st.markdown('Breve apresentação:')
st.video(abertura)

st.divider()

st.header('**Dados do projeto**')
st.markdown('Aqui mostramos um exemplo de dados fornecidos pelo sistema utilizado pelo cliente para alimentar toda nossa análise de dados')
st.video(apresentacao)

st.divider()
st.header('**Análise de dados**')
st.markdown('Uma das bases de nosso projetos é fornecer uma análise de dados, utilizando as principais ferramentas de ciência de dados, para extrair da melhor forma insights valiosos que possam aumentar tanto o lucro quanto a produtividade das empresas')
col1,col2 = st.columns(2)
col1.video(analise1)
col2.video(analise2)

st.divider()

st.header('**Modelos de IA**')
st.markdown('Existem hoje várias ferramentas de inteligência artificial, a maioria delas aplicáveis à negócios, ou até mesmo projetos pessoais.')
st.markdown('Reconhecimento Facial, visão computacional, Traduções, Transcrições de reuniões, Pesquisa em banco de dados, Atendimento à usuários, ChatBots, Machine Learning, Tornando impossível listar ou exemplificar todos aqui.')
st.markdown('Nossa equipe possui conhecimentos e experiência com várias inteligências artificiais e buscamos trazer o que há de mais avançado para nossos projetos.')
st.markdown('Nesse vídeo mostramos um ChatBot que recria a interface do chatGPT:')
st.video(chatbot)

st.divider()

st.header('**Técnica de RAG**')
st.markdown('Modelos de LLM (Large Language models) como o chatGPT por exemplo, são treinados para dar respostas a partir de uma base de dados. Essa base de dados pode conter como por exemplo o censo demográfico de uma cidade à data em que o modelo foi criado. Isso acaba "desatualizando" os dados que o modelo possui conforme o tempo passa.')
st.image('files/noticia.png')
st.markdown('O chatGPT 4 como na notícia acima foi treinado em abril de 2023, isso pode fazer com que o modelo tenha respostas menos precisas se necessário a recorrer a dados que são atualizados anualmente por exemplo.')
st.markdown('A RAG fornece uma maneira de otimizar o resultado de um LLM (Large Language Model) com informações direcionadas sem modificar o próprio modelo subjacente;')
st.markdown('as informações direcionadas podem ser mais atualizadas do que o LLM, bem como serem específicas para uma determinada organização e setor.')
st.markdown('Isso significa que o sistema de IA generativa pode fornecer respostas mais contextualmente apropriadas às solicitações, bem como basear essas respostas em dados extremamente atuais.')
st.video(rag)

st.divider()
st.header('Encerramento')
st.markdown('Tentamos por meio dessa página trazer alguns exemplos práticos de como funciona um projeto e que das vezes é necessário começar pelos dados para finalmente chegar em uma inteligência artificial')
st.markdown('E tambem informar as pessoas de que hoje qualquer um pode recorrer a uma ferramenta de IA para aumentar a produtividade e os resultados. Obrigado pela atenção')
st.video(encerramento)
st.markdown('Informações e contato: (16)9940-2537')
