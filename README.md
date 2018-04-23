# -FLOW-transpufal
Projeto para o processo de seleção do grupo FLOW, feito por Pedro Henrique Rodrigues Meira Bastos, aluno do teceiro semestre de engenharia civil.

A ideia inicial seria criar uma plataforma pela qual discentes e docentes poderiam interagir de forma mais direta em relação a seus processos administrativos, como quebra de pré-requisito, reaproveitamento de matérias, etc, é fácil ver que muitos professores membros dos colegiados no CTEC (e não apenas do CTEC) tem problemas lidando com pilhas e pilhas de documentos, e como confirmad pelo professor Roberto Barbosa, membro do colegiado de Engenharia Civil, uma ferramenta pela qual o professor pudesse consultar tais documentos digatalmente seria muito mais conveniente, e agilizaria os processos, pro bem de ambos alunos e professores.


Dito isso, o projeto teve um desenvolvimento conturbado: um aparente sem-número de provas e trabalhos acadêmicos gastou parte significativa do prazo oferecido para terminar esse programa (basicamente apenas esse final de semana livre), e a situação "agrava ainda mais" considerando que era o aluno responsável por esse projeto tinha pouco ou nenhum com as ferramentas a serem utilizadas: Python, Django e HTML, sendo esse o primeiro projeto relacionado a Web que ele fez.

Sem mais delongas, seguem as instruções para usar o código:

#### iniciando um serivdor #####
Dentro do diretório do projeto, o usuário deverá iniciar o servidor de desenvolvimento, através do comando (no Linux): 
>>python3 manage.py runserver

Feito isso, o usuário poderá acessar o site que está, por padrão do Django, hosteado localmente. O Django permite outras opções de hosteamento, para que mais usuários possam acessar a plataforma, mas dado o caráter demonstrativo desse projeto, e o seu estado ainda muito infante, isso não será necessário. Quando o servidor for iniciado, poderá ser copiado do terminal o link para acessar o site, que provavelmente será o http://127.0.0.1:8000.

#### criando conta de administrador ####
Logo de cara, o usuário irá deparar com uma tela de login: dado o caráter acadêmico do sistema, achou-se inapropriado deixar qualquer um simplesmente entrar no site e criar uma conta para acessar os documentos, então apenas o administrador poderá usar criar contas e gerenciar processos. Para criar uma conta de administrador, é necessário o comando (no Linux):
>>python3 manage.py createsuperuser
OBS.: o servidor tem que estar desligado para criar contas de administrador.

O processo de criação automático, todo o passo a passo será mostrado no terminal, pedindo nume do usuário, senha, confirmação da senha, e email. Novamente, dado o caráter demonstrativo do código, pode escrever nomes, senhas e emails genéricos como admin e admin123456 e admin@admin.com.

Feito isso, o usuário poderá acessar a página de administrador com o link:
>>http://127.0.0.1:8000/admin
Ali ele escreverá o seu username e senha, e então o usuário terá total acesso a administração dos site, poderá criar contas de usuário comuns, grupos, ceder permissões para as ditas categorias, e criar processos e categorias para separar os processos.

#### os processos ####
Todo processo tem nome, código de identificação, categória, arquivo e status:
> Nome: o nome do processo
> Código de Identificação: um número para identificar o processo
> Categória: o tipo de processo: reaproveitamento de matéria, transferência, etc, etc.
> Arquivo: um arquivo, de preferência PDF, com os documentos necessários para o trâmite do processo
> Status: indica se o processo já foi concluído ou não

Criar processos e categorias é bem fácil através da página do adminstrador.

#### login e logout ####
Como dito anteriormente, o administador pode criar usuários e grupos. Para logar e deslogar no site, basta acessar a página de login através do link http://127.0.0.1:8000. Ali o usuário poderá acessar os processos, ver quantos existem, quantos foram resolvidos e quantas vezes ele já visitou a página.

#### o bug e futuros ajustes ####
Existe um bug bem desagradável ainda a ser resolvido: se o usuário abrir a página de processos, escolher um deles e tentar baixar o documento através do link fornecido, a página irá retornar com o erro 404, por algum motivo, o site não direciona para a localização do documento, procurando um endereço que não existe e retornando o erro.

O projeto ainda pode ser muito expandido, pode ser criado uma diferenciação entre contas de alunos e professores, alunos podendo enviar documentos por intermédio da plataforma, assim ele estaria mais próximo da proposta inicial, e a partir dela, o projeto poderia crescer em várias direções: implementação de filtros, de chat direto entre aluno e professor, atribuição de processos a determinados professores, etc, etc, etc, o Django vai permitir essa rápida expansão.


#### agradecimentos ####
Agradeço a equipe do FLOW pela oportunidade do processo e de seleção, e agradeço ao pessoal do Django e Python por fornecer uma documentação muito bem explicada, e pelo tutorial disponível no site do Django por muitas vezes "quebrando o galho". Outra ajuda muitíssimo grande veio da plataforma de desenvolvimento da Mozilla, que contém vários tutorais para desenvolvedores, incluindo Django.
