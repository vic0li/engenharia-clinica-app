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
    page_title="Engenharia Clínica | Guia de Campo V2",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# ESTILO
# ----------------------------------------------------------
st.markdown("""
<style>
    .hero {
        padding: 1.5rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #eef6ff, #f7fbff);
        border: 1px solid #d8e8f8;
        margin-bottom: 1rem;
    }
    .concept {
        padding: 1rem;
        border-left: 5px solid #2d7ff9;
        background-color: #f7fbff;
        border-radius: 8px;
        margin: 0.7rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-left: 5px solid #f59e0b;
        background-color: #fffaf0;
        border-radius: 8px;
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
# FUNÇÕES
# ==========================================================

def render_image(info):
    if info.get("imagem"):
        st.image(info["imagem"], use_container_width=True)
    else:
        st.info("📷 Área reservada para foto do equipamento. Adicione imagens na pasta `images/` e atualize o campo `imagem`.")

def render_raciocinio(items):
    for titulo, texto in items:
        st.markdown(f"""
        <div class="concept">
        <b>{titulo}</b><br>{texto}
        </div>
        """, unsafe_allow_html=True)

def render_componentes(componentes):
    data = []
    for nome, funcao, diagnostico in componentes:
        data.append({
            "Componente": nome,
            "O que faz": funcao,
            "Como pensar na falha": diagnostico
        })
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

def render_problema(problema):
    st.subheader(f"⚠️ {problema['titulo']}")
    st.error(f"**Sintoma:** {problema['sintoma']}")

    st.markdown("### 🧠 Linha de raciocínio")
    st.info(problema["cadeia"])

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 🔍 Possíveis causas")
        for causa in problema["causas"]:
            st.markdown(f"- {causa}")

    with c2:
        st.markdown("### 🧭 Princípio do diagnóstico")
        st.write(
            "Não pule diretamente para a troca de uma peça. "
            "Tente localizar em qual ponto da cadeia o comportamento deixa de ser esperado."
        )

    st.markdown("### 🛠️ Roteiro de investigação")
    for i, passo in enumerate(problema["passos"], 1):
        st.markdown(f"**{i}. {passo}**")

    st.markdown("### ⛔ O que não fazer")
    st.warning(problema["nao_fazer"])

def render_diagnostico(info):
    st.markdown("""
    ## 🌳 Método universal de diagnóstico

    A ideia é transformar manutenção em uma investigação.

    **SINTOMA → SUBSISTEMA → HIPÓTESE → TESTE → RESULTADO → DECISÃO**
    """)

    st.markdown("""
    ### 1. Confirmar o sintoma

    O defeito é reproduzível?

    ### 2. Descobrir o que ainda funciona

    Se algumas funções funcionam, isso ajuda a eliminar partes da cadeia.

    ### 3. Separar subsistemas

    Elétrico? Mecânico? Pneumático? Hidráulico? Térmico? Eletrônico? Ambiente?

    ### 4. Testar uma variável por vez

    Não altere cinco coisas e depois tente descobrir qual resolveu.

    ### 5. Confirmar antes de reparar

    Hipótese não é diagnóstico.

    ### 6. Validar

    A manutenção não termina quando o equipamento liga. É necessário confirmar funcionamento e segurança.
    """)

def render_fluxo_ecg():
    st.markdown("""
    ## 🌳 Exemplo: ECG com interferência

    **Traçado anormal**

    ↓

    **O problema acontece em todas as derivações?**

    ↓

    **Verificar eletrodos e contato**

    ↓

    **Inspecionar cabos**

    ↓

    **Existe relação com movimento?**

    ↓

    **Testar em ambiente diferente**

    ↓

    **Afastar possíveis fontes de interferência**

    ↓

    **Utilizar simulador de ECG, quando disponível**

    ↓

    **Se persistir em condições controladas → investigar circuito interno**
    """)

def equipamento_page(nome, info):
    st.markdown(f'<div class="hero"><h1>{nome}</h1><h4>{info["tipo"]}</h4></div>', unsafe_allow_html=True)

    render_image(info)

    tabs = st.tabs([
        "📚 Visão geral",
        "🧠 Como pensar",
        "⚙️ Componentes",
        "🔄 Funcionamento",
        "⚡ Interferências/Física",
        "🛠️ Problemas",
        "🌳 Diagnóstico"
    ])

    with tabs[0]:
        st.markdown("## O que é e para que serve?")
        st.markdown(info["objetivo"])

    with tabs[1]:
        st.markdown("## Desenvolvendo o raciocínio técnico")
        render_raciocinio(info["raciocinio"])

    with tabs[2]:
        st.markdown("## Componentes e função no diagnóstico")
        render_componentes(info["componentes"])

    with tabs[3]:
        st.markdown("## Princípio de funcionamento")
        st.markdown(info["principio"])

    with tabs[4]:
        if nome == "📈 Eletrocardiógrafo":
            st.markdown(info["interferencia"])
        else:
            st.markdown("""
            ## Física aplicada ao diagnóstico

            Um bom diagnóstico depende de entender qual tipo de energia o equipamento utiliza.

            Pergunte:

            - Existe energia elétrica?
            - Existe conversão para calor?
            - Existe movimento?
            - Existe pressão?
            - Existe fluxo?
            - Existe transferência de calor?
            - Existe sinal elétrico?
            - Existe luz?
            - Existe um sensor?

            Depois siga a cadeia de transformação da energia.

            **Energia entra → componente transforma → outro componente transmite →
            sensor mede → controlador decide → resultado ocorre.**
            """)

    with tabs[5]:
        st.markdown("## Biblioteca de falhas")
        busca = st.text_input(
            "🔎 Pesquisar",
            placeholder="Ex.: vazamento, não aquece, ruído, temperatura..."
        ).lower()

        encontrados = []
        for p in info["problemas"]:
            texto = (p["titulo"] + p["sintoma"] + " ".join(p["causas"])).lower()
            if not busca or busca in texto:
                encontrados.append(p)

        if not encontrados:
            st.info("Nenhum problema encontrado.")
        else:
            escolha = st.selectbox(
                "Selecione o problema",
                [p["titulo"] for p in encontrados]
            )
            problema = next(p for p in encontrados if p["titulo"] == escolha)
            render_problema(problema)

    with tabs[6]:
        if nome == "📈 Eletrocardiógrafo":
            render_fluxo_ecg()
        else:
            render_diagnostico(info)

# ==========================================================
# REGISTRO
# ==========================================================

def registro_page():
    st.title("📝 Registro de ocorrência")

    with st.form("registro_form"):
        equipamento = st.selectbox("Equipamento", list(EQUIPAMENTOS.keys()))
        patrimonio = st.text_input("Patrimônio / identificação")
        local = st.text_input("Local")
        sintoma = st.text_area("Sintoma observado")
        subsistema = st.multiselect(
            "Possíveis subsistemas envolvidos",
            ["Elétrico", "Eletrônico", "Mecânico", "Térmico",
             "Pneumático", "Hidráulico", "Óptico", "Sensor",
             "Software/Controle", "Ambiente"]
        )
        hipotese = st.text_area("Hipótese inicial")
        teste = st.text_area("Teste realizado")
        resultado = st.text_area("Resultado do teste")
        diagnostico = st.text_area("Causa confirmada")
        acao = st.text_area("Ação corretiva / encaminhamento")
        validacao = st.text_area("Como foi validado?")
        status = st.selectbox(
            "Status",
            ["Em análise", "Aguardando peça", "Encaminhado", "Resolvido"]
        )

        submit = st.form_submit_button("💾 Salvar ocorrência")

    if submit:
        if "registros" not in st.session_state:
            st.session_state.registros = []

        st.session_state.registros.append({
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Equipamento": equipamento,
            "Patrimônio": patrimonio,
            "Local": local,
            "Sintoma": sintoma,
            "Subsistema": ", ".join(subsistema),
            "Hipótese": hipotese,
            "Teste": teste,
            "Resultado": resultado,
            "Diagnóstico": diagnostico,
            "Ação": acao,
            "Validação": validacao,
            "Status": status
        })

        st.success("Ocorrência salva na sessão.")

    if st.session_state.get("registros"):
        df = pd.DataFrame(st.session_state.registros)

        st.subheader("Histórico atual")
        st.dataframe(df, use_container_width=True, hide_index=True)

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ Exportar CSV",
            csv,
            "ocorrencias_engenharia_clinica.csv",
            "text/csv"
        )

# ==========================================================
# MODO ESTUDO
# ==========================================================

def estudo_page():
    st.title("🎓 Modo estudo")

    equipamento = st.selectbox("Escolha um equipamento", list(EQUIPAMENTOS.keys()))
    info = EQUIPAMENTOS[equipamento]

    st.markdown(f"## {equipamento}")

    st.markdown("### 🧠 Perguntas para estudar")

    perguntas = [
        "Qual é a energia de entrada do sistema?",
        "Qual é a principal transformação de energia?",
        "Qual componente executa essa transformação?",
        "Quais sensores existem?",
        "O que acontece se o sensor falhar?",
        "Quais subsistemas participam do funcionamento?",
        "Qual seria o primeiro passo diante de uma falha?",
        "Como diferenciar falha externa de falha interna?"
    ]

    for i, pergunta in enumerate(perguntas, 1):
        resposta = st.text_area(f"{i}. {pergunta}", key=f"{equipamento}_{i}")
        if resposta:
            st.caption("💡 Compare sua resposta com as abas 'Como pensar' e 'Componentes'.")

# ==========================================================
# INÍCIO
# ==========================================================

st.sidebar.title("🩺 Engenharia Clínica")
st.sidebar.caption("Guia de Campo V2")

menu = st.sidebar.radio(
    "Navegação",
    ["🏠 Início", "🎓 Modo estudo", "📝 Registro de ocorrência", "📚 Método universal", *EQUIPAMENTOS.keys()]
)

st.sidebar.divider()
modo = st.sidebar.selectbox(
    "Modo de uso",
    ["🎓 Estudo", "🔧 Campo"]
)

st.sidebar.warning("""
⚠️ Este aplicativo é um guia de estudo e apoio ao raciocínio técnico.

Não substitui:
- manual técnico;
- treinamento;
- procedimento institucional;
- instrumentos adequados;
- testes de segurança;
- autorização técnica.
""")

if menu == "🏠 Início":
    st.markdown('<div class="hero"><h1>🩺 Guia de Campo de Engenharia Clínica</h1><h3>Versão 2 — aprender a pensar, não apenas decorar defeitos</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    ## A lógica do aplicativo

    Em vez de:

    **“Sintoma → trocar peça”**

    o objetivo é:

    **Princípio físico → funcionamento → componente → subsistema →
    sintoma → hipótese → teste → confirmação → correção → validação**

    Essa abordagem ajuda a trabalhar mesmo quando aparece um equipamento ou defeito que
    você nunca viu antes.
    """)

    c1, c2, c3 = st.columns(3)
    c1.metric("Equipamentos", len(EQUIPAMENTOS))
    c2.metric("Modo", modo)
    c3.metric("Ocorrências na sessão", len(st.session_state.get("registros", [])))

    st.markdown("## 📌 Equipamentos")
    for nome, info in EQUIPAMENTOS.items():
        with st.expander(nome):
            st.write(info["tipo"])

elif menu == "🎓 Modo estudo":
    estudo_page()

elif menu == "📝 Registro de ocorrência":
    registro_page()

elif menu == "📚 Método universal":
    st.title("📚 Método universal de diagnóstico")

    st.markdown("""
    # 1️⃣ Comece pelo princípio físico

    Antes de procurar defeitos, pergunte:

    **Como esse equipamento funciona?**

    # 2️⃣ Desenhe a cadeia

    Exemplo genérico:

    **Energia → conversão → transmissão → sensor → controle → resultado**

    # 3️⃣ Descubra onde o comportamento deixa de ser esperado

    Não pergunte apenas:

    > “Qual peça está ruim?”

    Pergunte:

    > “Em qual ponto da cadeia o sistema deixou de funcionar corretamente?”

    # 4️⃣ Isole variáveis

    Um teste bom modifica apenas uma variável.

    # 5️⃣ Diferencie hipótese de diagnóstico

    **Hipótese:** pode ser o cabo.

    **Diagnóstico:** o defeito foi reproduzido e isolado no cabo por teste apropriado.

    # 6️⃣ Corrija

    Somente depois de confirmar a causa.

    # 7️⃣ Valide

    Confirme desempenho, segurança e ausência do defeito.

    # 8️⃣ Registre

    O registro cria histórico e melhora diagnósticos futuros.
    """)

else:
    equipamento_page(menu, EQUIPAMENTOS[menu])
