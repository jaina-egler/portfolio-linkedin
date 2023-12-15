# Importando bibliotecas necessárias
import streamlit as st

# Título do site
st.title("Portfólio de Dashboards")

# Descrição do site
st.write(
    "Olá! Bem-vindo ao meu portfólio de dashboards! Aqui você encontrará visualizações interativas "
    "criadas usando diversas ferramentas, incluindo Power BI e Looker Studio. Esse portfólio está em constante atualização e utiliza dados fictícios."
)

# Seção para o Power BI
st.header("Power BI Dashboards")

# Descrição do Power BI
st.write(
    "Conheça alguns dashs que criei usando o Power BI."
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


# Seção para o Looker Studio
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

