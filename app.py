import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Engenharia Clínica | Guia de Campo",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# CONFIGURAÇÃO
# =========================================================
EQUIPAMENTOS = {
    "♨️ Autoclave": {
        "imagem": None,  # Adicione um caminho local, ex.: "images/autoclave.jpg"
        "subtitulo": "Esterilização por vapor sob pressão",
        "descricao": """
A autoclave é um equipamento utilizado para **esterilizar artigos e materiais por calor úmido**, utilizando vapor em condições controladas de temperatura, tempo e, conforme o equipamento, pressão e remoção de ar.

Em ambientes como **odontologia, enfermagem, CME e serviços de saúde**, ela é utilizada para o processamento de artigos compatíveis com o método, contribuindo para a prevenção de transmissão de microrganismos e infecções relacionadas à assistência.

⚠️ **Importante:** a arquitetura e o ciclo variam conforme marca, modelo e aplicação. Uma autoclave compacta de bancada não possui necessariamente bomba de vácuo, osmose reversa ou gerador de vapor separado.
""",
        "principio": """
### Como a esterilização ocorre?

O processo depende da transferência de calor pelo vapor. A eficácia não é explicada apenas por “alta temperatura”: o resultado depende da combinação correta entre **temperatura, tempo, qualidade do vapor, remoção de ar e contato adequado com a carga**.

Em termos microbiológicos, o aumento da temperatura acelera a inativação dos microrganismos. Por isso, os ciclos são definidos e validados para atingir determinadas condições.

### Visão simplificada do processo

**Água / alimentação de vapor → geração ou entrada de vapor → remoção de ar → exposição da carga → manutenção das condições do ciclo → exaustão/despressurização → secagem, quando aplicável.**
""",
        "ciclo": [
            {
                "fase": "1. Condicionamento da carga",
                "texto": """O objetivo é preparar a câmara e a carga para a esterilização, principalmente reduzindo a presença de ar que pode dificultar o contato do vapor com as superfícies.

Em autoclaves com pré-vácuo, a remoção de ar pode ocorrer por pulsos de vácuo. Em outros equipamentos, pode existir deslocamento gravitacional do ar. Portanto, **o método depende do tipo de autoclave**."""
            },
            {
                "fase": "2. Esterilização / Exposição",
                "texto": """Após atingir as condições programadas e validadas, inicia-se o período de exposição. A carga permanece durante o tempo previsto sob as condições definidas pelo ciclo."""
            },
            {
                "fase": "3. Exaustão e secagem",
                "texto": """Após a exposição, o vapor é removido e ocorre redução de pressão. Em equipamentos com secagem por vácuo, uma bomba de vácuo pode ajudar a remover vapor e umidade.

Quando o vapor entra em contato com uma carga mais fria, parte dele condensa. A secagem adequada depende do projeto do equipamento e do ciclo."""
            }
        ],
        "componentes": [
            ("Câmara", "Local onde a carga é processada; deve suportar as condições de temperatura e pressão previstas."),
            ("Sistema de aquecimento / gerador de vapor", "Fornece energia térmica ou vapor para o ciclo."),
            ("Resistência elétrica", "Converte energia elétrica em calor, quando presente no sistema."),
            ("Sensor de temperatura", "Fornece ao sistema de controle a informação de temperatura."),
            ("Sensor/transdutor de pressão", "Monitora a pressão quando aplicável ao projeto."),
            ("Porta e sistema de travamento", "Mantêm a câmara fechada e ajudam a impedir abertura em condição insegura."),
            ("Gaxeta / borracha de vedação", "Promove vedação entre porta e câmara."),
            ("Válvulas", "Controlam entrada, saída ou alívio de fluidos e vapor."),
            ("Bomba d'água", "Pode alimentar água ao sistema, dependendo do modelo."),
            ("Bomba de vácuo", "Pode remover ar e auxiliar na secagem; não existe em todos os modelos."),
            ("Microcontrolador / placa eletrônica", "Executa a lógica do ciclo e recebe sinais dos sensores."),
            ("Sistema de segurança", "Pode incluir travamento, proteção térmica, válvula de segurança e outras proteções.")
        ],
        "problemas": [
            {
                "titulo": "Não liga",
                "sintoma": "Painel apagado ou ausência completa de resposta.",
                "causas": [
                    "Ausência de alimentação elétrica",
                    "Cabo, tomada ou disjuntor",
                    "Fusível ou proteção aberta",
                    "Falha na fonte ou placa eletrônica"
                ],
                "passos": [
                    "Descrever exatamente o sintoma antes de desmontar.",
                    "Verificar a alimentação externa e o procedimento seguro da instituição.",
                    "Inspecionar cabo, plugue e sinais visíveis de dano.",
                    "Verificar proteções acessíveis conforme manual técnico.",
                    "Se a alimentação estiver correta, investigar a cadeia de alimentação interna conforme documentação do fabricante.",
                    "Após qualquer intervenção, realizar teste funcional e registrar o resultado."
                ],
                "alerta": "Não energize circuitos expostos e não substitua proteções por pontes."
            },
            {
                "titulo": "Liga, mas não aquece",
                "sintoma": "Painel funciona e o ciclo inicia, porém a temperatura não sobe como esperado.",
                "causas": [
                    "Falha na resistência ou no sistema de aquecimento",
                    "Conector ou fiação com mau contato",
                    "Relé/contator não acionando",
                    "Sensor ou controle impedindo o acionamento",
                    "Dispositivo de proteção térmica aberto"
                ],
                "passos": [
                    "Identificar em qual ponto do ciclo o aquecimento deveria iniciar.",
                    "Desenergizar o equipamento e aguardar resfriamento completo.",
                    "Consultar o diagrama elétrico do modelo antes de acessar componentes.",
                    "Inspecionar conectores, cabos e sinais de aquecimento anormal.",
                    "Testar os componentes pelo método previsto pelo fabricante e com instrumento adequado.",
                    "Diferenciar falha de comando (placa/relé) de falha da carga (resistência).",
                    "Após o reparo, executar validação funcional conforme o procedimento técnico."
                ],
                "alerta": "Não faça jumper em termostatos, sensores ou dispositivos de segurança como procedimento de reparo. Um componente com dois fios pode ser uma proteção crítica."
            },
            {
                "titulo": "Vazamento de vapor na porta",
                "sintoma": "Escape de vapor ou água na região da porta durante o ciclo.",
                "causas": [
                    "Gaxeta suja, ressecada, deformada ou danificada",
                    "Porta desalinhada",
                    "Pressão de fechamento desigual",
                    "Mecanismo de travamento com folga",
                    "Superfície de vedação danificada"
                ],
                "passos": [
                    "Interromper o uso e aguardar equipamento frio e sem pressão.",
                    "Localizar e registrar exatamente o ponto do vazamento.",
                    "Inspecionar a gaxeta em todo o perímetro.",
                    "Limpar apenas conforme orientação do fabricante.",
                    "Comparar o lado que vaza com o lado que veda corretamente.",
                    "Verificar alinhamento e folgas do mecanismo de fechamento.",
                    "Executar ajuste somente pelo método previsto para aquele modelo.",
                    "Executar ciclo de teste e validar ausência de vazamento conforme procedimento da empresa."
                ],
                "alerta": "Não utilizar martelo, anilhas ou deformação mecânica como solução genérica. O ajuste deve seguir o mecanismo e a especificação do fabricante."
            },
            {
                "titulo": "Vazamento sempre do mesmo lado",
                "sintoma": "O vazamento é repetitivo e localizado.",
                "causas": [
                    "Desalinhamento da porta",
                    "Pressão de fechamento não uniforme",
                    "Dobradiça ou ponto de apoio com folga",
                    "Gaxeta deformada especificamente naquela região"
                ],
                "passos": [
                    "Registrar o lado e a posição exata do vazamento.",
                    "Comparar visualmente e mecanicamente ambos os lados da porta.",
                    "Verificar o assentamento da gaxeta.",
                    "Verificar folgas e geometria do fechamento.",
                    "Consultar o procedimento técnico específico do fabricante antes de alterar anilhas, espaçadores ou dobradiças.",
                    "Após o ajuste autorizado, realizar teste completo de vedação e ciclo."
                ],
                "alerta": "Este sintoma é um indício útil, mas não prova sozinho que a porta está desalinhada."
            },
            {
                "titulo": "Não atinge a temperatura programada",
                "sintoma": "Aquece, porém o ciclo não alcança o setpoint esperado.",
                "causas": [
                    "Sistema de aquecimento com desempenho insuficiente",
                    "Alimentação elétrica inadequada",
                    "Perda de energia por vazamento",
                    "Sensor com leitura incorreta",
                    "Falha no controle"
                ],
                "passos": [
                    "Confirmar o valor programado e o comportamento real.",
                    "Verificar se há vazamentos ou perda evidente de vapor.",
                    "Analisar o histórico/tempo de subida de temperatura, se disponível.",
                    "Verificar a cadeia sensor → controle → acionamento → aquecimento.",
                    "Comparar medições apenas com instrumentos adequados e procedimentos autorizados.",
                    "Validar o ciclo após a correção."
                ],
                "alerta": "Não alterar parâmetros do ciclo para compensar uma falha técnica."
            },
            {
                "titulo": "Temperatura sobe demais / superaquecimento",
                "sintoma": "Temperatura ultrapassa o comportamento esperado ou ocorre atuação de proteção.",
                "causas": [
                    "Falha de sensor",
                    "Falha de controle",
                    "Relé travado",
                    "Problema no circuito de proteção"
                ],
                "passos": [
                    "Retirar o equipamento de operação.",
                    "Não ignorar alarmes ou proteções.",
                    "Registrar em qual momento ocorreu o desvio.",
                    "Investigar sensor, circuito de comando e elementos de proteção conforme documentação.",
                    "Após correção, validar o comportamento em ciclo controlado."
                ],
                "alerta": "Superaquecimento é uma condição de segurança. Não faça bypass de proteções."
            },
            {
                "titulo": "Ciclo interrompe ou apresenta alarme",
                "sintoma": "O processo não chega ao final ou o equipamento indica erro.",
                "causas": [
                    "Temperatura fora do esperado",
                    "Pressão fora da faixa",
                    "Falha de sensor",
                    "Falha de porta/travamento",
                    "Falha de alimentação",
                    "Erro de controle"
                ],
                "passos": [
                    "Registrar o código e o momento exato da falha.",
                    "Consultar o manual técnico específico.",
                    "Não apagar evidências antes de registrar o erro.",
                    "Separar a falha por subsistema: térmico, pressão, porta, sensor ou controle.",
                    "Executar o teste previsto pelo fabricante.",
                    "Registrar a ação corretiva e a validação."
                ],
                "alerta": "O código de erro deve ser interpretado pelo manual do modelo; códigos variam entre fabricantes."
            }
        ]
    },

    "📈 Eletrocardiógrafo": {
        "imagem": None,
        "subtitulo": "Aquisição e registro de sinais bioelétricos cardíacos",
        "descricao": """
O eletrocardiógrafo registra diferenças de potencial elétrico associadas à atividade cardíaca por meio de eletrodos posicionados no paciente.

O equipamento precisa captar sinais pequenos, rejeitar ruídos e apresentar o traçado com amplitude e velocidade adequadas. Por isso, cabos, eletrodos, contato com a pele, filtros, aterramento e o próprio circuito de aquisição podem influenciar o resultado.
""",
        "principio": """
**Paciente → eletrodos → cabo do paciente → proteção/isolação → amplificação diferencial → filtragem → conversão/processamento → display/impressão.**

O diagnóstico de um traçado alterado deve separar **artefato externo, problema de contato, cabo/eletrodo e falha interna do equipamento**.
""",
        "ciclo": [
            {"fase": "1. Captação", "texto": "Os eletrodos captam diferenças de potencial na superfície corporal."},
            {"fase": "2. Condicionamento", "texto": "O sinal é protegido, amplificado e filtrado."},
            {"fase": "3. Processamento", "texto": "O sinal é digitalizado e processado."},
            {"fase": "4. Registro", "texto": "O traçado é exibido ou impresso."}
        ],
        "componentes": [
            ("Eletrodos", "Interface elétrica entre paciente e sistema."),
            ("Cabo do paciente", "Conduz os sinais até a entrada do equipamento."),
            ("Amplificador de instrumentação", "Amplifica sinais diferenciais de pequena amplitude."),
            ("Filtros", "Reduzem determinadas interferências."),
            ("Sistema de isolação", "Ajuda a garantir segurança elétrica do paciente."),
            ("Conversor e processador", "Digitalizam e processam o sinal."),
            ("Display/impressora", "Apresentam o traçado.")
        ],
        "problemas": [
            {
                "titulo": "Traçado com muito ruído",
                "sintoma": "Linha com interferência excessiva.",
                "causas": ["Mau contato dos eletrodos", "Movimento", "Cabos danificados", "Interferência elétrica", "Problema de aterramento"],
                "passos": [
                    "Identificar o tipo de ruído.",
                    "Verificar preparação e contato dos eletrodos.",
                    "Inspecionar cabos e conectores.",
                    "Afastar fontes óbvias de interferência e comparar o ambiente.",
                    "Testar com simulador de ECG quando disponível.",
                    "Se o defeito persistir com simulador, investigar o equipamento."
                ],
                "alerta": "Não concluir que a bancada metálica ou o transformador são a causa sem teste controlado."
            },
            {
                "titulo": "Amplitude aparentemente incorreta",
                "sintoma": "Ondas muito altas, muito baixas ou comportamento desregulado.",
                "causas": ["Configuração de ganho", "Artefato", "Falha de aquisição", "Problema de cabo", "Interferência"],
                "passos": [
                    "Conferir ganho e configuração.",
                    "Comparar com um simulador de ECG.",
                    "Comparar com outro equipamento sob condições controladas.",
                    "Trocar uma variável por vez: cabo, tomada, ambiente ou superfície.",
                    "Registrar se todas as derivações são afetadas.",
                    "Investigar internamente somente após isolar causas externas."
                ],
                "alerta": "Uma bancada metálica pode ser parte do ambiente eletromagnético, mas não deve ser assumida como causa sem evidência."
            },
            {
                "titulo": "Sem sinal em uma derivação",
                "sintoma": "Uma ou mais derivações não apresentam traçado adequado.",
                "causas": ["Eletrodo", "Conexão", "Via rompida no cabo", "Entrada do equipamento"],
                "passos": [
                    "Verificar eletrodo e posicionamento.",
                    "Inspecionar conector correspondente.",
                    "Comparar com cabo conhecido em boas condições.",
                    "Testar com simulador, se disponível.",
                    "Seguir o manual técnico para diagnóstico da entrada."
                ],
                "alerta": "Evite medir ou injetar sinais em entradas de paciente sem procedimento e equipamento de teste apropriados."
            }
        ]
    },

    "❄️ Câmara fria / Câmara de vacina": {
        "imagem": None,
        "subtitulo": "Controle e monitoramento de temperatura",
        "descricao": """
Esses equipamentos são utilizados para manter produtos sensíveis dentro de condições térmicas específicas. Em uma câmara de vacina, não basta “estar gelando”: é necessário manter a temperatura dentro da faixa definida para o produto e garantir monitoramento confiável.

O projeto pode incluir controlador eletrônico, sensores, compressor, evaporador, condensador, ventiladores, alarmes, bateria e registro de temperatura.
""",
        "principio": """
**Sensor detecta temperatura → controlador compara com o setpoint → sistema de refrigeração é acionado → calor é removido da câmara → controlador monitora continuamente.**
""",
        "ciclo": [
            {"fase": "1. Leitura", "texto": "O sensor mede a temperatura."},
            {"fase": "2. Decisão", "texto": "O controlador compara a medição com a faixa configurada."},
            {"fase": "3. Refrigeração", "texto": "O compressor e demais componentes removem calor."},
            {"fase": "4. Monitoramento", "texto": "Alarmes e registros acompanham o comportamento."}
        ],
        "componentes": [
            ("Compressor", "Comprime e movimenta o refrigerante no ciclo."),
            ("Condensador", "Rejeita calor para o ambiente."),
            ("Dispositivo de expansão", "Reduz a pressão do refrigerante."),
            ("Evaporador", "Absorve calor do ambiente interno."),
            ("Ventilador", "Ajuda na circulação de ar, quando presente."),
            ("Sensor", "Mede temperatura."),
            ("Controlador", "Controla refrigeração e alarmes."),
            ("Gaxeta da porta", "Reduz entrada de calor e umidade.")
        ],
        "problemas": [
            {
                "titulo": "Temperatura acima da faixa",
                "sintoma": "Temperatura interna sobe ou não retorna ao setpoint.",
                "causas": ["Porta aberta", "Gaxeta defeituosa", "Condensador obstruído", "Falha de ventilação", "Falha de compressor", "Sensor/controlador"],
                "passos": [
                    "Verificar imediatamente o protocolo da instituição para proteção do conteúdo.",
                    "Confirmar leitura com método de referência autorizado.",
                    "Verificar porta e vedação.",
                    "Inspecionar circulação de ar e obstrução externa.",
                    "Registrar histórico de temperatura.",
                    "Investigar refrigeração e controle conforme procedimento técnico."
                ],
                "alerta": "Em câmaras com produtos críticos, a prioridade é proteger o conteúdo e seguir o procedimento institucional."
            },
            {
                "titulo": "Formação excessiva de gelo",
                "sintoma": "Acúmulo anormal de gelo no evaporador ou interior.",
                "causas": ["Entrada de umidade", "Vedação deficiente", "Problema de degelo", "Sensor/controlador"],
                "passos": [
                    "Verificar a frequência de abertura da porta.",
                    "Inspecionar gaxeta.",
                    "Consultar o método de degelo previsto.",
                    "Não remover gelo com objetos que possam perfurar componentes.",
                    "Investigar sistema de degelo conforme o modelo."
                ],
                "alerta": "Nunca perfure gelo próximo ao evaporador."
            }
        ]
    },

    "💨 Compressor": {
        "imagem": None,
        "subtitulo": "Geração e armazenamento de ar comprimido",
        "descricao": """
O compressor transforma energia elétrica em energia pneumática. Um conjunto de compressão aspira ar e aumenta sua pressão, armazenando-o em um reservatório ou fornecendo-o ao sistema.

Em aplicações odontológicas, a qualidade do ar — incluindo limpeza, umidade e presença de contaminantes — é importante para o equipamento atendido.
""",
        "principio": """
**Motor → mecanismo de compressão → aumento da pressão → reservatório → pressostato controla liga/desliga → ar segue para o sistema.**
""",
        "ciclo": [
            {"fase": "1. Aspiração", "texto": "O ar é admitido."},
            {"fase": "2. Compressão", "texto": "O mecanismo reduz o volume e eleva a pressão."},
            {"fase": "3. Armazenamento", "texto": "O ar pode ser armazenado no reservatório."},
            {"fase": "4. Controle", "texto": "O pressostato controla o funcionamento conforme pressão."}
        ],
        "componentes": [
            ("Motor", "Fornece energia mecânica."),
            ("Cabeçote/pistão", "Comprime o ar."),
            ("Reservatório", "Armazena ar pressurizado."),
            ("Pressostato", "Controla o acionamento conforme pressão."),
            ("Manômetro", "Indica pressão."),
            ("Válvula de retenção", "Evita retorno do ar."),
            ("Válvula de segurança", "Protege contra sobrepressão."),
            ("Filtro", "Reduz entrada de partículas."),
            ("Purgador", "Permite remoção de condensado.")
        ],
        "problemas": [
            {
                "titulo": "Não liga",
                "sintoma": "Motor não inicia.",
                "causas": ["Sem alimentação", "Pressostato", "Proteção térmica", "Capacitor", "Motor"],
                "passos": [
                    "Verificar alimentação.",
                    "Registrar se há ruído, aquecimento ou tentativa de partida.",
                    "Verificar pressão atual e condição do pressostato.",
                    "Seguir o procedimento técnico para teste do circuito de partida.",
                    "Validar o acionamento após correção."
                ],
                "alerta": "Reservatórios pressurizados exigem procedimento seguro antes de qualquer intervenção."
            },
            {
                "titulo": "Enche muito lentamente",
                "sintoma": "Demora maior que o normal para atingir pressão.",
                "causas": ["Vazamento", "Filtro obstruído", "Desgaste do conjunto de compressão", "Válvula"],
                "passos": [
                    "Comparar o tempo de enchimento com a referência do equipamento.",
                    "Inspecionar conexões e possíveis vazamentos.",
                    "Verificar filtro de admissão.",
                    "Investigar válvulas e conjunto de compressão conforme manual.",
                    "Validar pressão de corte e tempo de recuperação."
                ],
                "alerta": "Não exceda a pressão nominal durante testes."
            }
        ]
    },

    "🦷 Cadeira e caneta odontológica": {
        "imagem": None,
        "subtitulo": "Sistema integrado eletromecânico, hidráulico e pneumático",
        "descricao": """
Uma cadeira odontológica pode integrar movimentação mecânica ou eletro-hidráulica, comandos elétricos, água, ar comprimido, iluminação e instrumentos.

O diagnóstico fica mais fácil quando o sistema é separado em subsistemas: **elétrico, pneumático, hidráulico e mecânico**.
""",
        "principio": """
**Comando → placa/controle → atuador ou válvula → movimento/fluxo → retorno de sensores ou fim de curso, conforme o projeto.**
""",
        "ciclo": [
            {"fase": "1. Comando", "texto": "Botão ou pedal solicita uma função."},
            {"fase": "2. Controle", "texto": "A placa ou circuito interpreta o comando."},
            {"fase": "3. Acionamento", "texto": "Motor, atuador ou válvula é acionado."},
            {"fase": "4. Resultado", "texto": "A cadeira ou instrumento executa o movimento/função."}
        ],
        "componentes": [
            ("Placa de comando", "Gerencia comandos."),
            ("Pedal", "Envia comandos ao sistema."),
            ("Motor/atuador", "Produz movimento."),
            ("Fim de curso", "Indica limite de movimento, quando presente."),
            ("Mangueiras", "Conduzem ar ou água."),
            ("Válvulas", "Controlam fluxo."),
            ("Regulador", "Ajusta pressão.")
        ],
        "problemas": [
            {
                "titulo": "Cadeira não sobe ou desce",
                "sintoma": "Movimento não ocorre.",
                "causas": ["Sem comando", "Falha de alimentação", "Fim de curso", "Placa", "Motor/atuador", "Travamento mecânico"],
                "passos": [
                    "Identificar se nenhum movimento funciona ou apenas um.",
                    "Verificar comando/pedal.",
                    "Verificar alimentação e proteções.",
                    "Observar se existe ruído de acionamento.",
                    "Separar falha elétrica de travamento mecânico.",
                    "Consultar esquema específico antes de medir na placa."
                ],
                "alerta": "Não apoiar ou trabalhar sob partes móveis sem travamento mecânico adequado."
            },
            {
                "titulo": "Caneta não gira ou tem baixa potência",
                "sintoma": "Instrumento não atinge funcionamento esperado.",
                "causas": ["Pressão inadequada", "Mangueira", "Conexão", "Turbina/motor", "Desgaste interno"],
                "passos": [
                    "Confirmar se o problema ocorre em uma ou mais posições.",
                    "Verificar fornecimento de ar conforme especificação.",
                    "Inspecionar mangueira e conexão.",
                    "Testar com instrumento conhecido em boas condições, quando permitido.",
                    "Encaminhar componente interno para manutenção conforme fabricante."
                ],
                "alerta": "Não exceda pressão especificada pelo fabricante."
            }
        ]
    },

    "🔊 Ultrassom odontológico": {
        "imagem": None,
        "subtitulo": "Vibração ultrassônica para procedimentos odontológicos",
        "descricao": """
O ultrassom odontológico utiliza um circuito eletrônico para excitar um transdutor, que converte energia elétrica em vibração mecânica de alta frequência.

Dependendo da tecnologia, o equipamento pode utilizar transdutores piezoelétricos ou magnetoestritivos. Portanto, frequência, construção e diagnóstico variam conforme o modelo.
""",
        "principio": """
**Energia elétrica → gerador eletrônico → transdutor → vibração mecânica → ponta/inserto.**

O sistema de água auxilia o procedimento e pode participar do resfriamento.
""",
        "ciclo": [
            {"fase": "1. Comando", "texto": "O operador aciona pedal ou comando."},
            {"fase": "2. Geração", "texto": "O circuito gera sinal adequado ao transdutor."},
            {"fase": "3. Conversão", "texto": "O transdutor produz vibração mecânica."},
            {"fase": "4. Irrigação", "texto": "O sistema de água atua conforme o equipamento."}
        ],
        "componentes": [
            ("Placa eletrônica", "Gera e controla o sinal."),
            ("Transdutor", "Converte energia elétrica em vibração."),
            ("Caneta", "Transmite a vibração."),
            ("Inserto/ponta", "Elemento ativo no procedimento."),
            ("Pedal", "Aciona o funcionamento."),
            ("Sistema de água", "Fornece irrigação.")
        ],
        "problemas": [
            {
                "titulo": "Sem vibração",
                "sintoma": "Ponta não apresenta funcionamento.",
                "causas": ["Inserto inadequado", "Cabo", "Transdutor", "Placa", "Pedal"],
                "passos": [
                    "Confirmar alimentação e comando.",
                    "Verificar encaixe e compatibilidade do inserto.",
                    "Comparar com caneta/acessório conhecido em boas condições quando permitido.",
                    "Inspecionar cabo e conectores.",
                    "Investigar circuito e transdutor conforme manual técnico."
                ],
                "alerta": "Não operar ponta sem condições adequadas de irrigação quando o procedimento exigir."
            },
            {
                "titulo": "Sem água",
                "sintoma": "Não há irrigação adequada.",
                "causas": ["Registro fechado", "Obstrução", "Mangueira", "Válvula/bomba"],
                "passos": [
                    "Verificar nível/fonte de água.",
                    "Verificar regulagem.",
                    "Inspecionar mangueira.",
                    "Verificar obstruções pelo método autorizado.",
                    "Investigar válvula ou bomba conforme o modelo."
                ],
                "alerta": "Não utilizar objetos improvisados que possam danificar orifícios ou componentes."
            }
        ]
    },

    "🔍 Colposcópio": {
        "imagem": None,
        "subtitulo": "Sistema óptico de ampliação e iluminação",
        "descricao": """
O colposcópio permite observação ampliada e iluminada de estruturas anatômicas. Dependendo do modelo, pode possuir sistema óptico binocular, câmera, captura digital e diferentes fontes de iluminação.

O diagnóstico deve separar **óptica, iluminação, alimentação e mecânica**.
""",
        "principio": """
**Fonte de luz → iluminação do campo → sistema óptico/câmera → ampliação → observação ou captura de imagem.**
""",
        "ciclo": [
            {"fase": "1. Alimentação", "texto": "O sistema recebe energia."},
            {"fase": "2. Iluminação", "texto": "A fonte ilumina o campo."},
            {"fase": "3. Óptica", "texto": "Lentes formam a imagem ampliada."},
            {"fase": "4. Ajuste", "texto": "Foco e ampliação são configurados."}
        ],
        "componentes": [
            ("Fonte de luz", "Ilumina o campo."),
            ("Lentes", "Formam e ampliam a imagem."),
            ("Sistema de foco", "Ajusta nitidez."),
            ("Braço articulado", "Permite posicionamento."),
            ("Câmera, quando presente", "Realiza captura digital."),
            ("Fonte de alimentação", "Fornece energia.")
        ],
        "problemas": [
            {
                "titulo": "Imagem sem foco",
                "sintoma": "Imagem permanece desfocada.",
                "causas": ["Ajuste de foco", "Lente suja", "Problema mecânico/óptico"],
                "passos": [
                    "Verificar ajuste e distância de trabalho.",
                    "Inspecionar lentes.",
                    "Utilizar apenas material de limpeza recomendado.",
                    "Se persistir, encaminhar para avaliação óptica."
                ],
                "alerta": "Não utilizar produtos ou tecidos inadequados em superfícies ópticas."
            },
            {
                "titulo": "Iluminação não funciona",
                "sintoma": "Luz apagada ou instável.",
                "causas": ["Fonte", "LED/lâmpada", "Driver", "Cabo", "Controle de intensidade"],
                "passos": [
                    "Verificar alimentação.",
                    "Registrar se a falha é total ou intermitente.",
                    "Verificar componente de iluminação conforme manual.",
                    "Inspecionar conectores.",
                    "Validar intensidade e estabilidade após correção."
                ],
                "alerta": "Fontes internas podem permanecer energizadas mesmo após desligamento; siga o procedimento do fabricante."
            }
        ]
    }
}


# =========================================================
# FUNÇÕES
# =========================================================
def mostrar_imagem(info):
    if info.get("imagem"):
        st.image(info["imagem"], use_container_width=True)
    else:
        st.info(
            "📷 **Imagem do equipamento:** adicione uma foto na pasta `images/` "
            "e informe o caminho correspondente no campo `imagem`."
        )


def mostrar_componentes(componentes):
    st.dataframe(
        [{"Componente": nome, "Função": funcao} for nome, funcao in componentes],
        use_container_width=True,
        hide_index=True
    )


def mostrar_problemas(problemas):
    st.subheader("🛠️ Biblioteca de problemas e soluções")
    st.caption("Use como roteiro de investigação. A intervenção deve seguir manual técnico, treinamento e autorização aplicáveis.")

    termo = st.text_input(
        "🔎 Procurar problema, sintoma ou causa",
        placeholder="Ex.: não aquece, vazamento, ruído..."
    ).lower()

    encontrados = 0

    for problema in problemas:
        texto_busca = (
            problema["titulo"] + " " +
            problema["sintoma"] + " " +
            " ".join(problema["causas"])
        ).lower()

        if not termo or termo in texto_busca:
            encontrados += 1

            with st.expander(f"⚠️ {problema['titulo']}", expanded=False):
                st.error(f"**Sintoma:** {problema['sintoma']}")

                st.markdown("#### 🔍 Possíveis causas")
                for causa in problema["causas"]:
                    st.markdown(f"- {causa}")

                st.markdown("#### 🧭 Roteiro passo a passo")
                for i, passo in enumerate(problema["passos"], 1):
                    st.markdown(f"**{i}.** {passo}")

                st.warning(f"⚠️ **Atenção:** {problema['alerta']}")

    if encontrados == 0:
        st.info("Nenhum problema encontrado. Tente outro termo.")


def mostrar_fluxo_autoclave():
    st.subheader("🌳 Fluxo mental de diagnóstico")

    st.code("""
[ EQUIPAMENTO COM FALHA ]
            |
            v
[ Qual é o sintoma? ]
            |
    +-------+--------+---------+
    |       |        |         |
 Não liga  Não      Vaza    Ciclo/
           aquece            alarme
    |       |        |         |
 Elétrico  Aquec.   Porta/   Identificar
           Controle Vedação  etapa do ciclo
    |       |        |         |
 Testar    Separar  Localizar Consultar
 cadeia    comando  ponto     código/manual
           x carga  e causa
            |
            v
[ Corrigir somente após confirmar a hipótese ]
            |
            v
[ Validar funcionamento e registrar ]
""", language="text")


def pagina_equipamento(nome, info):
    st.title(nome)
    st.caption(info["subtitulo"])

    mostrar_imagem(info)

    tabs = st.tabs([
        "📚 Entender o equipamento",
        "⚙️ Componentes",
        "🔄 Funcionamento",
        "🛠️ Problemas e soluções",
        "🌳 Diagnóstico"
    ])

    with tabs[0]:
        st.subheader("O que é e para que serve?")
        st.markdown(info["descricao"])

        st.subheader("Princípio de funcionamento")
        st.markdown(info["principio"])

    with tabs[1]:
        st.subheader("Principais componentes")
        mostrar_componentes(info["componentes"])

    with tabs[2]:
        st.subheader("Funcionamento passo a passo")
        for etapa in info["ciclo"]:
            with st.expander(etapa["fase"], expanded=True):
                st.write(etapa["texto"])

    with tabs[3]:
        mostrar_problemas(info["problemas"])

    with tabs[4]:
        if nome == "♨️ Autoclave":
            mostrar_fluxo_autoclave()
        else:
            st.markdown("""
### Método universal

**1. Confirmar o sintoma → 2. Identificar a etapa de funcionamento → 3. Separar o equipamento em subsistemas → 4. Começar por verificações simples → 5. Testar uma hipótese por vez → 6. Corrigir → 7. Validar → 8. Registrar.**

#### Perguntas-chave

- O problema é reproduzível?
- Quando ele aparece?
- O que ainda funciona?
- O que mudou?
- Existe outro equipamento para comparação?
- Posso testar com simulador ou instrumento apropriado?
- O defeito está no ambiente, no acessório ou no equipamento?
""")


# =========================================================
# APP
# =========================================================
st.sidebar.title("🩺 Engenharia Clínica")
st.sidebar.caption("Guia de estudo e campo")

menu = st.sidebar.radio(
    "Navegação",
    ["🏠 Início", *EQUIPAMENTOS.keys(), "📝 Registro de ocorrência", "📚 Metodologia"]
)

st.sidebar.divider()
st.sidebar.info("""
⚠️ **Uso profissional**

Este app é um guia de estudo e apoio ao diagnóstico.

Sempre priorize:
- Manual do fabricante
- Procedimento da empresa
- Segurança
- Rastreabilidade
- Validação após intervenção
""")

if menu == "🏠 Início":
    st.title("🩺 Guia Prático de Engenharia Clínica")
    st.markdown("""
Este aplicativo foi pensado para funcionar como um **manual de bolso**, mas sem transformar manutenção em uma simples lista de “troque esta peça”.

A ideia central é desenvolver seu raciocínio técnico:

> **Sintoma → Sistema envolvido → Hipóteses → Testes → Confirmação → Correção autorizada → Validação**

### Como usar no dia a dia

**1. Escolha o equipamento**  
Leia primeiro a finalidade e o princípio de funcionamento.

**2. Entenda os componentes**  
Antes de procurar defeitos, saiba a função de cada componente.

**3. Abra a biblioteca de problemas**  
Pesquise pelo sintoma observado.

**4. Siga o roteiro de investigação**  
Comece por verificações simples e isole uma variável por vez.

**5. Registre a ocorrência**  
Anote equipamento, sintoma, causa confirmada e ação realizada.
""")

    st.subheader("📊 Equipamentos disponíveis")
    cols = st.columns(2)
    for i, (nome, info) in enumerate(EQUIPAMENTOS.items()):
        with cols[i % 2]:
            st.markdown(f"### {nome}")
            st.write(info["subtitulo"])

elif menu == "📚 Metodologia":
    st.title("📚 Metodologia universal de manutenção")

    st.markdown("""
## 1. Não comece desmontando

Primeiro pergunte:

- O que exatamente aconteceu?
- Quando começou?
- O defeito acontece sempre?
- Em qual etapa ele aparece?

## 2. Identifique o subsistema

Exemplos:

- **Não aquece** → sistema térmico + comando
- **Vaza** → vedação + mecânica + pressão
- **Não liga** → alimentação + proteção + controle
- **Sinal com ruído** → paciente/acessório + ambiente + aquisição

## 3. Mude uma variável por vez

Em um ECG com interferência, por exemplo:

- mesmo equipamento, outro ambiente;
- mesmo ambiente, outra tomada;
- mesmo equipamento, outro cabo;
- teste com simulador.

Assim você evita conclusões falsas.

## 4. Não confunda hipótese com diagnóstico

“Pode ser a resistência” é uma hipótese.

“Foi confirmada falha na resistência pelo teste previsto” é um diagnóstico técnico.

## 5. Validação faz parte da manutenção

A manutenção só termina depois de confirmar:

- funcionamento;
- segurança;
- desempenho;
- ausência do defeito;
- registro da intervenção.
""")

elif menu == "📝 Registro de ocorrência":
    st.title("📝 Registro rápido de ocorrência")

    with st.form("registro"):
        equipamento = st.selectbox("Equipamento", list(EQUIPAMENTOS.keys()))
        patrimonio = st.text_input("Patrimônio / identificação")
        local = st.text_input("Local")
        sintoma = st.text_area("Sintoma observado")
        etapa = st.selectbox(
            "Etapa em que ocorre",
            ["Não identificado", "Inicialização", "Funcionamento", "Durante o ciclo", "Finalização"]
        )
        hipotese = st.text_area("Hipótese inicial")
        teste = st.text_area("Teste realizado")
        resultado = st.text_area("Resultado")
        acao = st.text_area("Ação realizada / encaminhamento")
        status = st.selectbox("Status", ["Em análise", "Resolvido", "Encaminhado", "Aguardando peça"])
        enviar = st.form_submit_button("Salvar na sessão")

    if enviar:
        registro = {
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Equipamento": equipamento,
            "Patrimônio": patrimonio,
            "Local": local,
            "Sintoma": sintoma,
            "Etapa": etapa,
            "Hipótese": hipotese,
            "Teste": teste,
            "Resultado": resultado,
            "Ação": acao,
            "Status": status
        }

        if "registros" not in st.session_state:
            st.session_state.registros = []

        st.session_state.registros.append(registro)
        st.success("Ocorrência salva na sessão atual.")

    if st.session_state.get("registros"):
        st.subheader("Registros da sessão")
        st.dataframe(st.session_state.registros, use_container_width=True)

else:
    pagina_equipamento(menu, EQUIPAMENTOS[menu])
