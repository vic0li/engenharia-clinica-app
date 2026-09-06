import streamlit as st

st.set_page_config(
    page_title="Guia Prático de Engenharia Clínica",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Guia Prático de Engenharia Clínica & Manutenção")
st.caption("Manual de Bolso, Diagnóstico e Roteiro de Estudos para Auxiliar de Engenharia Clínica")

# Sidebar - Navigation & Study Route
st.sidebar.header("📌 Navegação")
menu = st.sidebar.radio(
    "Selecione uma Seção:",
    ["🎯 Roteiro de Estudos & Metodologia", 
     "♨️ 1. Autoclave (Prioridade 1)",
     "📈 2. Eletrocardiógrafo - ECG (Prioridade 2)",
     "❄️ 3. Câmaras de Vacina & Fria (Prioridade 3)",
     "💨 4. Compressor Odonto/Hospitalar (Prioridade 4)",
     "🦷 5. Cadeira & Caneta Odontológica (Prioridade 5)",
     "🔊 6. Ultrassom Odontológico (Prioridade 6)",
     "🔍 7. Colposcópio (Prioridade 7)",
     "🚀 Guia de Publicação no GitHub / Streamlit Cloud"]
)

# ---------------------------------------------------------
# SECTION 0: ROTEIRO DE ESTUDOS
# ---------------------------------------------------------
if menu == "🎯 Roteiro de Estudos & Metodologia":
    st.header("🎯 Roteiro Prático de Estudos & Metodologia de Manutenção")
    
    st.markdown("""
    Bem-vindo ao seu novo cargo como **Auxiliar de Engenharia Clínica**! 
    Este aplicativo foi estruturado para ser seu **manual de campo rápido** e **roteiro de aprendizado**.
    
    ### 🔄 Metodologia Universal de Diagnóstico
    Em qualquer equipamento biomédico, siga sempre este fluxo lógico para resolver problemas sem "trocar peças às cegas":
    
    $$\text{Sintoma} \longrightarrow \text{Possíveis Causas} \longrightarrow \text{Testes de Isolamento} \longrightarrow \text{Correção/Ajuste} \longrightarrow \text{Validação de Segurança e Desempenho}$$
    
    ---
    ### 🗓️ Roteiro Priorizado de Estudos
    Suas prioridades foram organizadas com base no impacto clínico, complexidade técnica e demandas reais do seu dia a dia:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **1️⃣ Autoclave (Alta Prioridade)**
        - *Motivo:* Envolve elétrica, mecânica, fluido, temperatura e pressão. Alta criticidade de biossegurança.
        - *Seus Casos Práticos:* Ajuste de alinhamento de porta/anilhas e teste de termostato vs. resistência.
        
        **2️⃣ Eletrocardiógrafo - ECG (Alta Prioridade)**
        - *Motivo:* Excelente para dominar bioeletrônica, filtros, aterramento e interferências magnéticas.
        - *Seu Caso Prático:* Interferência de bancada metálica/transformadores ferrosos gerando artefatos de amplitude.
        
        **3️⃣ Câmaras Frias & Vacina**
        - *Motivo:* Refrigeração médica, termometria, controladores PID, calibração de sensores e redundância de energia.
        
        **4️⃣ Compressor Odontológico / Hospitalar**
        - *Motivo:* Base da pneumática médica (ar isento de óleo, secadores, pressostatos, válvulas de alívio).
        """)
    with col2:
        st.warning("""
        **5️⃣ Cadeira e Caneta Odontológica**
        - *Motivo:* Integração de pneumática, hidráulica, iluminação e micro-motores de alta/baixa rotação.
        
        **6️⃣ Ultrassom Odontológico (Cavitadores)**
        - *Motivo:* Piezoelectricidade, geradores de alta frequência e transdutores.
        
        **7️⃣ Colposcópio**
        - *Motivo:* Óptica médica, iluminação LED/halógena e alinhamento mecânico de braços pantográficos.
        """)

# ---------------------------------------------------------
# SECTION 1: AUTOCLAVE
# ---------------------------------------------------------
elif menu == "♨️ 1. Autoclave (Prioridade 1)":
    st.header("♨️ Ficha Técnica: Autoclave")
    
    tab1, tab2, tab3 = st.tabs(["📝 Ficha Técnica & Mecanismo", "🔧 Seus Casos Práticos & Correções", "🌳 Fluxograma de Diagnóstico"])
    
    with tab1:
        st.subheader("1. Finalidade")
        st.write("Esterilização de artigos críticos por meio de calor úmido sob alta pressão, eliminando todas as formas de vida microbiana (esporos, bactérias, vírus).")
        
        st.subheader("2. Princípio de Funcionamento")
        st.write("A água destilada é aquecida por uma resistência elétrica na câmara. O vapor gerado fica retido, elevando a pressão interna. A alta pressão permite que a água atinja temperaturas superiores a 100°C (geralmente 121°C a 134°C), desnaturando proteínas celulares.")
        
        st.subheader("3. Fluxo de Funcionamento")
        st.code("Entrada: Água destilada + Energia Elétrica ➔ Aquecimento/Pressurização ➔ Esterilização (Set Point) ➔ Despressurização ➔ Secagem ➔ Saída: Artigos Estéreis", language="text")
        
        st.subheader("4. Componentes Principais")
        st.table([
            {"Componente": "Câmara (Interna/Externa)", "Função": "Vaso de pressão em aço inox que comporta os artigos e suporta a pressão."},
            {"Componente": "Resistência Elétrica", "Função": "Converte energia elétrica em calor para vaporizar a água."},
            {"Componente": "Borracha/Gaxeta da Porta", "Função": "Vedação hermética entre a câmara e a porta."},
            {"Componente": "Termostato de Segurança", "Função": "Desliga a resistência em caso de sobreaquecimento (proteção térmica)."},
            {"Componente": "Válvula Solenóide", "Função": "Controla a entrada e saída de água/vapor na câmara."},
            {"Componente": "Pressostato / Transdutor", "Função": "Monitora a pressão interna para controle do ciclo e descarte de segurança."},
            {"Componente": "Válvula de Segurança Mecânica", "Função": "Abre mecanicamente se a pressão ultrapassar o limite máximo seguro."}
        ])
        
        st.subheader("5. Manutenção Preventiva")
        st.markdown("""
        - **Limpeza:** Limpeza diária da borracha de vedação e da câmara interna com sabão neutro e água destilada.
        - **Inspeção:** Verificar desgaste, ressecamento ou rasgos na borracha da porta.
        - **Testes:** Teste biológico semanal (esporos *Geobacillus stearothermophilus*) e Teste químico de penetração de vapor (Bowie-Dick / Classe 5 ou 6).
        - **Troca Preventiva:** Substituição da borracha de vedação a cada 6 meses a 1 ano.
        - **Calibração:** Calibração anual dos sensores de temperatura e manômetro de pressão.
        """)

    with tab2:
        st.subheader("🛠️ Solução de Problemas Reais do Seu Dia a Dia")
        
        st.markdown("### ⚠️ Problema 1: Vazamento na Porta Digitale (Sempre no mesmo lado)")
        st.error("**Sintoma:** Escape de vapor/água durante a pressurização, localizado constantemente em um lado específico da porta.")
        st.markdown("""
        **Análise Técnica:**
        - Quando o vazamento ocorre **sempre no mesmo lado**, a causa raramente é apenas a borracha gasta. Indica **desalinhamento estrutural do fecho**, empenamento do braço ou pressão desequilibrada nos pontos de fixação.
        
        **Passo a Passo de Correção (Metodologia Aplicada):**
        1. **Inspeção Inicial:** Verifique a borracha de vedação (limpeza e ressecamento).
        2. **Análise de Alinhamento:** Observe a folga da porta com a câmara antes do aperto.
        3. **Ajuste com Anilhas/Arruelas:** Utilize chave e martelo/ferramenta de ajuste para posicionar anilhas nos pontos de articulação/dobradiça desalinhados, corrigindo a geometria e equilibrando a pressão de fechamento.
        4. **Testes de Validação:** Executar ciclo de teste com câmara vazia até a máxima pressão de trabalho (ex: 2.1 bar) e verificar com sabão líquido/detector se há vazamento no local.
        """)
        
        st.markdown("---")
        st.markdown("### ⚠️ Problema 2: Autoclave não esquenta (Diagnóstico: Termostato vs. Resistência)")
        st.warning("**Sintoma:** A autoclave liga a IHM/painel, inicia o ciclo, mas a temperatura não sobe.")
        st.markdown("""
        **Passo a Passo do Teste Prático de Campo:**
        1. **Segurança Primeiro:** Desconecte o equipamento da rede elétrica.
        2. **Acesso aos Componentes:** Abra a carenagem da autoclave para acessar o termostato de segurança e a resistência.
        3. **Teste do Termostato de Segurança:**
           - O termostato possui dois terminais elétricos.
           - Com o multímetro em escala de continuidade (bip), meça os terminais. Se estiver **Aberto (sem bip)**, o termostato atuou ou queimou.
           - *Teste de Confirmação:* Fazer o jumper (unir temporariamente os dois fios com isolamento). Ligar o equipamento brevemente. Se voltar a aquecer ➔ **Solicitar novo Termostato de Segurança com urgência.**
        4. **Teste da Resistência (caso o termostato esteja normal/jumper não resolva):**
           - Com multímetro na escala de Resistência (Ω), meça os terminais da resistência.
           - *Leitura esperada:* Valor ôhmico baixo (ex: $10\Omega$ a $40\Omega$ dependendo da potência $P = V^2/R$).
           - *Resistência Queimada:* Leitura em $OL$ (circuito aberto) ou fuga para a massa/terra.
        """)

    with tab3:
        st.subheader("🌳 Fluxograma de Diagnóstico: Autoclave")
        st.markdown("""
        ```text
        [ Autoclave com Falha ]
                 │
                 ├──► Não liga? ──► Verificar tomada / fusível geral / chave L/D / fonte da placa
                 │
                 ├──► Não esquenta? 
                 │          │
                 │          ├──► Testar continuidade do Termostato ──(Sem bip)──► Trocar Termostato
                 │          │
                 │          └──► Testar resistência (Ω) ────────────(Aberto)─► Trocar Resistência
                 │
                 └──► Vazamento na Porta?
                            │
                            ├──► Borracha ressecada/rasgada? ──► Substituir borracha
                            │
                            └──► Vazamento de um só lado? ────► Alinhar porta / Inserir anilhas de ajuste
        ```
        """)

# ---------------------------------------------------------
# SECTION 2: ECG
# ---------------------------------------------------------
elif menu == "📈 2. Eletrocardiógrafo - ECG (Prioridade 2)":
    st.header("📈 Ficha Técnica: Eletrocardiógrafo (ECG)")
    
    tab1, tab2, tab3 = st.tabs(["📝 Ficha Técnica", "🔬 Interferências & Seu Caso Real", "🌳 Fluxograma de Diagnóstico"])
    
    with tab1:
        st.subheader("1. Finalidade")
        st.write("Captação, amplificação e registro gráfico dos sinais elétricos bioelétricos gerados pela despolarização e repolarização do tecido cardíaco.")
        
        st.subheader("2. Princípio de Funcionamento")
        st.write("Eletrodos de Ag/AgCl aplicados na pele captam microvoltagens ($0,5mV$ a $5mV$). Um amplificador de instrumentação com alto CMRR (Razão de Rejeição em Modo Comum) amplifica o sinal, enquanto filtros rejeitam ruídos de rede ($60 Hz$) e tremores musculares.")
        
        st.subheader("3. Fluxo de Funcionamento")
        st.code("Sinal Bioelétrico (Pele) ➔ Eletrodos/Cabo Paciente ➔ Amplificação & Filtro ➔ Processamento Digital ➔ Impressora Térmica / Display", language="text")
        
        st.subheader("4. Componentes Principais")
        st.table([
            {"Componente": "Cabo de Paciente (10 vias)", "Função": "Conduz os sinais dos eletrodos até o módulo de entrada do equipamento."},
            {"Componente": "Amplificador de Instrumentação", "Função": "Amplifica os sinais de milivolts mantendo altíssima impedância de entrada."},
            {"Componente": "Circuito de Perna Direita (RLD)", "Função": "Injeta um sinal em contrafase para cancelar ruído de modo comum (60Hz)."},
            {"Componente": "Bloco Isolador (Opto/Indutivo)", "Função": "Garante a isolação galvânica do paciente para segurança contra choques."},
            {"Componente": "Módulo de Impressão Térmica", "Função": "Registra o gráfico em papel milimetrado térmico."}
        ])
        
        st.subheader("5. Manutenção Preventiva")
        st.markdown("""
        - **Limpeza:** Higienização de eletrodos e cabos com álcool 70% ou detergente neutro (evitar dobrar os cabos).
        - **Inspeção:** Inspeção visual dos pinos do cabo de paciente, presilhas/pera e integridade dos isolamentos.
        - **Testes:** Verificação com Simulador de ECG (geração de ondas de $1mV$, $60 BPM$).
        - **Calibração:** Validação de amplitude ($10 mm = 1 mV$) e velocidade do papel ($25 mm/s$ ou $50 mm/s$).
        """)

    with tab2:
        st.subheader("🔬 Estudo de Caso Real: Interferência Magnética de Bancada")
        st.warning("**Caso Relatado:** Dois eletrocardiógrafos no mesmo ambiente sobre bancada metálica (ferro/alumínio). Um equipamento antigo começou a apresentar exames desregulados com alta amplitude e ruído excessivo.")
        
        st.markdown("""
        ### 🧠 Fundamentação Teórica: Indução Eletromagnética & Bancadas Metálicas
        
        1. **Transformadores e Núcleo Ferroso:**
           - Transformadores de fonte interna trabalham com fluxo magnético alternado. Em equipamentos mais antigos, o blindamento magnético do transformador (chapa de ferro/Aço Silício) ou dos indutores pode perder eficiência.
           - O fluxo magnético disperso induz correntes parasitas (*Foucault*) na bancada metálica condutora.
        
        2. **Acoplamento Indutivo:**
           - A bancada de ferro/alumínio passa a atuar como uma antena condutora ou como um caminho de retorno de malha de terra (*ground loop*), elevando a tensão em modo comum no chassi do equipamento e nos cabos de sinal.
           - Isso distorce o ponto de referência do amplificador diferencial, fazendo o sinal oscilar ou saturar a amplitude do ECG.
        
        3. **Solução Prática Confirmada:**
           - **Isolamento Físico:** Colocar uma placa de **material dielétrico/plástico (ex: acrílico, borracha espessa, MDF)** sob o equipamento. Isso interrompe o acoplamento capacitivo/indutivo direto entre o chassi/fonte e a superfície metálica da bancada.
           - **Conexão de Aterramento:** Garantir que o pino de terra da tomada seja de baixa resistência ($< 5 \Omega$) e que o terminal de equalização de potencial do chassi do ECG esteja aterrado.
        """)

    with tab3:
        st.subheader("🌳 Fluxograma de Diagnóstico: ECG")
        st.markdown("""
        ```text
        [ Ruído / Sinal Alterado no ECG ]
                 │
                 ├──► Ruído de 60Hz (Onda senoidal contínua)?
                 │          ├──► Checar Aterramento da tomada
                 │          ├──► Checar eletrodo solto ou gel seco
                 │          └──► Verificar se há bancada metálica induzindo ruído ──► Usar isolante plástico sob o ECG
                 │
                 ├──► Linha de base oscilando (Respiração/Movimento)?
                 │          └──► Orientar paciente / Limpar pele com álcool / Trocar eletrodos
                 │
                 └──► Sem sinal em alguma derivação?
                            └──► Testar continuidade da via específica do Cabo de Paciente com multímetro
        ```
        """)

# ---------------------------------------------------------
# SECTION 3: CAMARAS
# ---------------------------------------------------------
elif menu == "❄️ 3. Câmaras de Vacina & Fria (Prioridade 3)":
    st.header("❄️ Ficha Técnica: Câmara de Vacina & Câmara Fria")
    
    st.markdown("""
    ### 1. Finalidade
    Manter imunobiológicos, bolsas de sangue e reagentes em faixa estrita de temperatura (geralmente $+2^\circ C$ a $+8^\circ C$ para vacinas, com setpoint fixo em $+5^\circ C$).

    ### 2. Princípio de Funcionamento
    Compressão de gás refrigerante (Ciclo Rankine de Refrigeração): O compressor comprime o gás (ex: R134a), que libera calor no condensador. O fluido passa pelo tubo capilar/válvula de expansão, evapora no evaporador absorvendo calor da câmara interna, resfriando o ar.

    ### 3. Fluxo de Funcionamento
    `Termostato/Sensor lê T > Setpoint ➔ Liga Compressor/Evaporador ➔ Troca Térmica ➔ T atinge Setpoint ➔ Desliga Compressor`

    ### 4. Componentes Principais
    """)
    st.table([
        {"Componente": "Compressor Hermético", "Função": "Bomba o fluido refrigerante pelo sistema."},
        {"Componente": "Controlador PID / Microprocessado", "Função": "Módulo eletrônico que gerencia temperatura, degelo e alarmes."},
        {"Componente": "Sensores NTC / Pt100", "Função": "Mede a temperatura interna da câmara e da solução termométrica."},
        {"Componente": "Sistema de Bateria / No-Break", "Função": "Mantém o sistema de monitoramento/refrigeração ativo na falta de energia."}
    ])

    st.markdown("""
    ### 5. Manutenção Preventiva
    - **Limpeza:** Limpeza mensal do condensador (remoção de poeira nas aletas para evitar sobreaquecimento).
    - **Inspeção:** Teste de alarme de porta aberta e vedação das gaxetas magnéticas.
    - **Calibração:** Calibração anual dos sensores térmicos com termômetro padrão aferido pela Rede Brasileira de Calibração (RBC).

    ### 6. Principais Falhas & Ações
    """)
    st.table([
        {"Sintoma": "Temperatura subindo acima de 8°C", "Possíveis Causas": "Condensador sujo, fuga de gás refrigerante, porta mal vedada, compressor travado", "Teste/Ação": "Limpar aletas do condensador; testar corrente (A) do compressor; verificar gaxeta"},
        {"Sintoma": "Bloqueio de gelo no evaporador", "Possíveis Causas": "Falha no degelo automático, resistência de degelo queimada, sensor de degelo descalibrado", "Teste/Ação": "Testar continuidade da resistência de degelo; acionar degelo manual no controlador"},
        {"Sintoma": "Alarme sonoro constante", "Possíveis Causas": "Desvio de temperatura, porta aberta, falha na bateria do nobreak", "Teste/Ação": "Verificar histórico de temperatura e tensão da bateria interna"}
    ])

# ---------------------------------------------------------
# SECTION 4: COMPRESSOR
# ---------------------------------------------------------
elif menu == "💨 4. Compressor Odonto/Hospitalar (Prioridade 4)":
    st.header("💨 Ficha Técnica: Compressor Isento de Óleo")
    
    st.markdown("""
    ### 1. Finalidade
    Fornecer ar comprimido limpo, seco e **isento de óleo** para acionamento de instrumentos odontológicos (canetas, sugadores) e equipamentos pneumáticos hospitalares.

    ### 2. Princípio de Funcionamento
    Motores elétricos movimentam pistões com anéis de Teflon (autolubrificantes). O ar ambiente é aspirado, comprimido para dentro do reservatório (reservatório de pressão) até atingir a pressão máxima (ex: 8 bar / 115 psi), quando o pressostato desliga o motor.

    ### 3. Componentes Principais
    """)
    st.table([
        {"Componente": "Pressostato", "Função": "Liga/Desliga o motor com base na pressão do reservatório."},
        {"Componente": "Válvula de Retenção", "Função": "Impede que o ar do reservatório retorne para os cabeçotes do compressor."},
        {"Componente": "Válvula de Alívio (Despressurização)", "Função": "Alivia a pressão do cabeçote ao desligar para permitir partida sem carga."},
        {"Componente": "Filtro Coalescente & Secador", "Função": "Remove umidade, óleo condensado e partículas do ar comprimido."},
        {"Componente": "Purgador Manual / Automático", "Função": "Drena a água acumulada no fundo do reservatório."}
    ])

    st.markdown("""
    ### 4. Principais Falhas & Diagnóstico
    """)
    st.table([
        {"Sintoma": "Compressor não liga", "Possíveis Causas": "Pressostato desarmado, capacitor de partida queimado, protetor térmico atuado", "Teste/Ação": "Checar tensão nos contatos do pressostato; testar capacitância do capacitor de partida com capacímetro"},
        {"Sintoma": "Demora muito para encher o reservatório", "Possíveis Causas": "Filtro de ar de entrada entupido, anéis de Teflon do pistão gastos, vazamento no sistema", "Teste/Ação": "Verificar filtro de ar; aplicar água com sabão nas conexões para achar vazamentos"},
        {"Sintoma": "Motor 'zune' mas não consegue dar partida", "Possíveis Causas": "Válvula de retenção com vazamento (cabeçote pressurizado) ou capacitor defeituoso", "Teste/Ação": "Testar se há ar saindo pela válvula de alívio; substituir capacitor"}
    ])

# ---------------------------------------------------------
# SECTION 5: CADEIRA & CANETA ODONTO
# ---------------------------------------------------------
elif menu == "🦷 5. Cadeira & Caneta Odontológica (Prioridade 5)":
    st.header("🦷 Ficha Técnica: Cadeira & Canetas Odontológicas")
    
    st.markdown("""
    ### 🛠️ Cadeira Odontológica (Mocho / Equipo)
    - **Princípio:** Eletromecânica (motores fuso/rosca sem fim) ou Eletro-hidráulica (bomba hidráulica e pistões) comandada por placa microprocessada e pedais.
    - **Manutenção Preventiva:** Lubrificação dos fusos mecânicos, ajuste dos fins de curso elétricos e drenagem do filtro regulador de ar do equipo.
    - **Falha Comum:** Cadeira não sobe/desce. *Teste:* Checar chaves de fim de curso (podem estar travadas abertas) e fusíveis da placa de comando.

    ---
    ### ⚙️ Caneta de Alta Rotação (Turbina Extraflex)
    - **Princípio:** O ar comprimido (2,2 bar) incide nas pás de um microrrolamento de cerâmica, atingindo até $400.000 RPM$.
    - **Manutenção Preventiva:** Lubrificação diária com spray lubrificante antes de autoclavar!
    - **Falhas Comuns:**
      - *Broca caindo:* Desgaste do sistema Push-Button (trocar a pinça/rotor).
      - *Pouco spray de água:* Entupimento do microfiltro de água ou do orifício do spray (desentupir com agulha especial).
    """)

# ---------------------------------------------------------
# SECTION 6: ULTRASSOM ODONTO
# ---------------------------------------------------------
elif menu == "🔊 6. Ultrassom Odontológico (Prioridade 6)":
    st.header("🔊 Ficha Técnica: Ultrassom Odontológico (Cavitador)")
    
    st.markdown("""
    ### 1. Finalidade
    Remoção de tártaro e raspagem periodontal por vibração ultrassônica.

    ### 2. Princípio de Funcionamento
    A placa eletrônica gera um sinal elétrico de alta frequência ($25 kHz$ a $30 kHz$). Este sinal alimenta cerâmicas piezoelétricas na caneta de ultrassom, que se expandem e contraem rapidamente, fazendo a ponta (inserto) vibrar mecânicamente.

    ### 3. Falhas Comuns & Soluções
    """)
    st.table([
        {"Sintoma": "Sem vibração na ponta", "Possíveis Causas": "Inserto mal apertado, cabo da caneta interrompido, transdutor piezoelétrico trincado", "Teste/Ação": "Apertar o inserto com a chave torquímetros; testar continuidade do cabo; testar caneta reserva"},
        {"Sintoma": "Sem fluxo de água (esquentando a ponta)", "Possíveis Causas": "Válvula solenoide de água queimada/entupida, registro regulador fechado", "Teste/Ação": "Testar tensão (V) na bobina da solenoide de água ao acionar o pedal"}
    ])

# ---------------------------------------------------------
# SECTION 7: COLPOSCÓPIO
# ---------------------------------------------------------
elif menu == "🔍 7. Colposcópio (Prioridade 7)":
    st.header("🔍 Ficha Técnica: Colposcópio")
    
    st.markdown("""
    ### 1. Finalidade
    Exame visual ampliado do colo do útero e vagina sob iluminação focalizada.

    ### 2. Princípio de Funcionamento
    Sistema óptico estéreo binocular (semelhante a um microscópio cirúrgico) montado sobre braço articulado. Utiliza lentes de aumento variável e fonte de luz LED ou halógena com filtro verde (para realce de vasos sanguíneos).

    ### 3. Manutenção & Soluções Rápidas
    - **Lentes Sujas/Embaçadas:** Limpeza estrita com papel óptico e solução de álcool isopropílico/éter. Nunca usar pano comum para não riscar o tratamento anti-reflexo.
    - **Luz Piscando ou Desligada:** Verificar a fonte chaveada interna ou a lâmpada/LED e potenciômetro de ajuste de intensidade (reostato).
    - **Braço caindo sozinho:** Ajuste da tensão mecânica das molas/frenagem nos manípulos das articulações.
    """)

# ---------------------------------------------------------
# SECTION 8: GITHUB & STREAMLIT CLOUD GUIDE
# ---------------------------------------------------------
elif menu == "🚀 Guia de Publicação no GitHub / Streamlit Cloud":
    st.header("🚀 Como Colocar este App na Web Gratuitamente")
    
    st.markdown("""
    Siga estes passos simples para ter o seu aplicativo acessível pelo celular ou qualquer computador:

    ### Passo 1: Criar a Conta no GitHub
    1. Acesse [github.com](https://github.com) e crie uma conta gratuita.

    ### Passo 2: Criar um Repositório
    1. Clique no botão **"+"** no canto superior direito ➔ **New repository**.
    2. Nomeie o repositório como: `engenharia-clinica-app`.
    3. Deixe marcado como **Public**.
    4. Marque a opção **Add a README file** e clique em **Create repository**.

    ### Passo 3: Adicionar os Arquivos
    Dentro do seu repositório criado:
    1. Clique em **Add file** ➔ **Upload files**.
    2. Suba o arquivo `app.py` (o código deste sistema).
    3. Suba o arquivo `requirements.txt` contendo a linha:
       ```text
       streamlit
       ```
    4. Clique em **Commit changes**.

    ### Passo 4: Publicar no Streamlit Community Cloud
    1. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login com sua conta do GitHub.
    2. Clique em **New app**.
    3. Selecione seu repositório `engenharia-clinica-app`, a branch `main` e o arquivo principal `app.py`.
    4. Clique em **Deploy!**
    
    🎉 **Pronto!** Em menos de 2 minutos você terá um link público (ex: `https://seu-usuario-engenharia-clinica.streamlit.app`) para usar no seu dia a dia no hospital/clínica!
    """)
