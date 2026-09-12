import streamlit as st
import pandas as pd
from datetime import datetime
import json

# ==========================================================
# ENGENHARIA CLÍNICA - GUIA DE CAMPO V2
# Filosofia:
# PRINCÍPIO FÍSICO → COMPONENTE → SINTOMA → HIPÓTESE
# → TESTE → CONCLUSÃO → CORREÇÃO AUTORIZADA → VALIDAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Engenharia Clínica | Guia de Campo V5",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# ESTILO (Cores ajustadas para fundo escuro com alto contraste)
# ----------------------------------------------------------
st.markdown("""
<style>
    .hero {
        padding: 1.5rem;
        border-radius: 18px;
        background: #1e293b;
        border: 1px solid #3b82f6;
        color: #f8fafc;
        margin-bottom: 1rem;
    }
    .concept {
        padding: 1rem;
        border-left: 5px solid #3b82f6;
        background-color: #0f172a;
        border-radius: 8px;
        margin: 0.7rem 0;
        color: #f8fafc;
        border-top: 1px solid #1e293b;
        border-right: 1px solid #1e293b;
        border-bottom: 1px solid #1e293b;
    }
    .warning-box {
        padding: 1rem;
        border-left: 5px solid #f59e0b;
        background-color: #2e1000;
        border-radius: 8px;
        color: #f8fafc;
        border-top: 1px solid #1e293b;
        border-right: 1px solid #1e293b;
        border-bottom: 1px solid #1e293b;
    }
    .hero h1, .hero h2, .hero h3, .hero h4, .hero p,
    .concept h1, .concept h2, .concept h3, .concept h4, .concept p,
    .warning-box h1, .warning-box h2, .warning-box h3, .warning-box h4, .warning-box p {
        color: #f8fafc !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# BASE TÉCNICA
# ==========================================================

EQUIPAMENTOS = {

"♨️ Autoclave": {
"tipo": "Esterilização por calor úmido",
"imagem": None,
"objetivo": """
A autoclave é um equipamento utilizado para esterilizar artigos compatíveis por meio
de vapor sob condições controladas. Seu objetivo não é simplesmente “esquentar o material”.
O processo depende de uma combinação controlada de **tempo, temperatura, qualidade do vapor,
remoção de ar e contato adequado entre vapor e carga**.

Em odontologia, enfermagem e outras áreas da saúde, a esterilização adequada é uma barreira
fundamental contra a transmissão de microrganismos por instrumentos e materiais.
""",
"raciocinio": [
("1. O que precisa acontecer?",
 "O calor precisa chegar de forma adequada às superfícies da carga durante tempo suficiente."),
("2. Por que o vapor é importante?",
 "O vapor condensa ao encontrar uma superfície mais fria e transfere grande quantidade de energia térmica."),
("3. Por que o ar pode ser um problema?",
 "Bolsões de ar podem dificultar o contato eficiente do vapor com determinadas superfícies."),
("4. O que controla o processo?",
 "Sensores fornecem informações ao controlador, que decide quando aquecer, manter condições e finalizar etapas."),
("5. Como pensar em uma falha?",
 "Primeiro identifique em qual etapa o processo falha: alimentação, aquecimento, vedação, controle, sensores ou finalização.")
],
"principio": """
### Cadeia de funcionamento

**Energia elétrica → sistema de controle → aquecimento/geração de vapor →
condicionamento da câmara → exposição da carga → exaustão → secagem, quando aplicável.**

A arquitetura exata depende da marca e do modelo. Autoclaves compactas de bancada podem
funcionar de forma diferente de autoclaves hospitalares de grande porte.

⚠️ Portanto, não assuma que toda autoclave possui bomba de vácuo, osmose reversa ou
gerador de vapor separado.
""",
"componentes": [
("Câmara", "Recipiente onde a carga é processada. Deve suportar as condições térmicas e mecânicas previstas.", "Se houver problema estrutural ou perda de vedação, o ciclo pode não manter as condições necessárias."),
("Resistência / sistema de aquecimento", "Transforma energia elétrica em energia térmica.", "Se o controlador solicita aquecimento mas a temperatura não sobe, investigue a cadeia de potência e o elemento de aquecimento."),
("Sensor de temperatura", "Informa ao controlador a temperatura do sistema.", "Uma leitura incorreta pode fazer o sistema aquecer pouco, demais ou interromper o ciclo."),
("Controle eletrônico", "Executa a lógica do ciclo com base em sensores e parâmetros.", "Uma falha de controle pode parecer falha de resistência, por isso é necessário separar comando de carga."),
("Porta", "Fecha a câmara e integra o sistema de vedação.", "Desalinhamento pode produzir vazamento localizado."),
("Gaxeta", "Promove vedação entre porta e câmara.", "Sujeira, ressecamento ou deformação podem permitir fuga de vapor."),
("Trava/sistema de segurança", "Impede abertura em condições inseguras e confirma condição da porta.", "Falhas podem impedir o início do ciclo ou gerar alarmes."),
("Válvulas", "Controlam ou protegem fluxos de vapor, água e pressão, conforme o modelo.", "Obstrução ou falha pode alterar pressão e comportamento do ciclo."),
],
"problemas": [
{
"titulo":"Vazamento de vapor na porta",
"sintoma":"Escape de vapor ou água pela região da porta.",
"cadeia":"Vedação depende de: geometria correta + força de fechamento adequada + gaxeta íntegra + superfície de contato adequada.",
"causas":["Gaxeta suja ou danificada","Gaxeta deformada","Porta desalinhada","Fechamento com força desigual","Folga mecânica","Superfície de vedação danificada"],
"passos":[
"Retirar o equipamento de uso e aguardar resfriamento e despressurização completa.",
"Registrar o ponto exato do vazamento.",
"Verificar se o vazamento ocorre sempre no mesmo lado.",
"Inspecionar visualmente toda a gaxeta.",
"Comparar o lado que vaza com o lado que apresenta vedação adequada.",
"Verificar alinhamento, folgas e mecanismo de fechamento conforme manual técnico.",
"Executar apenas o ajuste previsto pelo fabricante.",
"Realizar teste funcional e validar a vedação."
],
"nao_fazer":"Não usar martelo, anilhas ou deformação mecânica como procedimento genérico. O ajuste depende da geometria e do mecanismo específico do equipamento."
},
{
"titulo":"Liga, mas não aquece",
"sintoma":"Painel funciona, mas a temperatura não aumenta adequadamente.",
"cadeia":"Para aquecer, é necessário: comando → elemento de acionamento → circuito de potência → resistência → transferência de calor → leitura correta do sensor.",
"causas":["Resistência aberta ou degradada","Conexão defeituosa","Falha de relé/acionamento","Falha de comando","Sensor com leitura incorreta","Proteção térmica atuada"],
"passos":[
"Identificar em qual momento do ciclo o aquecimento deveria iniciar.",
"Desenergizar e aguardar o equipamento resfriar.",
"Consultar o diagrama elétrico específico do modelo.",
"Separar duas hipóteses: o sistema não está mandando aquecer OU está mandando aquecer e a carga não responde.",
"Verificar conectores e sinais visíveis de falha.",
"Realizar os testes elétricos previstos pelo fabricante.",
"Confirmar se a falha está no comando, na potência ou no elemento de aquecimento.",
"Após a intervenção, validar o comportamento completo."
],
"nao_fazer":"Não fazer jumper permanente em termostatos, sensores ou dispositivos de segurança para 'testar'. Um componente de dois fios pode exercer função crítica de proteção."
},
{
"titulo":"Não atinge a temperatura programada",
"sintoma":"A temperatura sobe, mas não alcança o comportamento esperado.",
"cadeia":"Pode haver geração insuficiente de calor, perda de energia, leitura errada ou controle inadequado.",
"causas":["Aquecimento insuficiente","Vazamento","Sensor incorreto","Falha de alimentação","Falha de controle"],
"passos":[
"Confirmar o comportamento real e a configuração do ciclo.",
"Verificar se existem vazamentos.",
"Observar o tempo de subida de temperatura.",
"Separar sensor → controle → acionamento → resistência.",
"Utilizar instrumentos de teste adequados.",
"Validar o ciclo após a correção."
],
"nao_fazer":"Não alterar parâmetros do ciclo para mascarar uma falha técnica."
}
]
},

"📈 Eletrocardiógrafo": {
"tipo":"Aquisição de sinais bioelétricos cardíacos",
"imagem":None,
"objetivo":"""
O eletrocardiógrafo registra diferenças de potencial elétrico relacionadas à atividade
elétrica cardíaca. Ele não “mede a indução do coração” da mesma forma que um sensor
indutivo mede um campo magnético.

Os eletrodos fazem contato elétrico com o corpo e permitem medir diferenças de potencial
entre pontos do corpo. O sistema eletrônico precisa amplificar sinais pequenos e rejeitar
ruídos sem distorcer o traçado.
""",
"raciocinio":[
("1. O coração gera atividade elétrica?",
 "Sim. A despolarização e a repolarização do tecido cardíaco produzem campos elétricos que resultam em diferenças de potencial detectáveis na superfície corporal."),
("2. Como o ECG captura isso?",
 "Por eletrodos em contato com a pele. O equipamento mede diferenças de potencial entre entradas."),
("3. Por que o sinal é sensível?",
 "Porque os sinais de interesse são relativamente pequenos e o ambiente possui diversas fontes de interferência."),
("4. O que o amplificador faz?",
 "Amplifica principalmente a diferença entre entradas e busca rejeitar sinais comuns às duas entradas."),
("5. Como uma interferência aparece?",
 "Um campo elétrico ou magnético externo pode acoplar energia aos cabos e circuitos, gerando sinais indesejados.")
],
"principio":"""
### Cadeia de aquisição

**Atividade elétrica cardíaca → propagação pelo corpo → eletrodos →
cabos → proteção/isolação → amplificador diferencial → filtros →
conversão/processamento → tela ou impressão.**

### Ponto essencial: ECG ≠ leitura por indução

O ECG normalmente mede **biopotenciais por eletrodos**, e não utiliza um princípio
de indução eletromagnética como mecanismo principal de aquisição.

Porém, a **indução eletromagnética pode explicar uma fonte de interferência**.
São duas coisas diferentes:

- **Sinal desejado:** diferença de potencial bioelétrica do paciente.
- **Interferência indesejada:** tensão ou ruído induzido/coplado ao sistema.

Essa diferença é fundamental para diagnosticar problemas.
""",
"componentes":[
("Eletrodo","Cria a interface elétrica entre a pele e o sistema.","Mau contato aumenta impedância e facilita ruído e artefatos."),
("Cabo do paciente","Transporta os sinais até o equipamento.","Funciona como possível caminho de captação de interferências."),
("Amplificador diferencial","Amplifica a diferença entre sinais das entradas.","Ajuda a rejeitar sinais comuns, mas a rejeição não é infinita."),
("Filtros","Reduzem faixas específicas de ruído.","Filtros inadequados ou excessivos podem alterar a interpretação do sinal."),
("Sistema de isolação","Ajuda a manter a segurança elétrica do paciente.","Falhas exigem avaliação especializada e testes de segurança."),
("Conversor/processador","Digitaliza e processa o sinal.","Falhas podem causar comportamento incorreto no registro."),
],
"interferencia":"""
## Transformadores e interferência: qual é a relação?

Um transformador utiliza **indução eletromagnética** para transferir energia entre enrolamentos.

### Funcionamento simplificado

**Corrente alternada no enrolamento primário → campo magnético variável no núcleo →
fluxo magnético variável → tensão induzida no enrolamento secundário.**

A relação com o ECG aparece porque campos eletromagnéticos externos podem produzir
**acoplamento indesejado**.

Isso pode ocorrer por:

### 1. Acoplamento magnético
Um campo magnético variável pode induzir tensão em um condutor. Cabos longos podem
funcionar como uma área suscetível à captação.

### 2. Acoplamento capacitivo
Existe acoplamento por campo elétrico entre condutores próximos.

### 3. Interferência conduzida
Ruído pode chegar pela alimentação elétrica ou pelo aterramento.

### 4. Loop de terra
Diferenças de potencial entre pontos de aterramento podem criar correntes indesejadas.

### Atenção ao caso da bancada metálica

Uma bancada metálica **não deve ser automaticamente considerada a causa** de amplitudes
anormais. O metal pode participar do ambiente eletromagnético e alterar caminhos de
acoplamento, mas isso precisa ser demonstrado com teste controlado.

O método correto é mudar **uma variável por vez**.
""",
"problemas":[
{
"titulo":"Traçado com ruído excessivo",
"sintoma":"Linha instável, oscilação ou interferência.",
"cadeia":"Paciente/eletrodo → cabo → ambiente → entrada analógica → processamento.",
"causas":["Mau contato","Movimento","Eletrodos inadequados","Cabo danificado","Interferência de rede elétrica","Equipamentos próximos","Problema de aterramento"],
"passos":[
"Classificar visualmente o ruído: contínuo, periódico, aleatório ou relacionado ao movimento.",
"Verificar eletrodos e preparação da pele conforme procedimento.",
"Inspecionar cabos e conectores.",
"Afastar possíveis fontes de interferência.",
"Comparar o equipamento em outro ambiente.",
"Quando disponível, utilizar simulador de ECG.",
"Trocar uma variável por vez.",
"Se o defeito persistir com simulador e em ambiente controlado, investigar o equipamento."
],
"nao_fazer":"Não concluir que um transformador ou bancada é a causa sem teste comparativo."
},
{
"titulo":"Amplitude muito alta ou muito baixa",
"sintoma":"Traçado aparentemente desregulado.",
"cadeia":"Amplitude observada depende do sinal real + ganho configurado + qualidade da aquisição + possíveis artefatos.",
"causas":["Ganho/configuração","Artefato","Problema de eletrodo","Cabo","Interferência","Falha do circuito de aquisição"],
"passos":[
"Verificar configuração de ganho.",
"Registrar quais derivações são afetadas.",
"Testar com simulador de ECG, quando disponível.",
"Comparar com outro equipamento sob condições controladas.",
"Trocar uma variável por vez: equipamento, cabo, ambiente, tomada.",
"Somente após isolar causas externas, investigar a eletrônica interna."
],
"nao_fazer":"Não interpretar amplitude anormal diretamente como defeito de transformador interno."
}
]
},

"💨 Compressor": {
"tipo":"Sistema pneumático",
"imagem":None,
"objetivo":"""
O compressor converte energia elétrica em energia pneumática ao aumentar a pressão do ar.
Em aplicações odontológicas, o ar comprimido pode alimentar instrumentos e outros subsistemas.

Para diagnosticar corretamente, pense em uma cadeia de energia:
**energia elétrica → motor → movimento mecânico → compressão → pressão → distribuição do ar.**
""",
"raciocinio":[
("Energia elétrica","Alimenta o motor."),
("Motor","Converte energia elétrica em movimento."),
("Compressão","O mecanismo reduz o volume disponível para o ar e aumenta sua pressão."),
("Armazenamento","O reservatório acumula energia pneumática."),
("Controle","O pressostato monitora a pressão e controla o funcionamento."),
("Distribuição","O ar segue por mangueiras, filtros e reguladores.")
],
"principio":"""
### Fluxo de funcionamento

**Tomada → circuito elétrico → motor → pistão/cabeçote → compressão →
reservatório → pressostato → mangueiras → equipamento.**

Um defeito deve ser localizado na cadeia.

Exemplo:

**Não enche o reservatório**

Pode ser:
- motor não gira;
- motor gira, mas não há compressão;
- há compressão, mas existe vazamento;
- existe problema de medição ou controle de pressão.
""",
"componentes":[
("Motor","Gera movimento mecânico.","Se não gira, investigue alimentação, comando e circuito de partida."),
("Cabeçote/pistão","Realiza compressão do ar.","Desgaste pode reduzir desempenho."),
("Reservatório","Armazena ar pressurizado.","Exige atenção especial por ser um recipiente pressurizado."),
("Pressostato","Controla acionamento conforme pressão.","Falha pode impedir partida ou desligamento."),
("Manômetro","Indica pressão.","Uma indicação incorreta pode confundir o diagnóstico."),
("Válvula de retenção","Evita retorno de ar.","Falha pode prejudicar pressão e partida."),
("Válvula de segurança","Protege contra sobrepressão.","É componente de segurança."),
("Purgador","Remove condensado.","Acúmulo de água pode causar problemas."),
],
"problemas":[
{
"titulo":"Compressor não liga",
"sintoma":"Motor não inicia.",
"cadeia":"Alimentação → proteção → comando → circuito de partida → motor.",
"causas":["Sem alimentação","Pressostato","Proteção térmica","Capacitor","Motor"],
"passos":[
"Confirmar alimentação.",
"Registrar se há ruído ou tentativa de partida.",
"Verificar a pressão atual.",
"Consultar a lógica do pressostato.",
"Seguir o procedimento técnico para o circuito de partida.",
"Confirmar a causa antes de substituir componentes."
],
"nao_fazer":"Não trabalhar em reservatório pressurizado sem despressurização e procedimento seguro."
},
{
"titulo":"Enche lentamente",
"sintoma":"Tempo excessivo para atingir pressão.",
"cadeia":"Capacidade de compressão deve ser maior que perdas por vazamentos e consumo.",
"causas":["Vazamento","Filtro obstruído","Desgaste","Válvula defeituosa"],
"passos":[
"Comparar tempo de enchimento com referência do equipamento.",
"Verificar vazamentos.",
"Inspecionar filtro.",
"Investigar conjunto de compressão e válvulas.",
"Validar pressão de corte e recuperação."
],
"nao_fazer":"Não exceder a pressão nominal durante testes."
}
]
},

"❄️ Câmara fria / Câmara de vacina": {
"tipo":"Refrigeração e controle térmico",
"imagem":None,
"objetivo":"""
Uma câmara fria ou câmara de vacina precisa manter produtos sensíveis em uma faixa térmica
especificada. O conceito central é **remover calor do interior e controlar continuamente
a temperatura**.

Não basta verificar se o equipamento está frio. É necessário analisar estabilidade,
uniformidade, alarmes, histórico e comportamento ao longo do tempo.
""",
"raciocinio":[
("O que é temperatura?","É uma medida relacionada ao estado térmico do sistema."),
("Como resfriar?","É necessário retirar energia térmica do ambiente interno."),
("Quem retira o calor?","O ciclo de refrigeração transporta calor de uma região para outra."),
("Quem decide quando ligar?","O controlador utiliza informações de sensores."),
("Como ocorre uma falha?","Pode ser problema de refrigeração, circulação de ar, porta, sensor ou controle.")
],
"principio":"""
### Ciclo de refrigeração simplificado

**Compressor → refrigerante comprimido → condensador libera calor →
expansão reduz pressão → evaporador absorve calor da câmara → compressor.**

### Controle

**Sensor → controlador → decisão → compressor/atuadores → nova medição.**

Assim, uma falha de temperatura pode ocorrer mesmo que o compressor esteja funcionando.
""",
"componentes":[
("Compressor","Movimenta o refrigerante pelo sistema.","Falha pode impedir remoção adequada de calor."),
("Condensador","Libera calor para o ambiente.","Sujeira e ventilação inadequada podem reduzir eficiência."),
("Evaporador","Absorve calor do ambiente interno.","Gelo excessivo pode reduzir desempenho."),
("Ventilador","Ajuda a distribuir ar.","Falha pode gerar gradientes de temperatura."),
("Sensor","Mede temperatura.","Leitura errada pode levar a controle incorreto."),
("Controlador","Decide acionamento.","Falha pode causar ciclos inadequados."),
("Gaxeta","Reduz entrada de ar quente e umidade.","Falha pode aumentar carga térmica."),
],
"problemas":[
{
"titulo":"Temperatura acima da faixa",
"sintoma":"Temperatura interna não retorna ao setpoint.",
"cadeia":"Carga térmica + remoção de calor + circulação + medição + controle.",
"causas":["Porta aberta","Gaxeta","Condensador obstruído","Ventilador","Compressor","Sensor","Controlador"],
"passos":[
"Priorizar imediatamente a proteção do conteúdo conforme protocolo institucional.",
"Confirmar a leitura por método autorizado.",
"Verificar porta e vedação.",
"Verificar circulação de ar.",
"Consultar histórico de temperatura.",
"Separar falha de refrigeração de falha de medição.",
"Investigar componentes conforme manual."
],
"nao_fazer":"Não ajustar o setpoint apenas para compensar uma falha."
}
]
},

"🦷 Cadeira e caneta odontológica": {
"tipo":"Sistema eletromecânico, pneumático e hidráulico",
"imagem":None,
"objetivo":"""
A cadeira odontológica é um sistema integrado. Ela pode combinar eletrônica, motores,
atuadores, válvulas, ar comprimido, água e mecanismos.

A melhor estratégia de diagnóstico é não pensar nela como um único equipamento,
mas como vários subsistemas conectados.
""",
"raciocinio":[
("Comando","O operador pressiona botão ou pedal."),
("Controle","O circuito interpreta o comando."),
("Atuação","Motor, válvula ou atuador recebe energia."),
("Movimento/fluxo","O mecanismo executa a função."),
("Feedback","Sensores ou fins de curso podem limitar ou informar posição.")
],
"principio":"""
### Pergunta principal

**Qual subsistema está falhando?**

- Elétrico?
- Eletrônico?
- Mecânico?
- Pneumático?
- Hidráulico?

Exemplo: a cadeira não sobe.

Isso não significa automaticamente “motor queimado”.

Pode ser:

**Botão → placa → relé → motor → transmissão mecânica → fim de curso.**
""",
"componentes":[
("Placa de controle","Interpreta comandos.","Falha pode afetar uma ou várias funções."),
("Pedal","Envia comandos.","Problemas podem ser mecânicos ou elétricos."),
("Motor/atuador","Produz movimento.","Pode falhar por alimentação, comando ou defeito próprio."),
("Fim de curso","Limita movimentos.","Falha pode impedir deslocamento."),
("Mangueiras","Transportam ar ou água.","Vazamentos reduzem pressão ou fluxo."),
("Válvulas","Controlam fluxo.","Obstrução ou falha altera funcionamento."),
("Regulador","Controla pressão.","Pressão inadequada afeta instrumentos.")
],
"problemas":[
{
"titulo":"Cadeira não sobe/desce",
"sintoma":"Movimento não ocorre.",
"cadeia":"Comando → controle → potência → motor/atuador → mecânica.",
"causas":["Comando","Alimentação","Fim de curso","Placa","Motor","Travamento mecânico"],
"passos":[
"Verificar se nenhuma função funciona ou apenas um movimento.",
"Verificar comando.",
"Observar ruídos de acionamento.",
"Separar ausência de comando de travamento mecânico.",
"Consultar esquema técnico antes de medir a placa.",
"Validar movimento após correção."
],
"nao_fazer":"Não trabalhar sob partes móveis sem suporte mecânico seguro."
}
]
},

"🔊 Ultrassom odontológico": {
"tipo":"Conversão eletromecânica em alta frequência",
"imagem":None,
"objetivo":"""
O ultrassom odontológico converte energia elétrica em vibração mecânica de alta frequência.
O circuito eletrônico fornece energia ao transdutor, que converte essa energia em movimento.

Dependendo da tecnologia, o sistema pode ser piezoelétrico ou magnetoestritivo.
""",
"raciocinio":[
("Energia elétrica","O circuito gera sinal elétrico adequado."),
("Transdutor","Converte energia elétrica em vibração mecânica."),
("Ressonância","O conjunto é projetado para operar adequadamente em determinadas frequências."),
("Ponta","Transmite a vibração."),
("Água","Auxilia irrigação e, conforme o sistema, resfriamento.")
],
"principio":"""
### Cadeia

**Comando → gerador eletrônico → transdutor → vibração →
caneta/inserto → ação mecânica.**

Um problema de “sem vibração” pode estar no comando, na placa, no cabo,
no transdutor ou no inserto.
""",
"componentes":[
("Placa geradora","Produz o sinal elétrico.","Falha pode impedir excitação."),
("Transdutor","Converte energia elétrica em mecânica.","É elemento central do funcionamento."),
("Caneta","Transmite a energia.","Cabos e conexões devem ser avaliados."),
("Inserto","Elemento vibratório ativo.","Desgaste ou incompatibilidade afetam desempenho."),
("Sistema de água","Fornece irrigação.","Obstrução reduz fluxo.")
],
"problemas":[
{
"titulo":"Sem vibração",
"sintoma":"Instrumento não apresenta funcionamento esperado.",
"cadeia":"Comando → geração → cabo → transdutor → inserto.",
"causas":["Inserto","Cabo","Transdutor","Placa","Pedal"],
"passos":[
"Confirmar alimentação.",
"Confirmar comando.",
"Verificar encaixe e compatibilidade do inserto.",
"Inspecionar cabo.",
"Comparar com componente conhecido em boas condições quando permitido.",
"Investigar eletrônica conforme documentação."
],
"nao_fazer":"Não utilizar componentes incompatíveis."
}
]
},

"🔍 Colposcópio": {
"tipo":"Sistema óptico e de iluminação",
"imagem":None,
"objetivo":"""
O colposcópio utiliza ampliação e iluminação para observação detalhada.
A qualidade da imagem depende de uma cadeia óptica e mecânica.

Para diagnosticar, separe:
**iluminação → óptica → foco → posicionamento → captura digital, quando presente.**
""",
"raciocinio":[
("Iluminação","O campo precisa receber luz adequada."),
("Reflexão","A luz interage com a superfície observada."),
("Lentes","A óptica coleta e organiza a luz."),
("Foco","A posição relativa das lentes determina nitidez."),
("Ampliação","O sistema altera o campo observado."),
("Imagem","O profissional observa diretamente ou por câmera.")
],
"principio":"""
### Cadeia óptica

**Fonte de luz → campo observado → reflexão → lentes → ampliação →
ocular/câmera → imagem.**

Se a imagem está ruim, não significa necessariamente defeito eletrônico.
Pode ser:

- lente suja;
- foco inadequado;
- distância de trabalho;
- iluminação;
- desalinhamento óptico.
""",
"componentes":[
("Fonte de luz","Ilumina o campo.","Falhas reduzem visualização."),
("Lentes","Formam imagem.","Sujeira ou dano alteram qualidade."),
("Sistema de foco","Ajusta nitidez.","Falha mecânica impede focalização."),
("Braço","Posiciona o conjunto.","Folgas afetam estabilidade."),
("Câmera","Captura imagem, quando presente.","Falha pode ser óptica, eletrônica ou de software.")
],
"problemas":[
{
"titulo":"Imagem desfocada",
"sintoma":"Imagem não apresenta nitidez.",
"cadeia":"Posicionamento → distância → foco → lente → alinhamento óptico.",
"causas":["Foco","Distância","Lente suja","Problema mecânico","Problema óptico"],
"passos":[
"Verificar ajuste de foco.",
"Verificar distância de trabalho.",
"Inspecionar lentes.",
"Limpar somente conforme orientação do fabricante.",
"Se persistir, investigar mecanismo de foco e sistema óptico."
],
"nao_fazer":"Não utilizar produtos ou materiais abrasivos nas lentes."
}
]
}
}


# ==========================================================
# CAMADA TÉCNICA AVANÇADA — V3
# Princípios físicos → subsistemas → componentes → relações
# → falhas → testes → decisão → validação
# ==========================================================

TECNICO = {
    "♨️ Autoclave": {
        "fisica": """
### Princípios físicos

**1. Conversão eletrotérmica (efeito Joule)**  
A resistência converte energia elétrica em calor. A potência dissipada depende do circuito e da resistência elétrica do elemento de aquecimento.

**2. Transferência de calor**  
O aquecimento da carga ocorre por condução, convecção e, principalmente no processo com vapor, pela transferência intensa de energia durante a condensação do vapor sobre superfícies mais frias.

**3. Relação pressão–temperatura do vapor**  
Em um sistema de vapor saturado, pressão e temperatura estão relacionadas. Entretanto, **pressão não substitui temperatura nem tempo de exposição**: o processo precisa seguir o ciclo especificado pelo fabricante.

**4. Remoção de ar e contato com a carga**  
Ar residual pode prejudicar a distribuição do vapor. A eficiência depende da arquitetura da autoclave, do carregamento e do ciclo utilizado.
""",
        "interno": [
            ("Entrada e proteção", "A alimentação chega ao equipamento e passa por dispositivos de proteção e distribuição."),
            ("Controle", "A placa/controlador lê sensores, verifica condições de segurança e executa a sequência programada."),
            ("Geração de calor", "A resistência transfere energia ao sistema térmico e possibilita a geração/aquecimento do meio de processo."),
            ("Câmara e vedação", "A porta, gaxeta e mecanismo de fechamento precisam manter a integridade do volume pressurizado."),
            ("Medição", "Sensores fornecem temperatura e, conforme o modelo, pressão ou outras condições."),
            ("Sequência do ciclo", "O controlador conduz condicionamento, aquecimento, exposição, exaustão e secagem conforme a arquitetura."),
            ("Segurança", "Intertravamentos e dispositivos de proteção impedem condições inseguras.")
        ],
        "subsistemas": {
            "Elétrico/Potência": ["alimentação", "fusíveis/proteções", "relé/acionamento", "resistência"],
            "Térmico": ["resistência", "transferência de calor", "sensor de temperatura"],
            "Pressão/Vapor": ["câmara", "válvulas", "linhas de fluxo", "exaustão"],
            "Vedação/Mecânico": ["porta", "gaxeta", "dobradiça", "mecanismo de fechamento"],
            "Controle/Sensores": ["placa", "sensor", "lógica do ciclo", "intertravamentos"],
            "Segurança": ["trava", "proteções térmicas", "dispositivos previstos pelo fabricante"]
        },
        "relacoes": [
            ("Controle", "Resistência", "comanda aquecimento"),
            ("Resistência", "Câmara", "fornece energia térmica"),
            ("Sensor de temperatura", "Controle", "fecha a malha de controle"),
            ("Porta/Gaxeta", "Câmara", "mantém vedação"),
            ("Válvulas", "Câmara", "controlam fluxo/condições")
        ],
        "diagrama": """ALIMENTAÇÃO
    ↓
PROTEÇÃO → CONTROLE ← SENSOR
    ↓               ↑
ACIONAMENTO → RESISTÊNCIA
                  ↓
             CÂMARA / VAPOR
                  ↓
        VEDAÇÃO → EXPOSIÇÃO → EXAUSTÃO""",
        "falhas": {
            "Vedação/Mecânico": ["Vazamento localizado na porta", "Gaxeta deformada/suja", "Desalinhamento", "Fechamento desigual"],
            "Elétrico/Potência": ["Não liga", "Liga mas não aquece", "Proteção atuada", "Falha de acionamento"],
            "Térmico": ["Subida lenta de temperatura", "Não atinge condição prevista", "Oscilação de leitura"],
            "Controle/Sensores": ["Ciclo interrompe", "Leitura incoerente", "Comando inadequado"],
            "Pressão/Vapor": ["Comportamento anormal de pressão", "Fluxo/exaustão inadequado"]
        },
        "testes": [
            ("Vazamento sempre no mesmo lado?", "Sim → aumenta a suspeita de assimetria mecânica; não → investigar gaxeta/superfície em todo o perímetro."),
            ("Controlador solicita aquecimento?", "Separar falha de comando de falha da cadeia de potência, conforme documentação técnica."),
            ("Temperatura medida externamente e leitura interna concordam?", "Divergência controlada sugere investigar medição/calibração; usar método autorizado."),
            ("Falha ocorre com ciclo repetido?", "Reprodutibilidade ajuda a separar evento aleatório de defeito sistemático.")
        ],
        "arvore": """SINTOMA
├── Não liga → alimentação? → proteção? → comando?
├── Liga/não aquece → comando? → potência? → elemento térmico?
├── Aquece/não conclui → sensor? → controle? → condição de processo?
└── Vaza na porta → ponto fixo? → gaxeta? → alinhamento? → fechamento?""",
        "validacao": ["Inspeção visual e montagem correta", "Ausência do sintoma original", "Ciclo funcional completo conforme fabricante", "Verificação dos intertravamentos", "Registro dos parâmetros/testes exigidos pelo procedimento institucional"]
    },

    "📈 Eletrocardiógrafo": {
        "fisica": """
### Princípios físicos

**1. Biopotenciais**  
O ECG mede diferenças de potencial elétrico associadas à atividade cardíaca, captadas na superfície corporal.

**2. Interface eletrodo–pele**  
A qualidade do contato influencia a impedância e a suscetibilidade a artefatos. Movimento e contato inadequado alteram a aquisição.

**3. Amplificação diferencial e rejeição de modo comum**  
O front-end amplifica diferenças entre entradas e busca rejeitar sinais comuns. A rejeição é finita e depende do equilíbrio do sistema.

**4. Ruído e acoplamento eletromagnético**  
Cabos podem captar interferência por acoplamento capacitivo, magnético ou conduzido. O ambiente deve ser tratado como variável experimental.
""",
        "interno": [
            ("Interface paciente", "Eletrodos estabelecem contato elétrico com a pele."),
            ("Cabos", "Transportam sinais de baixa amplitude e podem captar interferências."),
            ("Proteção/isolação", "A entrada do paciente possui arquitetura de segurança específica."),
            ("Front-end analógico", "Amplifica o sinal diferencial e condiciona o sinal."),
            ("Filtragem", "Atenua componentes indesejados dentro da estratégia do equipamento."),
            ("Conversão", "O sinal condicionado é digitalizado."),
            ("Processamento", "O software/processador organiza a exibição e os registros.")
        ]
    }
}


# ==========================================================
# INTERFACE DO GUIA DE CAMPO
# ==========================================================

def render_html_card(title, body, css_class="concept"):
    st.markdown(
        f"""
        <div class="{css_class}">
            <h3>{title}</h3>
            <div>{body}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

with st.sidebar:
    st.markdown(
        """
        <div style="padding: 1rem 0 1.2rem 0; text-align:center;">
            <div style="font-size:42px;">🩺</div>
            <h2 style="color:#f8fafc; margin:0;">Engenharia Clínica</h2>
            <p style="color:#cbd5e1; font-size:13px; margin-top:5px;">
                Guia de Campo
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        '<p style="color:#94a3b8;font-size:12px;font-weight:700;'
        'text-transform:uppercase;letter-spacing:.08em;">Equipamento</p>',
        unsafe_allow_html=True,
    )

    equipamento_selecionado = st.selectbox(
        "Selecione o equipamento",
        list(EQUIPAMENTOS.keys()),
        label_visibility="collapsed",
    )

    st.markdown("---")

    modo = st.radio(
        "Modo de visualização",
        ["📘 Guia de Campo", "🔬 Análise Técnica"],
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="color:#94a3b8;font-size:11px;line-height:1.55;">
            <b>FLUXO DE DIAGNÓSTICO</b><br><br>
            PRINCÍPIO FÍSICO<br>↓<br>
            COMPONENTE<br>↓<br>
            SINTOMA<br>↓<br>
            HIPÓTESE<br>↓<br>
            TESTE<br>↓<br>
            CONCLUSÃO<br>↓<br>
            CORREÇÃO AUTORIZADA<br>↓<br>
            VALIDAÇÃO
        </div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------
# DADOS
# ----------------------------------------------------------

dados = EQUIPAMENTOS[equipamento_selecionado]
tecnico = TECNICO.get(equipamento_selecionado)


# ==========================================================
# CABEÇALHO
# ==========================================================

st.markdown(
    f"""
    <div class="hero">
        <div style="font-size:13px;color:#93c5fd;font-weight:600;
                    margin-bottom:.4rem;">
            ENGENHARIA CLÍNICA • GUIA DE CAMPO
        </div>
        <h1 style="margin:0;font-size:2rem;">
            {equipamento_selecionado}
        </h1>
        <p style="margin-top:.7rem;margin-bottom:0;color:#cbd5e1;
                  font-size:15px;">
            {dados.get("tipo", "Sistema de engenharia clínica")}
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# GUIA DE CAMPO
# ==========================================================

if modo == "📘 Guia de Campo":

    st.markdown("## Visão geral")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="concept"><h3>🎯 Objetivo do equipamento</h3></div>',
            unsafe_allow_html=True,
        )
        st.markdown(dados.get("objetivo", "Informação não disponível."))

    with col2:
        st.markdown(
            '<div class="concept"><h3>⚙️ Princípio de funcionamento</h3></div>',
            unsafe_allow_html=True,
        )
        st.markdown(dados.get("principio", "Informação não disponível."))

    raciocinio = dados.get("raciocinio", [])

    if raciocinio:
        st.markdown("---")
        st.markdown("## 🧠 Raciocínio de engenharia")

        cols = st.columns(min(3, len(raciocinio)))

        for i, item in enumerate(raciocinio):
            pergunta, resposta = item

            with cols[i % len(cols)]:
                st.markdown(
                    f"""
                    <div class="concept" style="height:100%;">
                        <div style="color:#60a5fa;font-weight:700;
                                    font-size:14px;margin-bottom:.5rem;">
                            {pergunta}
                        </div>
                        <div style="color:#e2e8f0;font-size:14px;
                                    line-height:1.6;">
                            {resposta}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    componentes = dados.get("componentes", [])

    if componentes:
        st.markdown("---")
        st.markdown("## 🔩 Componentes e função")

        for componente in componentes:
            nome, funcao, falha = componente

            with st.expander(f"🔧 {nome}"):
                c1, c2 = st.columns(2)

                with c1:
                    st.markdown("**Função**")
                    st.write(funcao)

                with c2:
                    st.markdown("**O que observar em caso de falha**")
                    st.write(falha)

    problemas = dados.get("problemas", [])

    if problemas:
        st.markdown("---")
        st.markdown("## 🚨 Diagnóstico por sintoma")
        st.caption(
            "Selecione um sintoma para seguir uma sequência estruturada "
            "de diagnóstico."
        )

        titulos = [p.get("titulo", "Problema") for p in problemas]

        problema_titulo = st.selectbox(
            "Sintoma / problema",
            titulos,
            key=f"problema_{equipamento_selecionado}",
        )

        problema = next(
            (p for p in problemas if p.get("titulo") == problema_titulo),
            None,
        )

        if problema:
            st.markdown(
                f"""
                <div class="warning-box">
                    <h3 style="margin-top:0;">
                        {problema.get("titulo", "")}
                    </h3>
                    <p><b>Sintoma:</b> {problema.get("sintoma", "")}</p>
                    <p><b>Cadeia de diagnóstico:</b>
                    {problema.get("cadeia", "")}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            causas = problema.get("causas", [])

            if causas:
                st.markdown("### 🔎 Possíveis causas")
                cols = st.columns(2)

                for i, causa in enumerate(causas):
                    with cols[i % 2]:
                        st.markdown(
                            f'<div class="concept">🔹 {causa}</div>',
                            unsafe_allow_html=True,
                        )

            passos = problema.get("passos", [])

            if passos:
                st.markdown("### 🛠️ Passo a passo")

                for i, passo in enumerate(passos, start=1):
                    st.markdown(
                        f"""
                        <div class="concept">
                            <div style="display:flex;gap:12px;
                                        align-items:flex-start;">
                                <div style="min-width:30px;height:30px;
                                            border-radius:50%;
                                            background:#2563eb;
                                            display:flex;
                                            align-items:center;
                                            justify-content:center;
                                            font-weight:700;">
                                    {i}
                                </div>
                                <div style="padding-top:4px;line-height:1.5;">
                                    {passo}
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            nao_fazer = problema.get("nao_fazer")

            if nao_fazer:
                st.markdown(
                    f"""
                    <div class="warning-box">
                        <h3 style="margin-top:0;">⚠️ O que NÃO fazer</h3>
                        <p style="margin-bottom:0;">{nao_fazer}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# ==========================================================
# ANÁLISE TÉCNICA
# ==========================================================

else:

    if tecnico is None:
        st.warning(
            "A camada técnica avançada ainda não foi cadastrada "
            "para este equipamento."
        )
        st.info(
            "O Guia de Campo continua disponível no modo "
            "'📘 Guia de Campo'."
        )

    else:
        st.markdown("## 🔬 Análise Técnica Avançada")
        st.caption(
            "Princípios físicos → subsistemas → componentes → relações "
            "→ falhas → testes → decisão → validação"
        )

        fisica = tecnico.get("fisica")

        if fisica:
            st.markdown("---")
            st.markdown("## ⚛️ Princípios físicos")
            st.markdown(fisica)

        interno = tecnico.get("interno", [])

        if interno:
            st.markdown("---")
            st.markdown("## 🏗️ Estrutura interna")

            for etapa in interno:
                nome, descricao = etapa

                st.markdown(
                    f"""
                    <div class="concept">
                        <h4 style="margin-top:0;color:#60a5fa !important;">
                            {nome}
                        </h4>
                        <p style="margin-bottom:0;">{descricao}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        subsistemas = tecnico.get("subsistemas", {})

        if subsistemas:
            st.markdown("---")
            st.markdown("## 🧩 Subsistemas")

            for nome_subsistema, lista in subsistemas.items():
                with st.expander(nome_subsistema):
                    for componente in lista:
                        st.markdown(f"• {componente}")

        relacoes = tecnico.get("relacoes", [])

        if relacoes:
            st.markdown("---")
            st.markdown("## 🔗 Relações entre componentes")

            for origem, destino, funcao in relacoes:
                st.markdown(
                    f"""
                    <div class="concept">
                        <strong>{origem}</strong>
                        <span style="color:#60a5fa;font-size:20px;">
                            &nbsp;→&nbsp;
                        </span>
                        <strong>{destino}</strong>
                        <span style="color:#cbd5e1;">
                            &nbsp; {funcao}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        diagrama = tecnico.get("diagrama")

        if diagrama:
            st.markdown("---")
            st.markdown("## 📐 Diagrama funcional")
            st.code(diagrama, language="text")

        falhas = tecnico.get("falhas", {})

        if falhas:
            st.markdown("---")
            st.markdown("## 🚨 Mapa de falhas")

            for subsistema, lista_falhas in falhas.items():
                st.markdown(f"### {subsistema}")

                cols = st.columns(2)

                for i, falha in enumerate(lista_falhas):
                    with cols[i % 2]:
                        st.markdown(
                            f"""
                            <div class="warning-box"
                                 style="margin-bottom:.6rem;">
                                🔸 {falha}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        testes = tecnico.get("testes", [])

        if testes:
            st.markdown("---")
            st.markdown("## 🧪 Testes e tomada de decisão")

            for pergunta, interpretacao in testes:
                with st.expander(f"❓ {pergunta}"):
                    st.markdown(
                        f"""
                        <div class="concept">
                            <strong>Interpretação:</strong>
                            <p style="margin-top:.5rem;margin-bottom:0;">
                                {interpretacao}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        arvore = tecnico.get("arvore")

        if arvore:
            st.markdown("---")
            st.markdown("## 🌳 Árvore de diagnóstico")
            st.code(arvore, language="text")

        validacao = tecnico.get("validacao", [])

        if validacao:
            st.markdown("---")
            st.markdown("## ✅ Validação após intervenção")

            for i, item in enumerate(validacao, start=1):
                st.markdown(
                    f"""
                    <div class="concept">
                        <div style="display:flex;gap:12px;
                                    align-items:center;">
                            <div style="min-width:28px;height:28px;
                                        border-radius:50%;
                                        background:#2563eb;
                                        display:flex;
                                        align-items:center;
                                        justify-content:center;
                                        font-weight:700;">
                                {i}
                            </div>
                            <div>{item}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# ==========================================================
# RODAPÉ
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#64748b;font-size:11px;
                padding:1rem 0 2rem 0;">
        Engenharia Clínica • Guia de Campo<br>
        Diagnóstico estruturado baseado em princípio físico,
        cadeia funcional, testes e validação.
    </div>
    """,
    unsafe_allow_html=True,
)
