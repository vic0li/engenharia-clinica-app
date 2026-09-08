import json
from datetime import datetime
import pandas as pd
import streamlit as st

# ==========================================================
# ENGENHARIA CLÍNICA - GUIA DE CAMPO V5
# Filosofia:
# PRINCÍPIO FÍSICO → COMPONENTE → SINTOMA → HIPÓTESE
# → TESTE → DIAGNÓSTICO → PROCEDIMENTO DE REPARO PASSO A PASSO → VALIDAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Engenharia Clínica | Guia de Campo Técnico V5",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# ESTILO — ALTO CONTRASTE / MODO TÉCNICO
# ----------------------------------------------------------
st.markdown(
    """
<style>
/* Fundo geral */
.stApp {
    background: #0f172a;
    color: #f8fafc;
}

/* Área principal */
.main .block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Texto */
h1, h2, h3, h4, h5, h6,
p, li, label, .stMarkdown, .stMarkdown p, .stCaption {
    color: #f8fafc !important;
}

/* Cards personalizados */
.hero {
    padding: 1.8rem;
    border-radius: 16px;
    background: linear-gradient(135deg, #1e293b, #0f766e);
    border: 1px solid #38bdf8;
    color: #ffffff !important;
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.hero h1, .hero h2, .hero h3, .hero p { color: #ffffff !important; }

.concept {
    padding: 1rem;
    border-left: 5px solid #38bdf8;
    background-color: #1e293b;
    color: #f8fafc !important;
    border-radius: 8px;
    margin: 0.7rem 0;
}
.concept * { color: #f8fafc !important; }

.tech-box {
    padding: 1.2rem;
    border-left: 5px solid #10b981;
    background-color: #064e3b;
    color: #ecfdf5 !important;
    border-radius: 8px;
    margin: 0.8rem 0;
}
.tech-box * { color: #ecfdf5 !important; }

.warning-box {
    padding: 1rem;
    border-left: 5px solid #f59e0b;
    background-color: #422006;
    color: #fff7ed !important;
    border-radius: 8px;
    margin: 0.8rem 0;
}
.warning-box * { color: #fff7ed !important; }

.danger-box {
    padding: 1rem;
    border-left: 5px solid #ef4444;
    background-color: #450a0a;
    color: #fef2f2 !important;
    border-radius: 8px;
    margin: 0.8rem 0;
}
.danger-box * { color: #fef2f2 !important; }

/* Expansores */
details {
    background-color: #1e293b !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
    margin-bottom: 0.6rem !important;
}
details summary, details p, details div { color: #f8fafc !important; }

/* Inputs e selectbox */
.stSelectbox > div > div,
.stTextInput input,
.stTextArea textarea {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border-color: #64748b !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #38bdf8 !important;
    border-bottom-color: #38bdf8 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827 !important;
}
section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

/* Dataframes */
.stDataFrame, [data-testid="stDataFrame"] {
    background-color: #1e293b !important;
}

/* Código e diagramas */
pre, code {
    background-color: #020617 !important;
    color: #38bdf8 !important;
    font-size: 0.95rem !important;
}

/* Métricas */
[data-testid="stMetric"] {
    background-color: #1e293b;
    border: 1px solid #475569;
    padding: 0.8rem;
    border-radius: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# BASE TÉCNICA E GUIAS DE REPARO TIPO IFIXIT
# ==========================================================

EQUIPAMENTOS = {
    "♨️ Autoclave": {
        "tipo": "Esterilização por calor úmido sob pressão",
        "objetivo": """
A autoclave esteriliza artigos críticos via vapor saturado sob pressão. O processo exige o trinômio 
**Temperatura x Pressão x Tempo**, além de remoção prévia de ar e vapor livre de gases não condensáveis.
""",
        "raciocinio": [
            (
                "1. Transferência Térmica",
                "O vapor condensa na carga, liberando calor latente de vaporização (~2260 kJ/kg).",
            ),
            (
                "2. Remoção de Ar",
                "Ar atua como isolante térmico e impede o contato direto do vapor com o instrumental.",
            ),
            (
                "3. Malha de Controle",
                "Sensores PT100/NTC e transdutores de pressão informam a CLP/Placa Controladora.",
            ),
            (
                "4. Cadeia de Falha",
                "Identifique se o problema é elétrico (potência/comando), pneumático/hidráulico (vedação/válvulas) ou de instrumentação.",
            ),
        ],
        "principio": """
### Fluxo de Trabalho e Potência
**Rede Elétrica AC → Filtro EMI → Relé/SSR → Resistência Tubular → Caldeira/Câmara → Válvula Solenóide → Exaustão**
""",
        "componentes": [
            (
                "Câmara de Pressão",
                "Vaso de pressão em aço inox (AISI 304/316L).",
                "Deformações ou microfissuras invalidam o vaso.",
            ),
            (
                "Gaxeta de Vedação",
                "Anel de silicone elastomérico de alta temperatura.",
                "Ressecamento ou rasgos causam fuga de pressão.",
            ),
            (
                "Resistência Elétrica",
                "Elemento blindado de imersão/contato.",
                "Pode abrir circuito ou apresentar fuga para terra (massa).",
            ),
            (
                "Válvula Solenóide",
                "Válvula de controle de exaustão/água (NC/NO).",
                "Obstrução por incrustação de calcário/sujeira.",
            ),
            (
                "Sensor PT100",
                "Termorresistência de platina para leitura precisa.",
                "Descalibração ou rompimento do spiro.",
            ),
            (
                "Válvula de Segurança",
                "Dispositivo mecânico de alívio por sobrepressão.",
                "Travamento por oxidação ou mola fadigada.",
            ),
        ],
        "problemas": [
            {
                "titulo": "Vazamento de vapor na porta",
                "sintoma": "Vazamento visível ou ruído de escape de vapor na borda do fecho durante a pressurização.",
                "cadeia": "Pressão da câmara → Vedação mecânica da gaxeta → Ajuste de fecho da porta.",
                "causas": [
                    "Gaxeta impregnada com sujidade ou ressecada",
                    "Gaxeta montada no sentido invertido",
                    "Desalinhamento da trava mecânica da porta",
                    "Superfície da borda da câmara oxidada/danificada",
                ],
                "passos_diagnostico": [
                    "Aguardar despressurização total e resfriamento abaixo de 40°C.",
                    "Inspecionar a gaxeta visualmente sob iluminação focalizada.",
                    "Verificar presença de deformação permanente no silicone.",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Intermediário",
                    "ferramentas": [
                        "Chave Allen / Torx",
                        "Álcool Isopropílico 99%",
                        "Pano livre de fiapos",
                        "Gaxeta de reposição original (Silicone)",
                        "Graxa de silicone atóxica de alta temperatura",
                    ],
                    "passos": [
                        "**Passo 1 (Isolamento Energético):** Desconecte o equipamento da tomada de rede elétrica e garanta manômetro em ZERO bar.",
                        "**Passo 2 (Remoção do Vedante):** Com auxílio de uma espátula plástica (não use chave de fenda para não riscar o inox), remova a gaxeta antiga da canaleta da porta.",
                        "**Passo 3 (Higienização do Assento):** Limpe profundamente a cavidade da canaleta utilizando pano umedecido em álcool isopropílico até remover resíduos endurecidos.",
                        "**Passo 4 (Instalação da Nova Gaxeta):** Aplique uma camada microscópica de graxa de silicone atóxica na nova gaxeta. Insira-a na câmara iniciando pelos 4 pontos cardeais (12h, 6h, 9h, 3h) para garantir distribuição uniforme do elastômero sem esticar.",
                        "**Passo 5 (Ajuste Mecânico do Fecho):** Caso o vazamento persista, ajuste a porca micrométrica de pressão do fecho/trinco da porta com chave adequada, incrementando 1/4 de volta até obter resistência adequada ao fechar.",
                        "**Passo 6 (Validação e Teste de Estanqueidade):** Execute um ciclo completo de teste a vazio a 134°C. Monitore com detector visual ou sabão neutro nas bordas. Verifique a ausência de quedas de pressão na fase de esterilização.",
                    ],
                    "seguranca": "Risco de queimadura severa e projeção de vapor sob pressão. NUNCA tente ajustar trincos com a câmara pressurizada.",
                },
            },
            {
                "titulo": "Liga o painel, mas não aquece",
                "sintoma": "Display ativo, ciclo iniciado, porém a temperatura permanece ambiente e não há geração de pressão.",
                "cadeia": "Comando CLP → Relé/SSR → Termostato de Segurança → Resistência Tubular.",
                "causas": [
                    "Termostato rearmável (Bimetálico) disparado",
                    "Resistência elétrica queimada (Circuito Aberto)",
                    "Relé de Estado Sólido (SSR) ou Relé de Potência defeituoso",
                    "Sensor de nível de água não detecta água na câmara",
                ],
                "passos_diagnostico": [
                    "Verificar status dos LEDs indicadores de acionamento de resistência na placa.",
                    "Testar se o termostato de segurança mecânico abriu o circuito.",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Avançado",
                    "ferramentas": [
                        "Multímetro Digital True RMS com pontas de prova",
                        "Alicate amperímetro",
                        "Chave de fenda/Phillips isolada 1000V",
                        "Resistência de substituição",
                    ],
                    "passos": [
                        "**Passo 1 (Desconexão da Rede):** Desligue a autoclave do disjuntor principal e retire o cabo da tomada.",
                        "**Passo 2 (Teste do Termostato de Proteção):** Localize o termostato bimetálico rearmável no fundo da câmara. Pressione o pino central de reset até ouvir um 'click'. Meça a continuidade com o multímetro (deve indicar < 1 Ohm).",
                        "**Passo 3 (Medição da Resistência Elétrica):** Desconecte os terminais elétricos da resistência. Com o multímetro na escala de Resistência (Ω), meça o valor entre os terminais. (Exemplo: para 1200W/220V, o valor esperado é ~40 Ohms). Se indicar 'OL' ou resistência infinita, a resistência está queimada e deve ser substituída.",
                        "**Passo 4 (Teste de Fuga para a Massa):** Meça a resistência entre cada terminal da resistência e a carcaça de aterramento. O valor deve ser maior que 10 MΩ. Se houver continuidade, substitua a resistência devido ao risco de choque elétrico.",
                        "**Passo 5 (Verificação do Acionamento SSR/Relé):** Energize o equipamento com cuidado. Na fase de aquecimento, meça com o multímetro em VCA a tensão na saída do relé/SSR para a resistência. Se houver tensão de entrada no relé mas não houver saída, substitua o relé defeituoso.",
                        "**Passo 6 (Montagem e Teste de Corrente):** Reconecte os terminais isolados. Ligue o equipamento e utilize um alicate amperímetro no condutor fase da resistência para confirmar o consumo de corrente nominal durante o aquecimento.",
                    ],
                    "seguranca": "Perigo de choque elétrico em alta tensão (220V/110V) e alta corrente. Testes com equipamento energizado devem ser executados apenas com EPIS adequados.",
                },
            },
        ],
    },
    "📈 Eletrocardiógrafo": {
        "tipo": "Aquisição e amplificação de biopotenciais elétricos",
        "objetivo": """
Capturar biopotenciais bioelétricos cardíacos na ordem de 0.5mV a 5mV através de eletrodos de superfície, 
rejeitando ruídos de modo comum de 60Hz da rede elétrica e ruídos miográficos.
""",
        "raciocinio": [
            (
                "1. Biopotencial",
                "O sinal elétrico é captado por reações de óxido-redução na interface Ag/AgCl do eletrodo.",
            ),
            (
                "2. Rejeição de Modo Comum (CMRR)",
                "Amplificadores de instrumentação (ex: INA128) exigem alto CMRR (>100dB) para eliminar 60Hz.",
            ),
            (
                "3. Pernas/Drive de Perna Direita (DRD)",
                "Circuito ativo que injeta o ruído em contra-fase no paciente para cancelar a interferência.",
            ),
            (
                "4. Isolação Galvânica",
                "Barreira optoacoplada ou transformador isolador para proteção do paciente (Parte Aplicada Tipo CF).",
            ),
        ],
        "principio": """
### Cadeia Analógica
**Eletrodo Ag/AgCl → Cabo paciente → Proteção ESD/Defibrilador → Filtro Passa-Baixa Passive → Amplificador de Instrumentação → Isolação Galvânica → ADC → DSP**
""",
        "componentes": [
            (
                "Cabo de Paciente",
                "Conjunto de condutores blindados com malha trançada.",
                "Ruptura interna do cobre por dobramento excessivo.",
            ),
            (
                "Eletrodos de Clipes/Ventosas",
                "Sensores Ag/AgCl de contato direto.",
                "Oxidação do banho de prata gerando ruído offset.",
            ),
            (
                "Circuito de Proteção contra Desfibrilação",
                "Lâmpadas neon / Diodos TVS de corte de surto.",
                "Curto-circuito após absorver choque de desfibrilador.",
            ),
            (
                "Amplificador de Instrumentação",
                "CI de alta impedância de entrada (>10 MΩ).",
                "Dano por descarga eletrostática (ESD).",
            ),
        ],
        "problemas": [
            {
                "titulo": "Traçado com ruído excessivo de 60Hz / Linha de base grossa",
                "sintoma": "Interferência senoidal contínua de alta frequência saturando a visualização do complexo QRS.",
                "cadeia": "Pele do Paciente → Impedância do Eletrodo → Blindagem do Cabo → Circuito DRL → Aterramento.",
                "causas": [
                    "Aterramento elétrico da tomada ausente ou deficiente",
                    "Geleira/sujeira acumulada nos conectores das garras/clipes",
                    "Ruptura da malha de blindagem do cabo de paciente",
                    "Cabo do paciente correndo em paralelo a cabos de rede elétrica de 220V",
                ],
                "passos_diagnostico": [
                    "Desconectar o cabo do paciente e conectar um Simulador de ECG homologado.",
                    "Observar se o ruído desaparece com o simulador.",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Fácil a Intermediário",
                    "ferramentas": [
                        "Simulador de ECG / Paciente",
                        "Multímetro com escala de continuidade",
                        "Lixa d'água bem fina (Grão 1200) ou palha de aço",
                        "Álcool Isopropílico",
                        "Analisador de Segurança Elétrica",
                    ],
                    "passos": [
                        "**Passo 1 (Descarte do Ambiente/Aterramento):** Ligue o equipamento em uma tomada aterrada confirmada. Teste o neutro e terra da tomada com multímetro (diferença de potencial Neutro-Terra deve ser < 2VCA).",
                        "**Passo 2 (Limpeza dos Contatos de Eletrodos):** Se o ruído for no paciente, limpe os eletrodos metálicos de ventosa/clipe com álcool isopropílico. Se houver camada de oxidação escura, passe levemente a lixa grão 1200 para expor a camada condutora.",
                        "**Passo 3 (Teste de Continuidade do Cabo de Paciente):** Desconecte o cabo de paciente do ECG. Com o multímetro na escala de continuidade (bip), meça cabo a cabo: do pino do conector DB15/DB25 até a ponta de banana/clipe correspondente (ex: RA, LA, LL, V1-V6). O valor deve ser próximo de 0 Ohms ou ~1kΩ a 10kΩ caso haja resistor de proteção interno anti-desfibrilação no cabo.",
                        "**Passo 4 (Teste da Blindagem):** Meça a continuidade entre o pino do conector referente à blindagem (shield) e a malha do cabo. Se houver interrupção da blindagem, substitua o cabo completo por um novo cabo blindado.",
                        "**Passo 5 (Teste com Simulador e Validação):** Conecte o cabo ao Simulador de ECG e configure um sinal padrão de 1mV a 60 BPM. Selecione filtros de rede (Filtro Notch 60Hz ligado). Confirme um traçado limpo sem flutuações de linha de base.",
                    ],
                    "seguranca": "Garantir isolamento elétrico total conforme norma ABNT NBR IEC 60601-1 / CF para evitar correntes de fuga no paciente.",
                },
            }
        ],
    },
    "💨 Compressor": {
        "tipo": "Geração e armazenamento de energia pneumática isenta de óleo",
        "objetivo": """
Comprimir ar atmosférico limpo e seco para alimentar consultórios e equipamentos pneumáticos sem contaminação por lubrificantes.
""",
        "raciocinio": [
            (
                "1. Admissão e Compressão",
                "O pistão com anel de teflon reduz o volume do cilindro aumentando a pressão.",
            ),
            (
                "2. Retenção",
                "Válvulas unidirecionais impedem o retorno do ar comprimido do reservatório para o cabeçote.",
            ),
            (
                "3. Pressostato",
                "Interruptor pressórico comuta os contatos do motor entre a pressão de liga (ex: 80 PSI) e desliga (ex: 120 PSI).",
            ),
            (
                "4. Drenagem de Umidade",
                "O processo de compressão condensa a umidade do ar, exigindo purga periódica.",
            ),
        ],
        "principio": """
### Cadeia Pneumática
**Filtro de Ar → Válvula de Admissão → Cilindro/Pistão → Válvula de Descarga → Válvula de Retenção → Reservatório (Vaso de Pressão) → Pressostato → Regulador/Filtro Coalescente**
""",
        "componentes": [
            (
                "Pressostato",
                "Dispositivo eletromecânico ajustável de acionamento.",
                "Descalibração da mola ou contatos elétricos carbonizados.",
            ),
            (
                "Válvula de Retenção",
                "Válvula de sentido único na entrada do tanque.",
                "Vedações de borracha desgastadas deixando retornar ar.",
            ),
            (
                "Anel de Pistão (PTFE/Teflon)",
                "Vedação mecânica do pistão sem óleo.",
                "Desgaste por abrasão reduzindo a capacidade de vazão.",
            ),
            (
                "Capacitor de Partida",
                "Componente elétrico que cria o defasamento para partida do motor monofásico.",
                "Perda de capacitância (microfarads abaixo do nominal).",
            ),
        ],
        "problemas": [
            {
                "titulo": "Motor murmura (ronca), mas não consegue dar partida",
                "sintoma": "Ao cair a pressão, o motor tenta ligar, produz um zumbido grave e desarma o protetor térmico após alguns segundos.",
                "cadeia": "Pressostato → Capacitor de Partida → Enrolamento Auxiliar → Motor elétrico → Contra-pressão da Válvula de Retenção.",
                "causas": [
                    "Capacitor de partida/marcha esgotado ou queimado",
                    "Válvula de retenção presa aberta (deixando pressão travada no cabeçote)",
                    "Válvula de alívio/despressurização do pressostato travada",
                    "Baixa tensão de alimentação na rede elétrica (queda de tensão abaixo de 10%)",
                ],
                "passos_diagnostico": [
                    "Efetuar medição da tensão da tomada sob carga.",
                    "Despressurizar completamente o reservatório e tentar ligar.",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Intermediário",
                    "ferramentas": [
                        "Multímetro com Capacímetro",
                        "Chave de boca / Chave inglesa",
                        "Alicate Amperímetro",
                        "Capacitor de reposição (mesmo valor em µF e Volts)",
                        "Veda-rosca (Fita PTFE)",
                    ],
                    "passos": [
                        "**Passo 1 (Despressurização e Desconexão):** Abra o dreno do reservatório até zerar o manômetro de pressão. Desconecte o compressor da energia.",
                        "**Passo 2 (Diagnóstico da Válvula de Retenção):** Se o compressor consegue dar partida com o tanque em ZERO PSI, mas falha quando o tanque tem pressão, a Válvula de Retenção está defeituosa. Desmonte a válvula na entrada do tanque, limpe o disco de vedação interno de nitrila e substitua a mola de retorno.",
                        "**Passo 3 (Teste do Capacitor de Partida):** Abra a caixa de ligação do motor. Descarregue o capacitor encostando uma chave com cabo isolado nos dois terminais. Desconecte ao menos um terminal do capacitor. Configure o multímetro na função Capacímetro (µF). Meça o valor e compare com o rótulo do componente (ex: 45µF ±5%). Se o valor medido for inferior a 10% do nominal, substitua o capacitor.",
                        "**Passo 4 (Substituição do Capacitor):** Instale o novo capacitor respeitando a isolação dos terminais. Garanta conexões firmes.",
                        "**Passo 5 (Teste da Válvula de Alívio do Pressostato):** Quando o compressor desliga ao atingir a pressão máxima, ouve-se um pequeno espirro de ar ('psssht') perto do pressostato. Esse espirro é a liberação de ar da linha entre o cabeçote e a retenção. Se não ocorrer esse espirro, substitua a micro-válvula de alívio do pressostato.",
                        "**Passo 6 (Teste e Monitoramento de Amperagem):** Energize o compressor. Ligue-o e meça a corrente de partida e de trabalho no condutor fase utilizando o alicate amperímetro. Confirme se a corrente permanece dentro da corrente nominal (In) da plaqueta do motor.",
                    ],
                    "seguranca": "Reservatórios são vasos de pressão sujeitos a riscos de explosão por fadiga ou sobrepressão. NUNCA altere o lacre da válvula de segurança mecânica.",
                },
            }
        ],
    },
    "❄️ Câmara fria / Câmara de vacina": {
        "tipo": "Conservação térmica controlada de insumos imunobiológicos (2°C a 8°C)",
        "objetivo": """
Manter a temperatura homogênea no interior da câmara dentro da faixa restrita de 2.0°C a 8.0°C, 
com sistema de emergência, registrador de dados (datalogger) e autonomia em caso de queda de energia.
""",
        "raciocinio": [
            (
                "1. Mudança de Fase",
                "O fluido refrigerante (ex: R134a/R600a) absorve calor na evaporação e rejeita calor na condensação.",
            ),
            (
                "2. Homogeneidade",
                "Forçadores de ar com ventiladores axiais mantêm a temperatura idêntica em todas as prateleiras.",
            ),
            (
                "3. Degelo Inteligente (Defrost)",
                "Ciclos de degelo por resistência ou gás quente evitam o bloqueio do evaporador por acúmulo de gelo.",
            ),
            (
                "4. Calibração do Sensor",
                "Sensores em poço termo-amortecido (solução de glicol) simulam a temperatura real do frasco de vacina.",
            ),
        ],
        "principio": """
### Cadeia de Refrigeração e Controle
**Compressor Hermético → Condensador Aletado → Filtro Secador → Tubo Capilar / Válvula de Expansão → Evaporador → Linha de Sucção → Sensor PT100/NTC → Microprocessador PID**
""",
        "componentes": [
            (
                "Compressor Hermético",
                "Bomba do fluido refrigerante.",
                "Perda de rendimento mecânico (compressão fraca) ou travamento.",
            ),
            (
                "Microcontrolador / Termostato PID",
                "Cérebro eletrônico do equipamento.",
                "Desalinhamento de parâmetros PID ou falha nos relés de comando.",
            ),
            (
                "Sensor de Temperatura NTC/PT100",
                "Elemento sensor imerso em solução neutra.",
                "Deriva térmica (sensor 'mentindo' a temperatura real).",
            ),
            (
                "Micro-motor Evaporador",
                "Ventilador forçador de ar interno.",
                "Queima do enrolamento ou travamento por bucha gasta.",
            ),
        ],
        "problemas": [
            {
                "titulo": "Temperatura subindo acima de 8.0°C / Alarme de Alta Temperatura",
                "sintoma": "Display indicando subida gradual de temperatura (ex: 10.5°C) e alarme sonoro ativado.",
                "cadeia": "Carga Térmica → Ventilação Evaporador → Troca Térmica no Condensador → Fluido Refrigerante → Compressor.",
                "causas": [
                    "Sujeira/poeira acumulada bloqueando as aletas do condensador externo",
                    "Bloqueio de gelo no evaporador interno por falha no degelo",
                    "Microvazamento de gás refrigerante no sistema selado",
                    "Gaxeta magnética da porta danificada permitindo entrada de ar quente",
                ],
                "passos_diagnostico": [
                    "Transferir IMEDIATAMENTE as vacinas para caixa térmica de transporte com gelo reciclável e termômetro calibrado.",
                    "Inspecionar a colmeia do condensador.",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Avançado",
                    "ferramentas": [
                        "Manômetro de Refrigeração (Manifold para R134a/R600a)",
                        "Pincel macio / Aspirador de pó / Ar comprimido",
                        "Termômetro Padrão Calibrado (Inmetro)",
                        "Detector de vazamento de fluido refrigerante",
                        "Multímetro",
                    ],
                    "passos": [
                        "**Passo 1 (Plano de Contingência de Vacinas):** Transfira 100% da carga para recipiente térmico adequado mantendo a cadeia de frio antes de qualquer intervenção.",
                        "**Passo 2 (Limpeza do Condensador):** Remova a grade traseira/inferior. Com um pincel macio e aspirador de pó, limpe completamente o pó e fiapos acumulados nas aletas de alumínio do condensador. A sujeira impede a troca térmica e faz o compressor esquentar e desarmar por protetor térmico.",
                        "**Passo 3 (Verificação do Bloqueio de Gelo):** Abra o gabinete e verifique a hélice do ventilador do evaporador. Se houver placa de gelo cobrindo as aletas do evaporador, execute um degelo forçado ou utilize soprador térmico em baixa temperatura para derreter o gelo. Inspecione a resistência de degelo com o multímetro.",
                        "**Passo 4 (Verificação da Pressão de Gás):** Com o compressor ligado, conecte a mangueira de baixa do Manifold na válvula de serviço (Schrader). Verifique se a pressão de sucção está dentro do especificado pelo fabricante (Ex: para R134a, normalmente entre 0 a 12 PSI dependendo do evaporador). Pressão negativa (vácuo) indica vazamento ou obstrução no tubo capilar.",
                        "**Passo 5 (Teste do Sensor e Calibração):** Coloque a ponta do termômetro padrão calibrado junto ao sensor da câmara dentro do poço de glicol. Aguarde 15 minutos. Compare a leitura do display com a leitura do padrão. Caso haja diferença > 0.5°C, acesse o menu técnico do controlador e ajuste o parâmetro de OFFSET de temperatura.",
                        "**Passo 6 (Validação do Ciclo de Historiador):** Realize um teste de qualificação térmica por no mínimo 4 horas, verificando a estabilidade no gráfico do datalogger entre 2.0°C e 8.0°C antes de liberar para o uso da enfermagem.",
                    ],
                    "seguranca": "Fluidos refrigerantes tipo R600a (Isobutano) são altamente inflamáveis. Exigem cuidados extremoz contra faíscas durante soldagem/manutenção.",
                },
            }
        ],
    },
    "🩸 Esfigmomanômetro": {
        "tipo": "Medição não invasiva de pressão arterial (NIBP / NIPB)",
        "objetivo": """
Medir a Pressão Arterial Sistólica (PAS) e Diastólica (PAD) por meio de algoritmo oscilométrico, 
detectando as micro-oscilações de pressão geradas pela parede da artéria no manguito.
""",
        "raciocinio": [
            (
                "1. Pressão Dinâmica",
                "A micro-bomba infla o manguito acima da pressão sistólica esperada estangulando o fluxo sanguíneo.",
            ),
            (
                "2. Transdução Piezorresistiva",
                "O sensor de pressão (ex: ponte de Wheatstone de silício) converte a pressão pneumática em mV elétrico.",
            ),
            (
                "3. Filtro Analógico/Algoritmo",
                "O circuito separa o sinal DC (pressão estática do manguito) do sinal AC (pulsos arteriais de 1Hz a 3Hz).",
            ),
            (
                "4. Deflação Controlada",
                "A válvula solenóide de sangria libera a pressão a uma taxa linear de 2 a 3 mmHg por segundo.",
            ),
        ],
        "principio": """
### Cadeia do Módulo NIBP
**Manguito/Bolsa de Borracha → Acoplamento Rápido → Tubo Pneumático → Sensor Piezoelétrico → Amplificador Operacional → Micro-Bomba DC → Válvula Solenóide de Escorva → Processador**
""",
        "componentes": [
            (
                "Bolsa Inflável (Bladder)",
                "Bolsa de elastômero vulcanizado dentro do manguito de velkro.",
                "Micro-furos por ressecamento ou dobra continuada.",
            ),
            (
                "Sensor de Pressão Silício",
                "Transdutor piezorresistivo de alta precisão.",
                "Deriva de Zero (Zero Offset drift) requerendo calibração.",
            ),
            (
                "Micro-Válvula de Sangria",
                "Solenóide de controle proporcional de vazão.",
                "Entrada de fiapos da fita velcro travando o embolo.",
            ),
            (
                "Conector Engate Rápido",
                "Conexão macho/fêmea de encaixe do tubo.",
                "Anel O-Ring interno cortado ou ausente.",
            ),
        ],
        "problemas": [
            {
                "titulo": "Erro de Vazamento / Não consegue pressurizar (Erro de Deflação)",
                "sintoma": "A bomba funciona por longo período, a pressão no display sobe devagar ou aborta exibindo mensagem 'ERROR 1' / 'LEAK'.",
                "cadeia": "Comando de Bomba → Conectores Pneumáticos → Tubulação Interna → Manguito → Válvula de Exaustão.",
                "causas": [
                    "Bolsa de borracha interna do manguito furada",
                    "Anel de vedação O-ring do conector de engate rápido danificado",
                    "Tubo de silicone interno desconectado da placa principal",
                    "Válvula solenóide com sujeira no assento de vedação",
                ],
                "passos_diagnostico": [
                    "Conectar um manômetro digital calibrado / Analisador de NIBP para teste de decaimento de pressão (Pneumatic Leak Test).",
                ],
                "guia_reparo_passo_a_passo": {
                    "dificuldade": "Fácil a Intermediário",
                    "ferramentas": [
                        "Analisador de PNI / Manômetro Digital de Precisão",
                        "Seringa de 60ml ou Pera de insuflação com válvula",
                        "Recipiente com água e sabão (para teste de bolhas)",
                        "O-rings de reposição de silicone",
                        "Chave de precisão para abertura de gabinete",
                    ],
                    "passos": [
                        "**Passo 1 (Isolamento do Problema - Manguito vs Equipamento):** Desconecte o manguito do monitor. Conecte um manguito novo/testado ou um reservatório rígido de 500ml (simulador). Se o problema sumir, o defeito está no manguito/tubo do paciente.",
                        "**Passo 2 (Teste de Estanqueidade do Manguito):** Remova a bolsa de borracha interna do tecido de velkro. Infle a bolsa até 150 mmHg utilizando uma pera de insuflação com manômetro. Submerja a bolsa em um recipiente com água limpa e observe o aparecimento de bolhas de ar. Se houver bolhas, substitua o refil da bolsa inflável.",
                        "**Passo 3 (Inspecionar Engate Rápido):** Examine o interior do conector fêmea no painel do aparelho. Verifique se o anel de vedação (O-ring) está posicionado corretamente ou ressecado. Substitua o O-ring e aplique graxa de silicone atóxica.",
                        "**Passo 4 (Teste de Decaimento Interno):** Se o manguito estiver perfeito, abra o gabinete do monitor. Conecte o analisador de NIBP na saída. Utilize o menu técnico do equipamento para entrar no 'SERVICE MODE / LEAK TEST'. O equipamento inflará o sistema até 250 mmHg e fechará as válvulas. Aguarde 60 segundos. O decaimento de pressão NÃO deve exceder 5 mmHg em 1 minuto.",
                        "**Passo 5 (Limpeza da Válvula Solenóide):** Se houver decaimento rápido interno, desconecte a mangueira da solenóide de exaustão. Aplique um jato de álcool isopropílico e ar comprimido seco através dos orifícios da válvula solenóide para remover poeira e fiapos retidos no embolo.",
                        "**Passo 6 (Calibração e Zero Linear):** Após sanar o vazamento, execute a calibração de pressão estática utilizando o analisador de PNI em 50, 100, 150 e 200 mmHg, garantindo erro menor que ±3 mmHg em todos os pontos.",
                    ],
                    "seguranca": "Erros de medição de pressão arterial podem levar a diagnósticos incorretos de hipertensão ou hipotensão, impactando a medicação do paciente.",
                },
            }
        ],
    },
}

# ==========================================================
# INTERFACE STREAMLIT - ESTRUTURA DE TABS
# ==========================================================

# Header
st.markdown(
    """
<div class="hero">
    <h1>🩺 Engenharia Clínica — Guia Técnico V5</h1>
    <p>Manutenção Preventiva, Corretiva, Princípios Físicos e Manuais Práticos de Reparo (Padrão iFixit Medical)</p>
</div>
""",
    unsafe_allow_html=True,
)

# Seleção do Equipamento no Topo/Sidebar
equip_selecionado = st.sidebar.selectbox(
    "🔬 Selecione o Equipamento Médico:", list(EQUIPAMENTOS.keys())
)

dados_eq = EQUIPAMENTOS[equip_selecionado]

# Navegação Principal por Abas
tab_conceito, tab_hardware, tab_problemas, tab_passo_a_passo, tab_ifixit = (
    st.tabs(
        [
            "🧠 Princípio & Lógica",
            "🧩 Hardware & Componentes",
            "⚠️ Mapeamento de Defeitos",
            "🛠️ Guia Técnico de Reparo Step-by-Step",
            "📚 Integração iFixit & Documentação",
        ]
    )
)

# ----------------------------------------------------------
# TAB 1: PRINCIPIO E LOGICA
# ----------------------------------------------------------
with tab_conceito:
    st.header(f"Princípio de Funcionamento: {equip_selecionado}")
    st.caption(f"Tipo: {dados_eq['tipo']}")

    st.markdown(
        f"<div class='concept'>{dados_eq['objetivo']}</div>",
        unsafe_allow_html=True,
    )

    st.subheader("💡 Raciocínio Clínico e Físico de Diagnóstico")
    col1, col2 = st.columns(2)
    for i, (titulo, desc) in enumerate(dados_eq["raciocinio"]):
        with col1 if i % 2 == 0 else col2:
            st.info(f"**{titulo}**\n\n{desc}")

    st.markdown(dados_eq["principio"])

    if "interferencia" in dados_eq:
        st.markdown(dados_eq["interferencia"])

# ----------------------------------------------------------
# TAB 2: HARDWARE E COMPONENTES
# ----------------------------------------------------------
with tab_hardware:
    st.header(f"Anatomia de Hardware e Subsistemas: {equip_selecionado}")
    st.write(
        "Avaliação estrutural de componentes críticos para isolamento de falhas:"
    )

    df_comp = pd.DataFrame(
        dados_eq["componentes"],
        columns=["Componente / Subsistema", "Função Técnica", "Modo de Falha Comum"],
    )
    st.dataframe(df_comp, use_container_width=True, hide_index=True)

# ----------------------------------------------------------
# TAB 3: MAPEAMENTO DE DEFEITOS
# ----------------------------------------------------------
with tab_problemas:
    st.header(f"Sintomas, Cadeia Térmica/Elétrica e Causas Raiz")

    for prob in dados_eq["problemas"]:
        with st.expander(f"🔴 Defeito: {prob['titulo']}", expanded=True):
            st.write(f"**Sintoma Clínico:** {prob['sintoma']}")
            st.write(f"**Cadeia Funcional:** `{prob['cadeia']}`")

            st.subheader("Possíveis Causas Raiz:")
            for c in prob["causas"]:
                st.markdown(f"- {c}")

            st.subheader("Passos Diagnósticos Iniciais:")
            for p in prob["passos_diagnostico"]:
                st.markdown(f"1. {p}")

# ----------------------------------------------------------
# TAB 4: GUIA TECNICO DE REPARO PASSO A PASSO (NOVA ABA REQUISITADA)
# ----------------------------------------------------------
with tab_passo_a_passo:
    st.header(
        f"🛠️ Manual Técnico de Intervenção e Reparo Passo a Passo — {equip_selecionado}"
    )
    st.write(
        "Procedimentos operacionais padrão (POP) focados em resolução física, substituição e calibração de componentes."
    )

    tem_guia = False
    for prob in dados_eq["problemas"]:
        if "guia_reparo_passo_a_passo" in prob:
            tem_guia = True
            guia = prob["guia_reparo_passo_a_passo"]

            st.markdown(
                f"--- \n### 🔧 Procedimento de Reparo para: *{prob['titulo']}*"
            )

            # Dashboard de Informações do Reparo
            m1, m2 = st.columns(2)
            m1.metric("Nível de Dificuldade Técnico", guia["dificuldade"])
            m2.metric("Componente Alvo", prob["titulo"].split()[-1].capitalize())

            st.markdown(
                f"<div class='danger-box'><b>⚡ AVISO CRÍTICO DE SEGURANÇA E BPF:</b><br>{guia['seguranca']}</div>",
                unsafe_allow_html=True,
            )

            col_ferramentas, col_passos = st.columns([1, 2])

            with col_ferramentas:
                st.subheader("🧰 Ferramental & Insumos")
                for f in guia["ferramentas"]:
                    st.markdown(f"- {f}")

            with col_passos:
                st.subheader("📋 Roteiro de Execução Passo a Passo")
                for passo in guia["passos"]:
                    st.markdown(f"{passo}")
                    st.markdown("---")

    if not tem_guia:
        st.warning(
            "Selecione um equipamento com guia de instrução direta técnica disponível no menu lateral."
        )

# ----------------------------------------------------------
# TAB 5: INTEGRAÇÃO IFIXIT & DOCUMENTAÇÃO
# ----------------------------------------------------------
with tab_ifixit:
    st.header("📚 Referências do iFixit Medical Device e Manuais Técnicos")
    st.markdown(
        """
    O repositório **iFixit Medical Device Project** é uma plataforma comunitária aberta de direito ao reparo (Right to Repair) 
    que centraliza manuais de serviço, guias de desmontagem e solução de problemas para equipamentos médicos de diversas marcas.
    """
    )

    st.markdown(
        """
    <div class='tech-box'>
        <h4>🔗 Link Direto para o Portal iFixit Medical:</h4>
        <p>Acesse os manuais originais de serviço e guias fotográficos desmontagem:</p>
        <a href="https://pt.ifixit.com/Device/Medical_Device" target="_blank" style="color: #38bdf8; font-weight: bold; font-size: 1.1rem;">
            🌐 https://pt.ifixit.com/Device/Medical_Device
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("💡 Como Utilizar o Padrão iFixit em Ambientes Hospitalares:")
    st.markdown(
        """
    1. **Identificação Amostral por Fotos:** Utilize a documentação visual do iFixit para verificar a localização exata de fusíveis internos, placas SMD e conectores pneumáticos antes da desmontagem.
    2. **Ordem de Parafusos e Torques:** Siga o padrão iFixit organizando os parafusos retirados em organizadores magnéticos por tamanho e tipo (Torx, Phillips, Hexagonal) para evitar perfurações em placas de circuito.
    3. **Proteção ESD (Descarga Eletrostática):** Sempre utilize pulseira ou manta antiestática com cabo de aterramento ao manusear placas mães e controladores de equipamentos médicos.
    4. **Validação de Segurança Pós-Reparo (NBR IEC 60601-1):** Qualquer substituição de componente listada nos guias DEVE obrigatoriamente ser seguida por um ensaio de segurança elétrica (medindo correntes de fuga no chassis e partes aplicadas).
    """
    )

# Sidebar - Footer Info
st.sidebar.markdown("---")
st.sidebar.caption("Engenharia Clínica V5 | Padrão iFixit Medical Manual")
st.sidebar.caption("Foco em Resolução Prática de Campo")
