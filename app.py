import streamlit as st
import pandas as pd
import graphviz

# ==========================================================
# ENGENHARIA CLÍNICA - GUIA DE CAMPO V3 (PROFUNDIDADE TÉCNICA)
# Arquitetura:
# FÍSICA APLICADA → COMPONENTES → DIAGRAMA INTERATIVO → SUBSISTEMAS 
# → MATRIZ DE FALHAS → ARVORE DE DECISÃO → TESTES & VALIDAÇÃO (60601-1)
# ==========================================================

st.set_page_config(
    page_title="Engenharia Clínica | Guia Técnico V3",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# ESTILO VISUAL E CUSTOM CSS
# ----------------------------------------------------------
st.markdown("""
<style>
    .metric-card {
        padding: 1.2rem;
        border-radius: 10px;
        background: #0e1117;
        border: 1px solid #262730;
        margin-bottom: 1rem;
    }
    .physics-box {
        padding: 1.2rem;
        border-left: 5px solid #00d4b1;
        background-color: #0e1e24;
        border-radius: 6px;
        margin: 1rem 0;
    }
    .component-card {
        padding: 1rem;
        border: 1px solid #363945;
        border-radius: 8px;
        background-color: #161b22;
        margin-bottom: 0.8rem;
    }
    .danger-box {
        padding: 1rem;
        border-left: 5px solid #ff4b4b;
        background-color: #2a1215;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# BASE DE DADOS TÉCNICA - ENGINE V3
# ==========================================================

EQUIPAMENTOS_V3 = {

    "♨️ Autoclave Hospitalar / Bancada": {
        "categoria": "Esterilização por Calor Úmido",
        "fisica_aplicada": """
        ### 1. Termodinâmica e Mudança de Fase (Equação de Clapeyron)
        A esterilização a vapor não se baseia apenas na elevação da temperatura, mas no **calor latente de vaporização** ($\Delta H_{vap}$). 
        Quando o vapor saturado entra em contato com uma carga mais fria, ele condensa instantaneamente, liberando cerca de $2260 \text{ kJ/kg}$ de energia (a $100^\circ\text{C}$), coagulando irreversivelmente as proteínas microbianas.

        $$\frac{dP}{dT} = \frac{\Delta H_{vap}}{T \Delta V}$$

        *   **Pressão vs. Temperatura:** A elevação da pressão na câmara (ex: $2.1 \text{ bar}$ absoluto ou $1.1 \text{ bar}$ relativo) é o meio físico utilizado para elevar o ponto de ebulição da água até $121^\circ\text{C}$ ou $134^\circ\text{C}$.
        *   **Lei de Dalton e Ar Residual:** A pressão total na câmara é a soma das pressões parciais do vapor e do ar residual ($P_{total} = P_{vapor} + P_{ar}$). Se houver ar aprisionado, a temperatura real será menor do que a indicada pelo manômetro (violação da tabela de vapor saturado).
        """,
        "subsistemas": {
            "Mecânico/Pressão": ["Câmara Interna (Inox 316L)", "Porta e Mecanismo de Trava", "Gaxeta de Vedação"],
            "Térmico/Hidráulico": ["Resistência de Imersão/Gerador de Vapor", "Válvulas Solenoides", "Purgador Termodinâmico", "Válvula de Segurança"],
            "Eletroeletrônico/Controle": ["Placa Controladora (PID)", "Sensor de Temperatura (PT100)", "Transdutor de Pressão"]
        },
        "componentes_detalhados": {
            "RESISTÊNCIA": {
                "o_que_e": "Elemento de aquecimento resistivo blindado em tubo de aço inoxidável ou cobre niquelado.",
                "como_funciona": "Converte energia elétrica em energia térmica por Efeito Joule ($P = R \cdot I^2$), transferindo calor por condução direta à água do reservatório/gerador.",
                "principio_fisico": "Efeito Joule e Condução Térmica.",
                "como_testar": "1. Com multímetro (desenergizado), medir resistência ôhmica ($\Omega$) nos terminais (comparar com $R = V^2/P$).\n2. Testar isolamento contra a carcaça/massa usando Megômetro ($500\text{V DC} > 100\text{ M}\Omega$).\n3. Medir corrente alternada com alicate amperímetro durante ciclo ativo.",
                "sintomas_falha": "O ciclo não atinge a temperatura; disjuntor DR/GFCI dispara imediatamente ao ligar; aquecimento extremamente lento.",
                "relacao_componentes": "Acionada diretamente por Relé de Estado Sólido (SSR) ou Contator trifásico, sob comando do microcontrolador mediante leitura do PT100."
            },
            "GAXETA / ANEL DE VEDAÇÃO": {
                "o_que_e": "Elemento elastomérico (silicone atóxico de alta performance ou EPDM) com perfil específico para vedação dinâmica/estática.",
                "como_funciona": "Sela a fresta entre a flange da câmara e a porta. A própria pressão interna da câmara expande os lábios da gaxeta, aumentando a força de vedação.",
                "principio_fisico": "Deformação elástica mecânica e Vedação por diferencial de pressão.",
                "como_testar": "1. Inspeção visual contra ressecamento, trincas, cortes ou incrustações de minerais.\n2. Verificação do coeficiente de dureza (Shore A) se disponível.\n3. Teste de estanqueidade pressurizando a câmara fria.",
                "sintomas_falha": "Vazamento visível de vapor na borda da porta; incapacidade de pressurização; ruído de silvo durante a fase de esterilização.",
                "relacao_componentes": "Trabalha diretamente na interface mecânica Porta-Câmara e depende do travamento correto dos fusos/trincos mecânicos."
            },
            "SENSOR PT100": {
                "o_que_e": "Termorresistência de Platina (RTD) de alta precisão com resistência nominal de $100\,\Omega$ a $0^\circ\text{C}$.",
                "como_funciona": "Sua resistência elétrica varia de forma altamente linear e previsível em função da variação de temperatura ($\approx 0.385\,\Omega/^\circ\text{C}$).",
                "principio_fisico": "Coeficiente de temperatura positivo de resistência (PTC).",
                "como_testar": "1. Medir resistência nos terminais com multímetro de precisão: a $25^\circ\text{C}$ deve indicar $\approx 109.73\,\Omega$; a $100^\circ\text{C}$, $\approx 138.5\,\Omega$.\n2. Validar desvio contra um calibrador de bloco seco (Dry Block) padrão.",
                "sintomas_falha": "Erro de leitura no IHM (ex: $-99^\circ\text{C}$ ou $999^\circ\text{C}$); cancelamento do ciclo por sobretemperatura/subtemperatura; falha na validação biológica.",
                "relacao_componentes": "Envia sinal milivolt/ôhmico para o conversor Analógico-Digital (ADC) da placa principal, instruindo o algoritmo de controle PID."
            },
            "VÁLVULA DE SEGURANÇA": {
                "o_que_e": "Dispositivo de alívio de pressão acionado por mola de ação rápida.",
                "como_funciona": "Quando a força exercida pela pressão interna excede a força pré-ajustada da mola ($F = P \cdot A$), a válvula abre instantaneamente, descarregando o vapor para a atmosfera.",
                "principio_fisico": "Equilíbrio de forças mecânicas (Pressão x Pressão Elastómerica/Mola).",
                "como_testar": "1. Acionamento manual da alavanca sob carga de pressão (se aplicável ao protocolo).\n2. Teste de bancada em bancada de aferição de válvulas para verificar a pressão exata de abertura e recalibração.",
                "sintomas_falha": "Válvula soprando abaixo da pressão nominal de trabalho; válvula travada que não abre em sobrepressão extrema.",
                "relacao_componentes": "Proteção mecânica final em paralelo com a câmara, independente do sistema eletrônico de controle."
            }
        },
        "diagrama_dot": """
        digraph Autoclave {
            graph [background=transparent, rankdir=LR];
            node [shape=box, style=filled, fillcolor="#1f2937", fontcolor="#ffffff", fontname="Helvetica"];
            edge [fontcolor="#ffffff", color="#4b5563"];

            Placa [label="Placa Controladora (PID)", fillcolor="#1e3a8a"];
            Resistencia [label="RESISTÊNCIA", fillcolor="#991b1b"];
            Camara [label="CÂMARA DE ESTERILIZAÇÃO", fillcolor="#374151"];
            PT100 [label="SENSOR PT100", fillcolor="#065f46"];
            Gaxeta [label="GAXETA / VEDAÇÃO", fillcolor="#d97706"];
            ValvulaSeg [label="VÁLVULA DE SEGURANÇA", fillcolor="#991b1b"];

            Placa -> Resistencia [label="Sinal PWM/SSR"];
            Resistencia -> Camara [label="Transferência Térmica"];
            Camara -> PT100 [label="Leitura de Temp."];
            PT100 -> Placa [label="Feedback R(T)"];
            Gaxeta -> Camara [label="Estanqueidade"];
            Camara -> ValvulaSeg [label="Alívio Mecânico"];
        }
        """,
        "matriz_falhas": [
            {
                "sintoma": "Ciclo aborta por tempo limite de subida de temperatura excedido.",
                "causa_raiz": "Resistência parcialmente queimada (elemento em aberto num circuito trifásico) ou incrustação calcária maciça impedindo a troca térmica.",
                "teste": "Medição de corrente trifásica com alicate amperímetro e inspeção visual da superfície das blindagens."
            },
            {
                "sintoma": "Pressão sobe no manômetro, mas a temperatura no display fica abaixo do gráfico de vapor saturado.",
                "causa_raiz": "Falha no expurgo de ar (Purgador termodinâmico ou válvula solenoide de purga travada fechada). Presença de ar na câmara.",
                "teste": "Verificar se a válvula de purga evacua ar frio nos primeiros 5 minutos de aquecimento."
            }
        ],
        "arvore_decisao": [
            "1. Início do Diagnóstico: O equipamento liga a IHM?",
            "   ├── NÃO ➔ Verificar Fusiveis de Entrada, Cabo de Força e Fonte Chaveada da Placa Principal.",
            "   └── SIM ➔ Selecionar Ciclo Padrão e Iniciar.",
            "       ├── Falha ocorre antes dos 100°C?",
            "       │   ├── SIM ➔ Testar Resistência (Continuidade) e SSR (Tensão de Saída).",
            "       │   └── NÃO ➔ Verificar Vedações (Gaxeta) e Válvula de Expurgo.",
            "       └── Falha ocorre durante a Fase de Esterilização (Platô)?",
            "           ├── SIM ➔ Calibrar/Substituir PT100 ou verificar desvio de calibração do Transdutor de Pressão.",
            "           └── NÃO ➔ Analisar fase de secagem/bomba de vácuo."
        ],
        "validacao_seguranca": """
        ### Protocolo de Validação Pós-Manutenção
        1. **Ensaio de Segurança Elétrica (NBR IEC 60601-1 / 61010-1):**
           * Resistência do Condutor de Proteção (Aterramento): $R_{PE} \le 0.1\,\Omega$.
           * Corrente de Fuga para a Carcaça: $I_{fuga} \le 500\,\mu\text{A}$ (em Condição Normal).
           * Resistência de Isolação: $> 10\,\text{M}\Omega$ a $500\,\text{V DC}$.
        2. **Validação Físico-Química e Biológica:**
           * Teste de Bowie & Dick (para autoclaves com pré-vácuo) para validar remoção de ar.
           * Indicador Químico Classe 5 ou 6 inserido em pacote desafio.
           * Teste de Indicador Biológico (*Geobacillus stearothermophilus*).
        """
    },

    "📈 Eletrocardiógrafo (ECG)": {
        "categoria": "Aquisição Bioelétrica",
        "fisica_aplicada": """
        ### 1. Eletrofisiologia e Amplificação Instrumental
        O coração funciona como um dipolo elétrico dinâmico que gera potenciais na superfície da pele na ordem de $0.5\,\text{mV}$ a $5\,\text{mV}$. A interface entre a pele (eletrólito líquido) e o eletrodo (metal Ag/AgCl) gera uma **tensão de offset de meia-célula** de até $\pm 300\,\text{mV}$, muito maior que o próprio sinal bioelétrico.

        ### 2. Razão de Rejeição em Modo Comum (CMRR)
        O corpo humano atua como uma antena captando a ruído da rede elétrica ($60\,\text{Hz}$). Para extrair o sinal diferencial de ECG na presença deste ruído de modo comum, utiliza-se um Amplificador de Instrumentação (InAmp) de alto CMRR ($> 100\,\text{dB}$).

        $$V_{out} = A_d (V^+ - V^-) + A_c \left(\frac{V^+ + V^-}{2}\right)$$

        *   **Circuito de Perna Direita (Right Leg Drive - RLD):** Reduz ativamente a tensão de modo comum injetando o sinal de ruído invertido de volta ao paciente, melhorando drasticamente o CMRR do sistema.
        """,
        "subsistemas": {
            "Interface Paciente": ["Eletrodos de Ag/AgCl", "Cabo de Paciente (10 Vias com Resistores de Proteção)"],
            "Front-End Analógico": ["Bloco de Proteção contra Desfibrilação", "Filtro Passa-Altas (0.05Hz)", "Amplificador de Instrumentação", "Filtro Notch (60Hz)"],
            "Processamento Digital": ["Isolador Galvânico (Opto/Digital)", "Conversor A/D (24-bit Sigma-Delta)", "DSP / MCU Principal"]
        },
        "componentes_detalhados": {
            "AMPLIFICADOR DE INSTRUMENTAÇÃO": {
                "o_que_e": "Circuito integrado analógico de altíssima precisão formado por três amplificadores operacionais internos.",
                "como_funciona": "Amplifica exclusivamente a diferença de potencial entre duas entradas de sinal elétrico, rejeitando de forma drástica tensões iguais presentes em ambas as entradas.",
                "principio_fisico": "Amplificação diferencial e Rejeição de Modo Comum (CMRR).",
                "como_testar": "1. Injetar sinal padrão de $1\,\text{mV peak-to-peak} @ 1\,\text{Hz}$ via Simulador de ECG e verificar amplitude no canal digitado.\n2. Injetar sinal de modo comum de $10\,\text{V}_{pp} @ 60\,\text{Hz}$ short-circuitando as entradas e medir o ruído residual na saída.",
                "sintomas_falha": "Sinal saturado na linha superior/inferior da tela; interferência massiva de rede elétrica de $60\,\text{Hz}$ em todas as derivações; ausência total de traçado.",
                "relacao_componentes": "Posicionado diretamente após o circuito de proteção contra desfibrilação e antes do Conversor A/D."
            },
            "CABO DE PACIENTE (10 VIAS)": {
                "o_que_e": "Conjunto de condutores blindados multifilamento projetados para conduzir bio-sinais microvolticos com resistores de proteção integrados.",
                "como_funciona": "Conecta os eletrodos fixados no paciente à entrada do amplificador. Incorpora em cada via um resistor de alta isolação (ex: $10\,\text{k}\Omega$) para dissipar energia em pulsos de desfibrilação.",
                "principio_fisico": "Condução elétrica blindada contra acoplamento capacitivo/indutivo externo.",
                "como_testar": "1. Testar continuidade condutora ponta-a-ponta de cada via com multímetro (esperado valor do resistor em série, ex: $10\,\text{k}\Omega \pm 5\%$).\n2. Testar curto-circuito entre vias adjacentes ou com a blindagem externa.",
                "sintomas_falha": "Linha reta em derivações específicas; ruído de mal contato (artefato) ao movimentar o cabo; mensagem 'Eletrodo Solto' constante.",
                "relacao_componentes": "Interface física direta entre a pele/eletrodo do paciente e a placa de entrada do equipamento."
            },
            "CIRCUITO DRIVE DE PERNA DIREITA (RLD)": {
                "o_que_e": "Malha de realimentação negativa composta por um amplificador operacional invertido.",
                "como_funciona": "Coleta o ruído em modo comum presente no paciente, inverte sua fase em $180^\circ$ e o reinjeta através do eletrodo RL (Perna Direita), cancelando a interferência $60\,\text{Hz}$.",
                "principio_fisico": "Inversão de fase e Cancelamento Ativo de Interferência.",
                "como_testar": "1. Medir a tensão AC no pino RL com o cabo conectado a um simulador.\n2. Desconectar a via RL no simulador e observar se o ruído de $60\,\text{Hz}$ amplifica exponencialmente.",
                "sintomas_falha": "Ruído severo de $60\,\text{Hz}$ em todas as 12 derivações simultaneamente, mesmo com o filtro Notch ativado.",
                "relacao_componentes": "Conectado ao nó comum das resistências de amostragem das derivações de membros."
            }
        },
        "diagrama_dot": """
        digraph ECG {
            graph [background=transparent, rankdir=LR];
            node [shape=box, style=filled, fillcolor="#1f2937", fontcolor="#ffffff", fontname="Helvetica"];
            edge [fontcolor="#ffffff", color="#4b5563"];

            Paciente [label="PACIENTE / ELETRODOS", fillcolor="#374151"];
            Cabo [label="CABO DE PACIENTE", fillcolor="#d97706"];
            Protecao [label="Proteção Desfibrilador", fillcolor="#991b1b"];
            InAmp [label="AMPLIFICADOR DE INSTRUMENTAÇÃO", fillcolor="#1e3a8a"];
            RLD [label="CIRCUITO RLD (RL)", fillcolor="#065f46"];
            ADC [label="Conversor A/D & Isolador", fillcolor="#374151"];
            Display [label="Display / Processamento", fillcolor="#1e3a8a"];

            Paciente -> Cabo;
            Cabo -> Protecao;
            Protecao -> InAmp [label="Sinal Diferencial"];
            InAmp -> RLD [label="Amostra Modo Comum"];
            RLD -> Paciente [label="Feedback Invertido"];
            InAmp -> ADC [label="Sinal Amplificado"];
            ADC -> Display [label="Dados Digitais (Isolados)"];
        }
        """,
        "matriz_falhas": [
            {
                "sintoma": "O traçado apresenta ondas senoidais perfeitas e espessas de 60Hz.",
                "causa_raiz": "Ruptura da malha de blindagem do cabo de paciente, impedância de contato eletrodo-pele excessiva ($> 5\,\text{k}\Omega$), ou falha no circuito RLD.",
                "teste": "Substituir o cabo por um simulador calibrado de ECG. Se o ruído desaparecer, a falha é no cabo/eletrodo; se mantiver, a falha é na placa de aquisição (RLD/InAmp)."
            },
            {
                "sintoma": "Ao disparar um desfibrilador no paciente, a linha do ECG fica reta e leva mais de 10 segundos para retornar.",
                "causa_raiz": "Diodos/Tubos de descarga a gás do circuito de proteção travados em condução ou capacitores de acoplamento saturados.",
                "teste": "Ensaio de tempo de recuperação pós-desfibrilação com simulador com gerador de pulso."
            }
        ],
        "arvore_decisao": [
            "1. Início: Sinal com ruído ou falha de leitura?",
            "   ├── Desconectar cabo do paciente e conectar SIMULADOR DE ECG CALIBRADO.",
            "   ├── O ruído desapareceu no simulador?",
            "   │   ├── SIM ➔ O problema está no Cabo de Paciente, Eletrodos ou Preparação de Pele.",
            "   │   └── NÃO ➔ A falha é no Equipamento (Hardware Interno).",
            "   └── Se a falha é interna:",
            "       ├── Afeta APENAS UMA derivação? ➔ Falha na Chave Multiplexadora de entrada daquela via.",
            "       └── Afeta TODAS as derivações? ➔ Falha no Circuito RLD, Barreira de Isolação ou Fonte Interna."
        ],
        "validacao_seguranca": """
        ### Protocolo de Validação Pós-Manutenção (IEC 60601-2-25)
        1. **Ensaio de Segurança Elétrica Rígido (Parte Aplicada Tipo CF):**
           * Corrente de Fuga no Paciente (Patient Leakage Current):
             * Condição Normal: $I \le 10\,\mu\text{A}$ AC / $10\,\mu\text{A}$ DC.
             * Condição de Sobrefalha (Single Fault Condition): $I \le 50\,\mu\text{A}$.
           * Tensão de Isolação da Parte Aplicada: Injeção de $4000\,\text{V AC}$ na barreira galvânica.
        2. **Teste Metrológico de Sinal:**
           * Erro de Amplitude de Sinal ($1\,\text{mV}_{pp}$): Margem tolerada $\le \pm 5\%$.
           * Resposta em Frequência (Banda Passante): $0.05\,\text{Hz}$ a $150\,\text{Hz}$.
        """
    }
}

# ==========================================================
# INTERFACE STREAMLIT
# ==========================================================

st.title("⚡ Engenharia Clínica | Guia de Campo V3")
st.caption("Documentação de Profundidade Técnica, Física Aplicada e Diagnóstico Sistemático")

# Seleção de Equipamento na Sidebar
equipamento_sel = st.sidebar.selectbox("Selecione o Equipamento:", list(EQUIPAMENTOS_V3.keys()))
dados = EQUIPAMENTOS_V3[equipamento_sel]

st.sidebar.markdown("---")
st.sidebar.info(f"**Categoria:** {dados['categoria']}")

# TABS PRINCIPAIS
tab_fisica, tab_componentes, tab_diagrama, tab_subsistemas, tab_falhas, tab_decisao, tab_validacao = st.tabs([
    "🔬 1. Princípios de Física",
    "⚙️ 2. Componentes",
    "📊 3. Diagrama Interativo",
    "🧩 4. Mapa de Subsistemas",
    "💥 5. Matriz de Falhas",
    "🌳 6. Árvore de Decisão",
    "🛡️ 7. Validação & Segurança"
])

# 1. PRINCIPIOS DE FISICA
with tab_fisica:
    st.header(f"Física Aplicada ao Funcionamento — {equipamento_sel}")
    st.markdown(dados["fisica_aplicada"], unsafe_allow_html=True)

# 2. COMPONENTES DETALHADOS
with tab_componentes:
    st.header("Análise Detalhada de Componentes")
    comp_nomes = list(dados["componentes_detalhados"].keys())
    comp_selecionado = st.selectbox("Selecione o componente para detalhamento:", comp_nomes)
    
    c_info = dados["componentes_detalhados"][comp_selecionado]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 📌 {comp_selecionado}")
        st.write(f"**O que é:** {c_info['o_que_e']}")
        st.write(f"**Como Funciona:** {c_info['como_funciona']}")
        st.write(f"**Princípio Físico:** `{c_info['principio_fisico']}`")
    
    with col2:
        st.markdown("### 🛠️ Protocolo de Diagnóstico")
        st.info(f"**Como Testar:**\n{c_info['como_testar']}")
        st.error(f"**Sintomas de Falha:**\n{c_info['sintomas_falha']}")
        st.warning(f"**Relação Sistemática:**\n{c_info['relacao_componentes']}")

# 3. DIAGRAMA INTERATIVO
with tab_diagrama:
    st.header("Diagrama de Arquitetura Interativo")
    st.write("Clique nos nós do diagrama para renderizar o raio-x e as dependências operacionais.")
    
    # Renderizar Graphviz
    graph = graphviz.Source(dados["diagrama_dot"])
    st.graphviz_chart(dados["diagrama_dot"])
    
    st.markdown("---")
    st.subheader("🔍 Inspeção do Nó Selecionado")
    no_clicado = st.selectbox("Selecione o bloco do diagrama para inspecionar:", list(dados["componentes_detalhados"].keys()))
    
    if no_clicado in dados["componentes_detalhados"]:
        detalhe = dados["componentes_detalhados"][no_clicado]
        st.markdown(f"**Funcionamento do bloco [{no_clicado}]:** {detalhe['como_funciona']}")
        st.markdown(f"**Teste Rápido:** {detalhe['como_testar']}")

# 4. MAPA DE SUBSISTEMAS
with tab_subsistemas:
    st.header("Divisão por Subsistemas Operacionais")
    for sub, comps in dados["subsistemas"].items():
        with st.expander(f"⚙️ Subsistema: {sub}", expanded=True):
            for item in comps:
                st.markdown(f"- **{item}**")

# 5. MATRIZ DE FALHAS
with tab_falhas:
    st.header("Matriz Sistemática de Falhas e Causas Raiz")
    df_falhas = pd.DataFrame(dados["matriz_falhas"])
    st.table(df_falhas)

# 6. ARVORE DE DECISAO
with tab_decisao:
    st.header("Fluxograma Lógico de Diagnóstico")
    for passo in dados["arvore_decisao"]:
        st.code(passo, language="text")

# 7. VALIDACAO E SEGURANCA
with tab_validacao:
    st.header("Protocolos Metrológicos e NBR IEC 60601")
    st.markdown(dados["validacao_seguranca"], unsafe_allow_html=True)
