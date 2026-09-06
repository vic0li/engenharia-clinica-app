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
    page_title="Engenharia Clínica | Guia de Campo V4",
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
    ↓              ↑
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
            ("Processamento", "O software/processador organiza derivações, visualização e registro.")
        ],
        "subsistemas": {
            "Paciente/Eletrodos": ["eletrodos", "gel", "pele", "impedância de contato"],
            "Cabos": ["cabo paciente", "conectores", "blindagem"],
            "Aquisição Analógica": ["proteção", "amplificador diferencial", "referências"],
            "Filtragem/Conversão": ["filtros", "ADC", "processamento"],
            "Alimentação/Isolação": ["fonte", "isolação", "segurança elétrica"],
            "Ambiente": ["rede elétrica", "outros equipamentos", "campos EM", "aterramento"]
        },
        "relacoes": [
            ("Eletrodo", "Amplificador diferencial", "fornece biopotencial"),
            ("Cabo", "Ambiente", "pode sofrer acoplamento"),
            ("Amplificador", "Filtros", "entrega sinal condicionado"),
            ("Filtros", "ADC/Processamento", "prepara o sinal"),
            ("Ambiente", "Aquisição", "pode introduzir interferência")
        ],
        "diagrama": """ATIVIDADE CARDÍACA
      ↓
CORPO → ELETRODOS → CABOS ← INTERFERÊNCIA AMBIENTAL
                         ↓
              PROTEÇÃO / ISOLAÇÃO
                         ↓
             AMPLIFICADOR DIFERENCIAL
                         ↓
                  FILTROS → ADC
                         ↓
                 PROCESSAMENTO → TELA""",
        "falhas": {
            "Paciente/Eletrodos": ["Ruído por mau contato", "Artefato de movimento", "Impedância elevada"],
            "Cabos": ["Mau contato interno", "Conector danificado", "Captação de ruído"],
            "Aquisição Analógica": ["Amplitude incoerente", "Ruído persistente", "Falha de canal"],
            "Ambiente": ["Interferência de rede", "Acoplamento EM", "Problema de aterramento"],
            "Processamento": ["Configuração de ganho", "Filtros inadequados", "Falha de visualização"]
        },
        "testes": [
            ("Ruído muda com movimento?", "Sim → priorizar artefato/eletrodo/cabo; não → continuar isolamento."),
            ("Ruído persiste com simulador?", "Sim → reduz a probabilidade de causa fisiológica e aumenta investigação da cadeia técnica."),
            ("Mudar apenas o ambiente altera o defeito?", "Sim → investigar variável ambiental/acoplamento."),
            ("Todas as derivações são afetadas?", "Padrão ajuda a localizar entre contato, cabo, canal ou processamento.")
        ],
        "arvore": """TRAÇADO ANORMAL
├── Movimento altera? → eletrodo/pele/cabo
├── Todas derivações? → configuração/ambiente/cadeia comum
├── Persiste com simulador?
│   ├── Não → interface paciente
│   └── Sim → cabo → ambiente → aquisição interna
└── Persiste em ambiente controlado → investigar equipamento""",
        "validacao": ["Teste com simulador apropriado quando disponível", "Verificação de ganho e derivações", "Traçado estável nas condições de teste", "Testes de segurança elétrica aplicáveis", "Registro da condição antes/depois"]
    },

    "💨 Compressor": {
        "fisica": """
### Princípios físicos

**1. Conversão eletromecânica**: motor converte energia elétrica em movimento.

**2. Compressão de gás**: o mecanismo reduz o volume disponível ao ar, elevando sua pressão. A análise real envolve temperatura, vazamentos e eficiência do conjunto.

**3. Energia armazenada**: o reservatório contém energia pneumática e deve ser tratado como recipiente pressurizado.

**4. Controle por realimentação**: pressostato e indicação de pressão participam da lógica de partida e parada.
""",
        "interno": [("Alimentação", "Fornece energia ao sistema."), ("Motor/partida", "Produz torque e inicia movimento."), ("Cabeçote", "Comprime o ar."), ("Retenção", "Controla retorno de fluxo."), ("Reservatório", "Acumula ar pressurizado."), ("Controle", "Pressostato decide corte/retorno."), ("Distribuição", "Filtro, regulador e mangueiras entregam o ar.")],
        "subsistemas": {"Elétrico": ["alimentação", "proteção", "capacitor", "motor"], "Mecânico": ["pistão", "cabeçote", "rolamentos"], "Pneumático": ["válvulas", "reservatório", "mangueiras"], "Controle": ["pressostato", "manômetro"], "Segurança": ["válvula de segurança", "purgador", "proteções"]},
        "relacoes": [("Pressostato","Motor","liga/desliga"),("Motor","Cabeçote","fornece movimento"),("Cabeçote","Reservatório","fornece ar comprimido"),("Reservatório","Manômetro","fornece pressão para indicação"),("Válvula de retenção","Cabeçote","evita retorno")],
        "diagrama": """REDE → PROTEÇÃO → MOTOR → CABEÇOTE → RETENÇÃO → RESERVATÓRIO
                     ↑                              ↓
                 PRESSOSTATO ← PRESSÃO ← MANÔMETRO
                                                    ↓
                                      FILTRO/REGULADOR → USO""",
        "falhas": {"Elétrico": ["Não liga", "Tentativa de partida", "Proteção atua"], "Mecânico": ["Ruído", "Baixa compressão", "Desgaste"], "Pneumático": ["Vazamento", "Enchimento lento", "Retorno de ar"], "Controle": ["Não corta", "Não religa", "Indicação incoerente"]},
        "testes": [("Motor gira?", "Não → cadeia elétrica/comando; sim → seguir para compressão."), ("Pressão sobe?", "Não → capacidade de compressão versus vazamento."), ("Tempo de enchimento está fora da referência?", "Comparar com especificação do equipamento."), ("Pressão de corte é coerente?", "Avaliar controle e medição sem exceder limites nominais.")],
        "arvore": """NÃO ATINGE PRESSÃO
├── Motor não gira → alimentação/proteção/comando/partida
├── Motor gira → pressão sobe?
│   ├── Não → compressão/válvula/vazamento
│   └── Sim, lentamente → vazamento/filtro/desgaste
└── Pressão sobe demais → retirar de uso e investigar controle/segurança""",
        "validacao": ["Estanqueidade", "Tempo de enchimento dentro da referência", "Pressão de corte/retorno conforme fabricante", "Ausência de vazamento anormal", "Função dos dispositivos previstos de segurança"]
    },

    "❄️ Câmara fria / Câmara de vacina": {
        "fisica": """
### Princípios físicos

**1. Conservação de energia e transferência de calor**: o sistema remove energia térmica do interior.

**2. Ciclo de refrigeração**: o refrigerante circula entre regiões de maior e menor pressão, absorvendo calor no evaporador e rejeitando calor no condensador.

**3. Convecção**: ventiladores e circulação de ar influenciam a uniformidade espacial da temperatura.

**4. Controle em malha fechada**: sensor → controlador → atuador → nova medição.
""",
        "interno": [("Sensor", "Mede temperatura."), ("Controlador", "Compara medição e estratégia de controle."), ("Compressor", "Mantém circulação do refrigerante."), ("Condensador", "Rejeita calor ao ambiente."), ("Expansão", "Reduz pressão do fluido."), ("Evaporador", "Absorve calor do interior."), ("Ventilação", "Distribui ar e reduz gradientes."), ("Porta/gaxeta", "Limita entrada de calor e umidade.")],
        "subsistemas": {"Refrigeração": ["compressor","condensador","expansão","evaporador"], "Circulação de ar": ["ventiladores","dutos","distribuição"], "Controle": ["sensor","controlador","alarmes"], "Vedação": ["porta","gaxeta"], "Ambiente": ["temperatura externa","ventilação do condensador","carga térmica"]},
        "relacoes": [("Sensor","Controlador","realimenta"),("Controlador","Compressor","aciona"),("Compressor","Condensador","circula refrigerante"),("Evaporador","Ar interno","absorve calor"),("Ventilador","Temperatura interna","melhora uniformidade")],
        "diagrama": """SENSOR → CONTROLADOR → COMPRESSOR
   ↑                         ↓
TEMPERATURA ← EVAPORADOR ← EXPANSÃO
                    ↑
CONDENSADOR ← COMPRESSOR
                    ↓
             AMBIENTE EXTERNO""",
        "falhas": {"Refrigeração": ["Não resfria", "Recuperação lenta"], "Circulação": ["Gradiente térmico", "Pontos quentes/frios"], "Controle/Sensor": ["Leitura incoerente", "Ciclagem inadequada"], "Vedação": ["Entrada de ar quente", "Condensação"], "Ambiente": ["Condensador sem ventilação", "Carga térmica elevada"]},
        "testes": [("Leitura independente confirma o desvio?", "Separar falha real de falha de medição."), ("Compressor opera?", "Operação não garante capacidade frigorífica; continuar investigação."), ("Há circulação de ar?", "Falha pode causar não uniformidade."), ("Porta/gaxeta estão íntegras?", "Investigar carga térmica adicional."), ("Histórico mostra quando começou?", "Ajuda a correlacionar evento, ambiente e degradação.")],
        "arvore": """TEMPERATURA FORA DA FAIXA
├── Confirmar leitura por método autorizado
├── Desvio real?
│   ├── Não → sensor/medição
│   └── Sim → porta/carga/ambiente?
│             ├── Sim → reduzir causa externa conforme protocolo
│             └── Não → circulação → refrigeração → controle
└── Proteger conteúdo conforme protocolo institucional""",
        "validacao": ["Temperatura dentro da faixa especificada", "Estabilidade e recuperação", "Uniformidade conforme procedimento", "Alarmes e registro de dados", "Proteção do conteúdo e documentação"]
    },

    "🦷 Cadeira e caneta odontológica": {
        "fisica": """
### Princípios físicos

A unidade odontológica integra **eletricidade, mecânica, pneumática e hidráulica**. A mesma ação do operador pode disparar diferentes cadeias de energia.

- **Elétrica → mecânica**: motores e atuadores produzem movimento.
- **Pressão → movimento/rotação**: ar comprimido pode alimentar instrumentos.
- **Pressão e vazão**: água e ar são controlados por válvulas e reguladores.
- **Lógica de controle**: comandos são convertidos em acionamentos.
""",
        "interno": [("Comando", "Botões e pedal recebem a intenção do operador."), ("Controle", "Placa interpreta permissões e sequências."), ("Potência", "Relés/drivers fornecem energia aos atuadores."), ("Atuação", "Motor, válvula ou atuador executa a ação."), ("Distribuição", "Mangueiras transportam ar/água."), ("Feedback", "Fins de curso e sensores limitam ou informam posição.")],
        "subsistemas": {"Comando/Controle": ["pedal","botões","placa"], "Elétrico": ["fonte","relés","drivers"], "Mecânico": ["atuadores","transmissão","estrutura"], "Pneumático": ["compressor externo","regulador","válvulas","mangueiras"], "Hidráulico": ["água","válvulas","tubulações"], "Segurança/Posição": ["fim de curso","intertravamentos"]},
        "relacoes": [("Pedal","Placa","envia comando"),("Placa","Relé/Driver","comanda potência"),("Relé/Driver","Motor/Válvula","aciona"),("Ar comprimido","Caneta","fornece energia pneumática"),("Fim de curso","Controle","informa limite")],
        "diagrama": """OPERADOR → PEDAL/BOTÃO → CONTROLE → POTÊNCIA → ATUADOR
                                           ↓
AR/ÁGUA → REGULAÇÃO → VÁLVULAS → INSTRUMENTOS
                                           ↓
                                      MOVIMENTO/FLUXO
                                           ↑
                                   SENSOR/FIM DE CURSO""",
        "falhas": {"Comando/Controle": ["Função não responde", "Comando intermitente"], "Elétrico": ["Motor não aciona", "Sem alimentação"], "Mecânico": ["Travamento", "Folga", "Movimento irregular"], "Pneumático": ["Baixa pressão", "Vazamento", "Sem fluxo"], "Hidráulico": ["Baixa vazão", "Obstrução", "Vazamento"], "Segurança": ["Movimento bloqueado por fim de curso"]},
        "testes": [("Apenas uma função falha?", "Sim → cadeia específica; não → investigar alimentação/controle comum."), ("Há comando chegando ao atuador?", "Separar comando de potência/atuador conforme esquema."), ("Existe ruído de acionamento sem movimento?", "Sugere separar travamento mecânico de ausência de comando."), ("Pressão/fluxo na entrada está correto?", "Separar falha da unidade de falha no suprimento.")],
        "arvore": """FUNÇÃO NÃO OPERA
├── Outras funções operam?
│   ├── Não → alimentação/controle comum
│   └── Sim → comando específico
├── Há acionamento?
│   ├── Não → comando/controle/potência
│   └── Sim → atuador/mecânica/fluxo
└── Movimento bloqueado → verificar sensores/fins de curso conforme fabricante""",
        "validacao": ["Movimentos completos e suaves", "Comandos e pedal", "Pressão/vazão dentro da referência", "Ausência de vazamentos", "Limites de movimento e segurança"]
    },

    "🔍 Colposcópio": {
        "fisica": """
### Princípios físicos

**1. Óptica geométrica**: lentes coletam e direcionam raios de luz para formar uma imagem.

**2. Foco**: a nitidez depende da posição relativa entre objeto, lentes e plano de observação/captura.

**3. Ampliação e campo de visão**: alterações ópticas modificam a imagem observada e a área visualizada.

**4. Iluminação e reflexão**: a qualidade depende da quantidade, distribuição e direção da luz que retorna do campo observado.

**5. Captura digital, quando presente**: a luz é convertida em sinal por um sensor de imagem e processada.
""",
        "interno": [("Fonte de luz", "Produz iluminação controlada."), ("Sistema de iluminação", "Direciona a luz ao campo."), ("Objeto/campo", "Reflete parte da luz."), ("Óptica", "Coleta e forma imagem."), ("Foco/ampliação", "Ajusta nitidez e campo."), ("Ocular/câmera", "Permite observação ou captura."), ("Mecânica", "Mantém alinhamento e posicionamento.")],
        "subsistemas": {"Iluminação": ["fonte","driver","guia óptico"], "Óptico": ["objetivas","oculares","lentes"], "Foco/Ampliação": ["mecanismo","engrenagens","seletores"], "Mecânico": ["braço","suporte","articulações"], "Imagem Digital": ["câmera","sensor","cabo","software"]},
        "relacoes": [("Fonte de luz","Campo","ilumina"),("Campo","Lentes","fornece luz refletida"),("Lentes","Foco","formam imagem"),("Foco","Ocular/Câmera","entrega imagem nítida"),("Braço","Sistema óptico","mantém posicionamento")],
        "diagrama": """FONTE DE LUZ → ILUMINAÇÃO → CAMPO
                              ↓
CAMPO → LUZ REFLETIDA → LENTES → FOCO/AMPLIAÇÃO → OCULAR/CÂMERA
                                                        ↓
                                                     IMAGEM""",
        "falhas": {"Iluminação": ["Campo escuro", "Intensidade irregular"], "Óptico": ["Imagem turva", "Sujeira/dano"], "Foco/Ampliação": ["Não focaliza", "Ampliação irregular"], "Mecânico": ["Folga", "Instabilidade", "Desalinhamento"], "Imagem Digital": ["Sem imagem na tela", "Artefatos digitais"]},
        "testes": [("Imagem direta está boa e digital ruim?", "Separar cadeia óptica de câmera/software."), ("A nitidez muda com distância de trabalho?", "Investigar foco/posicionamento antes de assumir defeito óptico."), ("Iluminação muda sem alterar foco?", "Separar subsistema de iluminação."), ("Há folga mecânica?", "Instabilidade pode simular problema óptico.")],
        "arvore": """IMAGEM RUIM
├── Iluminação adequada?
│   ├── Não → fonte/driver/caminho óptico
│   └── Sim → foco correto?
│             ├── Não → posicionamento/mecanismo
│             └── Sim → lente limpa/íntegra?
│                       ├── Não → procedimento de limpeza autorizado
│                       └── Sim → alinhamento/câmera/óptica especializada""",
        "validacao": ["Iluminação uniforme", "Foco e ampliação funcionais", "Imagem estável", "Movimento mecânico sem folgas anormais", "Captura digital, quando aplicável"]
    }
}


# ==========================================================
# V4 - FUNDAMENTOS, COMPONENTES INTERATIVOS E ANATOMIA
# ==========================================================
COMPONENTES_BASE = {
    "Amplificador diferencial": {
        "o_que_e":"Circuito eletrônico que amplifica principalmente a diferença de tensão entre duas entradas e reduz, dentro dos seus limites, sinais presentes de forma semelhante nas duas entradas.",
        "como_funciona":"Ele recebe dois sinais, compara V+ e V− e produz uma saída proporcional à diferença. Em equipamentos biomédicos, isso é importante porque o sinal útil pode ser pequeno e o ambiente pode introduzir ruído comum aos dois condutores.",
        "fisica":"Lei de Ohm, circuitos diferenciais e amplificação. A rejeição de modo comum é uma característica real, mas não elimina qualquer interferência.",
        "no_equipamento":"No ECG, integra a etapa analógica inicial que recebe os biopotenciais antes do processamento digital.",
        "falhas":"Saturação, ganho incorreto, ruído, conexão defeituosa ou falha na alimentação podem alterar o sinal. Sempre separar entrada, amplificação e processamento.",
        "revisar":"Entrada → proteção → amplificador diferencial → filtros → ADC/processamento."
    },
    "Relé": {
        "o_que_e":"Chave eletromecânica controlada eletricamente. Um circuito de comando energiza uma bobina e o campo magnético movimenta contatos para abrir ou fechar outro circuito.",
        "como_funciona":"Corrente na bobina → campo magnético → armadura móvel → mudança dos contatos. Assim, uma placa de baixa potência pode comandar uma carga maior, respeitando o projeto.",
        "fisica":"Eletromagnetismo e conversão de energia elétrica em movimento mecânico.",
        "no_equipamento":"Pode aparecer no acionamento de resistência, motor ou outros atuadores, dependendo do projeto.",
        "falhas":"Contato queimado/oxidado, bobina aberta, contato travado ou falha do sinal de comando.",
        "revisar":"Comando ≠ potência: confirmar primeiro se o relé recebe comando e depois se seus contatos entregam energia à carga."
    },
    "Filtro passa-baixa": {
        "o_que_e":"Filtro que permite a passagem das frequências abaixo de uma frequência de corte e atenua progressivamente frequências acima dela.",
        "como_funciona":"Pode ser implementado com componentes passivos ou circuitos ativos. Em sinais biomédicos, ajuda a limitar componentes de alta frequência antes ou depois da digitalização.",
        "fisica":"Resposta em frequência. A frequência de corte não significa bloqueio instantâneo: existe uma região de transição e uma inclinação de atenuação.",
        "no_equipamento":"Pode ser usado em cadeias de aquisição como o ECG, conforme a arquitetura e finalidade do filtro.",
        "falhas":"Corte inadequado pode deixar ruído passar ou remover informação relevante.",
        "revisar":"Baixa frequência passa; alta frequência é atenuada."
    },
    "Filtro passa-alta": {
        "o_que_e":"Filtro que atenua componentes abaixo da frequência de corte e permite a passagem das componentes acima dela.",
        "como_funciona":"Pode reduzir variações muito lentas e componentes de baixa frequência, como derivações de linha de base, dependendo da aplicação.",
        "fisica":"Resposta em frequência e frequência de corte.",
        "no_equipamento":"Pode integrar condicionamento de sinais analógicos, especialmente quando há necessidade de reduzir componentes muito lentas.",
        "falhas":"Um corte excessivo pode distorcer sinais de interesse.",
        "revisar":"Alta frequência passa; baixa frequência é atenuada."
    },
    "Filtro passa-faixa": {
        "o_que_e":"Combinação funcional que privilegia uma faixa de frequências e atenua componentes abaixo e acima dela.",
        "como_funciona":"Pode resultar da associação de comportamento passa-alta e passa-baixa ou de outras topologias.",
        "fisica":"Define uma banda de interesse por limites inferior e superior.",
        "no_equipamento":"Útil quando o sistema precisa priorizar uma faixa de sinal conhecida.",
        "falhas":"Faixa mal definida pode reduzir informação ou manter ruído indesejado.",
        "revisar":"Frequência baixa demais ↓ | faixa de interesse ✓ | frequência alta demais ↓."
    },
    "Filtro rejeita-faixa / notch": {
        "o_que_e":"Filtro projetado para atenuar uma faixa estreita ou uma frequência específica.",
        "como_funciona":"É usado quando existe uma interferência conhecida que se deseja reduzir, sem necessariamente remover todas as frequências próximas.",
        "fisica":"Atenuação seletiva em frequência.",
        "no_equipamento":"Em ECG, pode ser associado à redução de interferência de rede, conforme projeto e configuração. Seu uso deve ser entendido porque filtragem também pode modificar o traçado.",
        "falhas":"Uso excessivo ou inadequado pode mascarar informação e não substitui a identificação da fonte do ruído.",
        "revisar":"Filtrar não é o mesmo que eliminar a causa da interferência."
    },
    "Conversor A/D": {
        "o_que_e":"Circuito que transforma um sinal analógico contínuo em representação digital.",
        "como_funciona":"O sistema amostra o sinal em intervalos e quantiza sua amplitude em níveis digitais. Taxa de amostragem e resolução influenciam a representação.",
        "fisica":"Amostragem, quantização e processamento digital de sinais.",
        "no_equipamento":"Após o condicionamento analógico, permite que processadores armazenem, exibam e analisem sinais.",
        "falhas":"Problemas de referência, clock, resolução ou processamento podem gerar comportamento incorreto.",
        "revisar":"Analógico → amostragem → quantização → dados digitais."
    },
    "Sensor": {
        "o_que_e":"Elemento que transforma uma grandeza física em um sinal utilizável pelo sistema.",
        "como_funciona":"Temperatura, pressão, posição ou outra variável altera uma propriedade física e o circuito converte essa alteração em informação.",
        "fisica":"Depende do tipo: resistivo, termistor, termopar, pressão, óptico, magnético etc.",
        "no_equipamento":"Fecha o ciclo de controle: processo → sensor → controlador → atuador → processo.",
        "falhas":"Sensor pode estar correto e a leitura exibida errada por falha de cabo, condicionamento, ADC ou software.",
        "revisar":"Não confunda: grandeza real, sinal do sensor e valor exibido são três etapas diferentes."
    },
    "Controlador eletrônico": {
        "o_que_e":"Parte responsável por receber informações, aplicar lógica e comandar atuadores.",
        "como_funciona":"Entrada de sensores/comandos → lógica programada ou analógica → saída para driver, relé, motor, válvula ou resistência.",
        "fisica":"Eletrônica, lógica de controle e sistemas em malha aberta ou fechada.",
        "no_equipamento":"É o centro da decisão, mas não deve ser culpado antes de verificar entradas e saídas.",
        "falhas":"Entrada incorreta, alimentação, software, saída de acionamento ou comunicação.",
        "revisar":"Pergunte: o controlador recebeu a informação correta? tomou a decisão correta? entregou o comando?"
    },
    "Resistência / sistema de aquecimento": {
        "o_que_e":"Elemento que converte energia elétrica em energia térmica por efeito Joule.",
        "como_funciona":"A corrente atravessa um material resistivo e parte da energia elétrica é dissipada como calor.",
        "fisica":"Efeito Joule; potência elétrica depende das relações entre tensão, corrente e resistência.",
        "no_equipamento":"Autoclaves e outros sistemas térmicos usam aquecimento controlado para atingir condições definidas.",
        "falhas":"Elemento aberto, conexão, relé/driver, proteção térmica ou comando.",
        "revisar":"Comando → potência → resistência → transferência de calor → sensor → controle."
    },
    "Motor": {
        "o_que_e":"Conversor eletromecânico que transforma energia elétrica em movimento.",
        "como_funciona":"O projeto do motor utiliza campos elétricos e magnéticos para produzir torque e rotação ou outro movimento.",
        "fisica":"Eletromagnetismo e conversão eletromecânica.",
        "no_equipamento":"Pode movimentar compressor, bomba, ventilador ou mecanismos.",
        "falhas":"Alimentação, comando, circuito de partida, enrolamentos, rolamentos ou carga mecânica excessiva.",
        "revisar":"Motor não gira não significa automaticamente motor defeituoso."
    },
    "Válvula": {
        "o_que_e":"Elemento que controla, direciona, interrompe ou protege o fluxo de um fluido ou gás.",
        "como_funciona":"Uma abertura controlada altera o caminho disponível ao fluxo. Pode ser manual, mecânica, pneumática ou solenóide, conforme o equipamento.",
        "fisica":"Pressão, diferença de pressão, vazão e resistência ao fluxo.",
        "no_equipamento":"Autoclaves, compressores e equipamentos odontológicos podem possuir diferentes tipos de válvulas.",
        "falhas":"Obstrução, vazamento, travamento, comando ausente ou desgaste de vedação.",
        "revisar":"Verifique o fluxo real e não apenas se existe comando elétrico."
    },
    "Fonte de luz": {
        "o_que_e":"Subsistema que fornece energia luminosa ao campo observado.",
        "como_funciona":"Energia elétrica é convertida em luz por uma tecnologia de iluminação; a óptica direciona essa luz.",
        "fisica":"Óptica, emissão luminosa, intensidade e distribuição da luz.",
        "no_equipamento":"No colposcópio, iluminação é parte da cadeia de formação da imagem.",
        "falhas":"Fonte, driver, conexão, guia óptico ou controle de intensidade.",
        "revisar":"Sem iluminação adequada, a óptica pode estar perfeita e a imagem ainda ser inadequada."
    }
}

ANATOMIA = {
    "♨️ Autoclave": {"sistema":"Não mede diretamente uma função anatômica; atua sobre instrumentos e materiais usados no cuidado ao paciente.","relacao":"A relação com o corpo humano é indireta e ocorre pela prevenção de transmissão de microrganismos. O entendimento básico de microbiologia e barreiras de controle de infecção é mais relevante que uma anatomia de órgão específico.","conexao":"Paciente → procedimento → instrumentos/material → processamento correto → redução do risco associado ao reuso."},
    "📈 Eletrocardiógrafo": {"sistema":"Sistema cardiovascular e sistema de condução elétrica cardíaca.","relacao":"O nó sinoatrial inicia a ativação elétrica fisiológica; a condução pelo miocárdio produz campos elétricos que resultam em diferenças de potencial detectáveis na superfície corporal. O ECG registra essas diferenças por eletrodos.","conexao":"Coração → atividade elétrica → propagação pelo volume condutor corporal → pele → eletrodos → cabos → aquisição eletrônica → traçado."},
    "💨 Compressor": {"sistema":"Não mede diretamente anatomia humana; fornece ar comprimido para sistemas que podem ser utilizados em procedimentos clínicos/odontológicos.","relacao":"No contexto odontológico, sua relação é indireta: o ar comprimido permite o funcionamento de instrumentos que atuam na cavidade oral. A segurança depende da qualidade do ar e da aplicação prevista.","conexao":"Compressor → tratamento/distribuição do ar → equipamento odontológico → instrumento → procedimento no paciente."},
    "❄️ Câmara fria / Câmara de vacina": {"sistema":"Relação indireta com imunologia e conservação de produtos biológicos.","relacao":"O equipamento não atua diretamente no corpo, mas mantém condições ambientais necessárias para preservar produtos utilizados posteriormente em pacientes.","conexao":"Controle térmico → conservação do produto → manutenção das características especificadas → aplicação clínica conforme protocolo."},
    "🦷 Cadeira e caneta odontológica": {"sistema":"Cavidade oral, dentes, periodonto e estruturas associadas.","relacao":"A cadeira posiciona o paciente e os instrumentos realizam funções mecânicas, pneumáticas e hidráulicas relacionadas ao atendimento odontológico. Para engenharia clínica, é essencial entender que pressão, rotação, irrigação e posicionamento afetam diretamente a execução do procedimento.","conexao":"Paciente → posicionamento → acesso ao campo oral → instrumento → energia mecânica/pneumática + irrigação → procedimento."},
    "🔊 Ultrassom odontológico": {"sistema":"Estruturas dentárias e periodontais, conforme a aplicação clínica.","relacao":"O equipamento gera vibração mecânica de alta frequência no inserto; a aplicação clínica ocorre sobre estruturas específicas segundo técnica profissional. A engenharia deve compreender a cadeia física sem extrapolar para decisão clínica.","conexao":"Gerador → transdutor → vibração → inserto + irrigação → interação mecânica no campo odontológico."},
    "🔍 Colposcópio": {"sistema":"Sistema reprodutor feminino, especialmente estruturas observadas durante o exame colposcópico.","relacao":"O equipamento não 'cria' a imagem do tecido: ele ilumina o campo e amplia a luz refletida para permitir observação detalhada. A interpretação anatômica e clínica é responsabilidade profissional específica.","conexao":"Estrutura anatômica → iluminação → reflexão → óptica → ocular/câmera → imagem para observação."}
}

def get_component_knowledge(nome):
    nome_l = nome.lower()
    for chave, dados in COMPONENTES_BASE.items():
        if chave.lower() in nome_l or nome_l in chave.lower():
            return dados
    if "sensor" in nome_l: return COMPONENTES_BASE["Sensor"]
    if "controle" in nome_l or "placa" in nome_l or "controlador" in nome_l: return COMPONENTES_BASE["Controlador eletrônico"]
    if "motor" in nome_l: return COMPONENTES_BASE["Motor"]
    if "válvula" in nome_l: return COMPONENTES_BASE["Válvula"]
    if "resist" in nome_l or "aquec" in nome_l: return COMPONENTES_BASE["Resistência / sistema de aquecimento"]
    if "luz" in nome_l: return COMPONENTES_BASE["Fonte de luz"]
    return {"o_que_e":"Componente específico do equipamento.","como_funciona":"Sua operação exata depende do projeto do fabricante e deve ser correlacionada ao diagrama técnico.","fisica":"Identifique a energia de entrada, transformação e saída.","no_equipamento":"Analise sua posição na cadeia funcional.","falhas":"Separe comando, alimentação, componente e carga.","revisar":"Onde este componente recebe energia/informação e para onde ele envia?"}

def render_componentes_interativos_v4(componentes, nome_eq):
    st.markdown("## 🔧 Laboratório de componentes interativos")
    st.caption("Escolha um componente. A ideia é revisar desde os fundamentos: o que é → como funciona → física → papel no equipamento → falhas.")
    nomes = [c[0] for c in componentes]
    selecionado = st.selectbox("🎯 Selecione um componente", nomes, key=f"comp_select_{nome_eq}")
    item = next(c for c in componentes if c[0] == selecionado)
    nome, funcao, diagnostico = item
    base = get_component_knowledge(nome)
    st.markdown(f"### {nome}")
    cols = st.columns(2)
    with cols[0]:
        st.info(f"**Função neste equipamento:** {funcao}")
        st.markdown("#### ⚙️ Como funciona")
        st.write(base["como_funciona"])
        st.markdown("#### ⚛️ Física e engenharia")
        st.write(base["fisica"])
    with cols[1]:
        st.markdown("#### 🧩 O que é")
        st.write(base["o_que_e"])
        st.markdown("#### 🏥 Papel no equipamento")
        st.write(base["no_equipamento"])
        st.markdown("#### ⚠️ Como pensar na falha")
        st.write(diagnostico)
    with st.expander("🧠 Revisão rápida: o que preciso lembrar?"):
        st.write(base["revisar"])
        st.write("**Falhas típicas:** " + base["falhas"])
    st.divider()
    st.markdown("### 📚 Glossário de eletrônica clínica")
    fundamentos = ["Amplificador diferencial", "Relé", "Filtro passa-baixa", "Filtro passa-alta", "Filtro passa-faixa", "Filtro rejeita-faixa / notch", "Conversor A/D", "Sensor", "Controlador eletrônico"]
    escolha = st.selectbox("Relembrar um fundamento", fundamentos, key=f"fund_{nome_eq}")
    d = COMPONENTES_BASE[escolha]
    with st.expander(f"📖 {escolha}", expanded=True):
        st.markdown(f"**O que é:** {d['o_que_e']}")
        st.markdown(f"**Como funciona:** {d['como_funciona']}")
        st.markdown(f"**Física:** {d['fisica']}")
        st.markdown(f"**Aplicação:** {d['no_equipamento']}")

def render_fundamentos_v4(nome):
    st.markdown("## 🧠 Fundamentos para quem está começando")
    st.markdown("Esta aba existe para conectar o equipamento à base da Engenharia Biomédica. Antes de decorar defeitos, entenda os blocos fundamentais.")
    blocos = [
        ("⚡ Energia elétrica", "Tensão é diferença de potencial; corrente é movimento de carga; resistência se opõe ao fluxo. Em diagnóstico, pergunte sempre: existe alimentação? a tensão chega? a carga responde?"),
        ("🔁 Sinais analógicos e digitais", "Um sensor pode produzir um sinal contínuo. O condicionamento ajusta esse sinal; o conversor A/D permite processamento digital."),
        ("🎛️ Ganho e amplificação", "Amplificar é aumentar a amplitude de um sinal. Ganho inadequado pode fazer um sinal parecer maior ou menor sem que o fenômeno físico tenha mudado."),
        ("📈 Frequência e filtros", "Passa-baixa reduz altas frequências; passa-alta reduz baixas; passa-faixa privilegia uma banda; notch/rejeita-faixa reduz uma região específica."),
        ("🔄 Controle em malha fechada", "Grandeza real → sensor → controlador → atuador → processo → nova medição. Temperatura, pressão e outros processos podem usar esse princípio."),
        ("🧲 Eletromagnetismo", "Motores e relés utilizam campos eletromagnéticos para produzir movimento ou comutação. Interferências também podem ocorrer por acoplamento elétrico ou magnético."),
        ("🛡️ Segurança", "Em equipamentos de saúde, desempenho não basta. Qualquer intervenção deve respeitar fabricante, procedimento, isolamento, aterramento, proteções e testes aplicáveis.")
    ]
    for t, txt in blocos:
        with st.expander(t): st.write(txt)

def render_anatomia_v4(nome):
    dados = ANATOMIA.get(nome)
    st.markdown("## 🫀 Relação com anatomia e fisiologia")
    if not dados:
        st.info("Relação anatômica a ser adicionada.")
        return
    st.markdown("### Sistema ou contexto biológico")
    st.write(dados["sistema"])
    st.markdown("### Como o equipamento se relaciona com o corpo humano")
    st.write(dados["relacao"])
    st.markdown("### Cadeia corpo ↔ tecnologia")
    st.info(dados["conexao"])
    st.warning("⚠️ Esta seção explica a relação técnico-biológica. Diagnóstico e interpretação clínica não devem ser inferidos apenas pelo funcionamento do equipamento.")


def render_fisica_avancada(info):
    st.markdown(info["fisica"])

def render_funcionamento_interno(info):
    st.markdown("## Funcionamento interno passo a passo")
    for i, (etapa, descricao) in enumerate(info["interno"], 1):
        with st.expander(f"{i}. {etapa}", expanded=(i == 1)):
            st.write(descricao)

def render_mapa_subsistemas(info):
    st.markdown("## Mapa de subsistemas")
    for subsistema, itens in info["subsistemas"].items():
        st.markdown(f"### 🔹 {subsistema}")
        st.markdown(" → ".join(itens))

def render_componentes_interativos(componentes):
    st.markdown("## Componentes interativos")
    st.caption("Clique em cada componente para abrir sua função e relação com o diagnóstico.")
    for nome, funcao, diagnostico in componentes:
        with st.expander(f"🔧 {nome}"):
            st.markdown(f"**Função:** {funcao}")
            st.markdown(f"**Impacto diagnóstico:** {diagnostico}")

def render_relacoes(info):
    st.markdown("## Relação entre componentes")
    for origem, destino, relacao in info["relacoes"]:
        st.markdown(f"**{origem}** ── *{relacao}* ──▶ **{destino}**")

def render_diagrama(info):
    st.markdown("## Diagrama funcional")
    st.code(info["diagrama"], language=None)

def render_falhas_subsistema(info):
    st.markdown("## Falhas organizadas por subsistema")
    for subsistema, falhas in info["falhas"].items():
        with st.expander(f"⚠️ {subsistema}"):
            for falha in falhas:
                st.markdown(f"- {falha}")

def render_testes_hipoteses(info):
    st.markdown("## Testes para diferenciar hipóteses")
    for pergunta, interpretacao in info["testes"]:
        st.markdown(f"**Teste/observação:** {pergunta}")
        st.info(interpretacao)

def render_arvore(info):
    st.markdown("## Árvore de decisão")
    st.code(info["arvore"], language=None)

def render_validacao(info):
    st.markdown("## Validação pós-manutenção")
    st.warning("A validação deve seguir manual do fabricante, procedimento institucional, competência técnica e requisitos de segurança aplicáveis.")
    for i, item in enumerate(info["validacao"], 1):
        st.checkbox(item, key=f"valid_{item}")


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
    avancado = TECNICO.get(nome)
    tabs = st.tabs([
        "📚 Visão geral", "🧠 Fundamentos", "🫀 Anatomia", "⚛️ Princípios físicos",
        "🔬 Funcionamento interno", "🧩 Subsistemas", "🔧 Componentes interativos",
        "🔗 Relações", "📊 Diagrama funcional", "⚠️ Falhas", "🧪 Testes",
        "🌳 Árvore de decisão", "✅ Validação", "🛠️ Problemas"
    ])
    with tabs[0]:
        st.markdown("## O que é e para que serve?")
        st.markdown(info["objetivo"])
        st.markdown("## Como desenvolver o raciocínio técnico")
        render_raciocinio(info["raciocinio"])
    with tabs[1]: render_fundamentos_v4(nome)
    with tabs[2]: render_anatomia_v4(nome)
    with tabs[3]:
        if avancado: render_fisica_avancada(avancado)
        if nome == "📈 Eletrocardiógrafo":
            st.divider(); st.markdown(info["interferencia"])
    with tabs[4]:
        if avancado: render_funcionamento_interno(avancado)
        st.divider(); st.markdown("## Cadeia de funcionamento"); st.markdown(info["principio"])
    with tabs[5]:
        if avancado: render_mapa_subsistemas(avancado)
    with tabs[6]: render_componentes_interativos_v4(info["componentes"], nome)
    with tabs[7]:
        if avancado: render_relacoes(avancado)
    with tabs[8]:
        if avancado: render_diagrama(avancado)
    with tabs[9]:
        if avancado: render_falhas_subsistema(avancado)
    with tabs[10]:
        if avancado: render_testes_hipoteses(avancado)
    with tabs[11]:
        if avancado: render_arvore(avancado)
    with tabs[12]:
        if avancado: render_validacao(avancado)
    with tabs[13]:
        st.markdown("## Biblioteca de problemas")
        busca = st.text_input("🔎 Pesquisar", placeholder="Ex.: vazamento, não aquece, ruído, temperatura...", key=f"busca_{nome}").lower()
        encontrados = [p for p in info["problemas"] if not busca or busca in (p["titulo"] + p["sintoma"] + " ".join(p["causas"])).lower()]
        if not encontrados: st.info("Nenhum problema encontrado.")
        else:
            escolha = st.selectbox("Selecione o problema", [p["titulo"] for p in encontrados], key=f"problema_{nome}")
            render_problema(next(p for p in encontrados if p["titulo"] == escolha))

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
st.sidebar.caption("Guia de Campo V4")

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
