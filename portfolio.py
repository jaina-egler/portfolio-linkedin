# Importando bibliotecas necessárias
import streamlit as st

# Adicionando uma sidebar
st.sidebar.title("Menu")

# Hiperlinks para as diferentes seções
home_link = st.sidebar.markdown("[🏠 Página Inicial](#pagina-inicial)")
power_bi_link = st.sidebar.markdown("[📊 Power BI Dashboards](#power-bi-dashboards)")
looker_link = st.sidebar.markdown("[📊 Looker Studio Dashboards](#looker-studio-dashboards)")
sobre_link = st.sidebar.markdown("[💬 Sobre mim](#sobre_link)")

# Ancoras para cada seção
st.markdown("<a name='pagina-inicial'></a>", unsafe_allow_html=True)
st.title("Portfólio de Dashboards - Página Inicial")

# Descrição do site
st.write(
    "Olá! Bem-vindo ao meu portfólio de dashboards! Aqui você encontrará visualizações interativas "
    "criadas usando diversas ferramentas, incluindo Power BI e Looker Studio. Esse portfólio está em constante atualização e utiliza dados fictícios."
)


# Ancoras para cada seção

st.markdown("<a name='power-bi-dashboards'></a>", unsafe_allow_html=True)
st.header("Power BI Dashboards")

# Descrição do Power BI
st.write(
    "Conheça alguns dashboards que criei usando o Power BI."
)
st.write(
    "Dash de vendas simples "
)
# Link para o dashboard Power BI 1
power_bi_iframe2 = """
<iframe title="Report Section" width="700" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNTk3ZjhlZDAtOWNjNC00YmIxLWJmOTQtNTU0MmRmMmI0ZTUxIiwidCI6IjcxZWZhMzRkLWE5MjEtNDMwMC05ZDgxLWNjNmVjOWJlMTdhNCJ9" frameborder="0" allowFullScreen="true"></iframe>
"""

# Exibindo o iframe no Streamlit
st.components.v1.html(power_bi_iframe2, height=500)
st.write(
    "Dash de vendas de conteúdo digital "
)
# Link para o dashboard Power BI 1
power_bi_iframe = """
<iframe title="DashVendasSimples" width="700" height="500" 
    src="https://app.powerbi.com/view?r=eyJrIjoiZTE0ZWQ1OTktOGQ3Mi00NTgwLWE5MjEtZjEyODU1ODhiNzZmIiwidCI6IjcxZWZhMzRkLWE5MjEtNDMwMC05ZDgxLWNjNmVjOWJlMTdhNCJ9" 
    frameborder="0" allowFullScreen="true">
</iframe>
"""

# Exibindo o iframe no Streamlit
st.components.v1.html(power_bi_iframe, height=500)

# Ancoras para cada seção
st.markdown("<a name='looker-studio-dashboards'></a>", unsafe_allow_html=True)
st.header("Looker Studio Dashboards")

# Descrição do Looker Studio
st.write(
    "Confira as visualizações de dados criadas usando Looker Studio. "
    "Os links abaixo levam aos dashboards correspondentes."
)
st.write(
    "Dash de análise de vídeos do Youtube "
)
# Link para o dashboard Looker Studio
looker_dashboard_url = "https://lookerstudio.google.com/embed/reporting/a280401c-9baf-4846-bebb-27cd706d4df8/page/VkMlD"

# Incorporando o iframe do Looker Studio
st.components.v1.iframe(looker_dashboard_url, width=800, height=500)

# Rodapé
st.write("Obrigado por explorar meu portfólio de dashboards!")


st.markdown("<a name='sobre_link'></a>", unsafe_allow_html=True)
st.title('Sobre mim')

st.markdown("""
   <table>
    <tr>
        <td><img style='border-radius: 50%;' src='https://media.licdn.com/dms/image/D4D03AQHaafOu1Glj6Q/profile-displayphoto-shrink_200_200/0/1676297546649?e=1709769600&v=beta&t=F0BKAsJHBNkH_19_g6tQcmLDp5nQBRF6miBhmSYXmwo' width='150'></td>
        <td>
            <h1 style="margin: 0;">Jaina Dady Egler Cardoso</h1>
            <p style="margin: 0;">Analista de Dados na Rocketship. Finalizando a graduação em análise e desenvolvimento de sistemas pelo IFRO (6/6). Experiência em extração de dados, integrações, e dashboards Power BI. </p>
            <hr>
            <p style="margin: 0;">📧 Meu Email: <a href="mailto:jainadadycardoso@gmail.com">jainadadycardoso@gmail.com</a></p>
            <p style="margin: 0;">👥 Meu LinkedIn: <a href="https://www.linkedin.com/in/jaina-dady/" target="_blank">in/jaina-dady</a></p>
        </td>
    </tr>
</table>

""", unsafe_allow_html=True)
