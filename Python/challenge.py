import datetime
import os

consultas = []

especialidades = {
    "1": "Arritmologia", "2": "Cardiologia", 
    "3": "Cardiologia Pediátrica", "4": "Endocrinologia",
    "5": "Gastroenterologia", "6": "Ginecologia", 
    "7": "Infectologia", "8": "Mastologia",
    "9": "Nefrologia", "10": "Neurologia", 
    "11": "Oftalmologia", "12": "Oncologia",
    "13": "Oncologia Pediátrica", "14": "Ortopedia", 
    "15": "Otorrinolaringologia", "16": "Patologia Clínica",
    "17": "Pediatria Geral", "18": "Pneumologia", 
    "19": "Pronto-Socorro", "20": "Psicologia Clínica",
    "21": "Psiquiatria", "22": "Quimioterapia", 
    "23": "Radiologia", "24": "Reabilitação",
    "25": "Tocoginecologia", "26": "Transplantes", 
    "27": "Urologia",
}

orientacoes = {
    "1 : Arritmologia": "Trata distúrbios do ritmo cardíaco, como taquicardia e fibrilação atrial.", "2 : Cardiologia": "Cuida do diagnóstico e tratamento de doenças do coração e vasos sanguíneos.",
    "3 : Cardiologia Pediátrica": "Foca em doenças cardíacas congênitas ou adquiridas em crianças.", "4 : Endocrinologia": "Trata doenças hormonais, como diabetes, tireoide e obesidade.",
    "5 : Gastroenterologia": "Lida com doenças do sistema digestivo, como gastrite, refluxo e fígado.", "6 : Ginecologia": "Cuida da saúde do sistema reprodutor feminino.",
    "7 : Infectologia": "Diagnostica e trata infecções causadas por vírus, bactérias e outros agentes.", "8 : Mastologia": "Especializa-se na saúde das mamas, incluindo prevenção e tratamento do câncer de mama.",
    "9 : Nefrologia": "Trata doenças dos rins, como insuficiência renal e nefrites.", "10 : Neurologia": "Cuida de distúrbios do sistema nervoso, como AVC, epilepsia e esclerose múltipla.",
    "11 : Oftalmologia": "Trata doenças dos olhos e problemas de visão.", "12 : Oncologia": "Diagnostica e trata o câncer em adultos.",
    "13 : Oncologia Pediátrica": "Cuida do tratamento de câncer em crianças.", "14 : Ortopedia": "Trata lesões e doenças dos ossos, músculos e articulações.",
    "15 : Otorrinolaringologia": "Cuida do ouvido, nariz e garganta.", "16 : Patologia Clínica": "Analisa exames laboratoriais para ajudar no diagnóstico de doenças.",
    "17 : Pediatria Geral": "Acompanha a saúde e desenvolvimento de crianças e adolescentes", "18 : Pneumologia": "Trata doenças dos pulmões e vias respiratórias, como asma e DPOC.",
    "19 : Pronto-Socorro": "Atende emergências médicas de forma imediata.", "20 : Psicologia Clínica": "Oferece acompanhamento psicológico e tratamento de transtornos emocionais.",
    "21 : Psiquiatria": "Diagnostica e trata transtornos mentais com uso de medicamentos, se necessário.", "22 : Quimioterapia": "Realiza tratamento medicamentoso contra o câncer.",
    "23 : Radiologia": "Usa exames de imagem (como raio-X e tomografia) para diagnóstico.", "24 : Reabilitação": "Promove a recuperação funcional de pacientes com deficiências ou após traumas.",
    "25 : Tocoginecologia": "Junta obstetrícia e ginecologia, cuidando da gravidez e saúde feminina.","26 : Transplantes": "Realiza e acompanha pacientes submetidos a transplantes de órgãos.",
    "27 : Urologia": "Trata doenças do sistema urinário e do aparelho reprodutor masculino.",
}

orientacao_de_preconsulta = {
    "1": "Alergologia:" "Levar exames anteriores relacionados a alergias. Não usar antialérgicos 3 dias antes (se possível), exceto sob orientação médica. Listar alimentos, medicamentos ou substâncias suspeitas de causar reações.", "2": "Trazer exames laboratoriais e cardiológicos recentes. Informar histórico de cirurgias e reações anteriores à anestesia. Jejum conforme orientação (geralmente 8h antes)." ,
    "3": "Cardiologia:" "Levar exames de sangue, eletrocardiograma, ecocardiograma ou testes de esforço anteriores. Anotar sintomas, frequência e fatores associados (ex: dor no peito, falta de ar). Listar todos os medicamentos em uso.", "4": "Levar exames anteriores e histórico do pré-natal e nascimento. Trazer a criança em jejum, se solicitado. Informar histórico familiar de doenças cardíacas.",
    "5": "Levar exames hormonais e de glicemia, TSH, T4, T3, HbA1c etc. Anotar sintomas como ganho/perda de peso, cansaço, alteração no sono. Informar uso de hormônios ou suplementos.", "6": "Jejum de 8 horas se for realizar exames. Levar exames anteriores (endoscopia, colonoscopia, etc.). Anotar sintomas gastrointestinais, duração e relação com alimentos.",
    "7": "Levar exames de Papanicolau, ultrassonografias, mamografias se tiver. Evitar relações sexuais 48h antes se for realizar exame físico. Informar sobre ciclo menstrual e histórico ginecológico", "8": "Levar exames laboratoriais recentes. Informar histórico de infecções, viagens recentes e vacinação. Relatar sintomas atuais com datas de início.",
    "9": "Levar mamografia, ultrassom de mama e exames anteriores. Informar histórico familiar de câncer de mama. Evitar uso de cremes ou desodorantes nas axilas no dia da consulta.", "10": "Levar exames de sangue e urina recentes. Informar uso de medicamentos contínuos. Relatar histórico de hipertensão, diabetes ou infecções urinárias.",
    "11": "Levar exames de imagem (ressonância, tomografia) e laboratoriais. Informar histórico de convulsões, desmaios, dores de cabeça etc. Levar diário de sintomas, se possível.", "12": "Levar exames e histórico de nascimento e desenvolvimento. Vídeos de crises (se houver) podem ajudar o diagnóstico. Levar brinquedos e alimentos para acalmar a criança.",
    "13": "Levar biópsias, exames de imagem, laboratoriais e laudos anteriores. Informar histórico familiar de câncer. Anotar sintomas e tratamentos já realizados.", "14": "Levar todos os exames anteriores e histórico médico completo. A criança deve estar acompanhada de responsável. Levar caderno com dúvidas e informações do dia a dia.",
    "15": "Levar exames de imagem (raios-x, ressonância, tomografia). Usar roupas que permitam fácil acesso à área afetada. Informar sobre cirurgias, quedas, traumas ou dores persistentes.", "16": "Evitar uso de descongestionantes nasais no dia da consulta (se possível).Levar exames de audiometria ou videonasofibroscopia anteriores. Relatar sintomas como zumbido, dor de garganta, obstrução nasal.",
    "17": "Levar cartão de vacinas e histórico de doenças. Informar sobre alimentação, sono, evacuações e comportamento da criança. Anotar dúvidas e trazer exames anteriores.", "18": "Mesmo preparo da pediatria: exames, vacinas e informações sobre desenvolvimento da criança.",
    "19": "Levar exames de imagem e espirometria (se tiver). Informar sobre tosse, falta de ar, tabagismo, alergias. Evitar broncodilatadores 8h antes, se possível.", "20": "Levar documentos e exames anteriores (se disponíveis). Informar medicações em uso, alergias e histórico de doenças.",
    "21": "Refletir sobre os motivos da busca por atendimento. Levar documentos e encaminhamentos, se houver. Estar disposto a falar sobre experiências e sentimentos.", "22": "Levar exames laboratoriais e relatórios psicológicos (se tiver). Informar histórico familiar, uso de substâncias, medicamentos. Ser honesto com sintomas e emoções.",
    "23": "Levar pedido médico e exames anteriores relacionados. Confirmar necessidade de jejum ou preparo específico (como uso de contraste). Informar alergias (especialmente a iodo).", "24": "Levar exames laboratoriais e de imagem anteriores. Relatar sintomas articulares, rigidez matinal, dor crônica. Anotar histórico familiar de doenças autoimunes.",
    "25": "Levar laudos médicos e psicológicos anteriores. Informar dificuldades motoras, cognitivas ou emocionais. Trazer lista de atividades que deseja melhorar.", "26": "Levar todos os exames relacionados ao órgão em questão. Informar histórico familiar e pessoal de doenças crônicas. Estar acompanhado, se possível, para melhor acolhimento.",
    "27": "Levar exames de urina, ultrassom e PSA (se aplicável). Evitar relações sexuais 48h antes se indicado. Informar sintomas urinários ou genitais.",
}


endereco_clinica = "R. Dr. Ovídio Pires de Campos, 225 - Cerqueira César, São Paulo - SP"


def agendar_consulta():
    os.system("cls")
    while True:
        nome = input("Digite o nome do paciente (somente letras): ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
            continue
        if any(char.isdigit() for char in nome):
            print("Nome não pode conter números.")
            continue
        break

    print(f"Agendamento iniciado para o paciente: {nome}")
    for codigo, esp in especialidades.items():
        print(f"{codigo} - {esp}")

    escolha = input("Escolha uma especialidade (número): ")
    especialidade = especialidades.get(escolha)
    if not especialidade:
        print("Especialidade inválida.")
        return

    data = input("Informe a data da consulta (dd/mm/aaaa): ")
    try:
        data_validada = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        if data_validada < datetime.date.today():
            print("Data no passado.")
            return
    except ValueError:
        print("Data inválida.")
        return

    horario = input("Informe o horário da consulta (hh:mm): ")
    try:
        datetime.datetime.strptime(horario, "%H:%M")
    except ValueError:
        print("Horário inválido.")
        return

    consultas.append({
        "nome": nome,
        "especialidade": especialidade,
        "data": data,
        "horario": horario
    })

    print(f"Consulta agendada com sucesso para {nome} em {data} às {horario} ({especialidade}).")


def cancelar_ou_remarcar():
    os.system("cls")
    if not consultas:
        print("Nenhuma consulta agendada.")
        return

    print("\nConsultas Agendadas:")
    for i, c in enumerate(consultas, 1):
        print(f"{i}. {c['nome']} - {c['especialidade']} - {c['data']} às {c['horario']}")

    try:
        idx = int(input("Digite o número da consulta para cancelar/remarcar: ")) - 1
        if idx < 0 or idx >= len(consultas):
            print("Consulta não encontrada.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    opc = input("Deseja [C]ancelar ou [R]emarcar? ").strip().upper()
    if opc == "C":
        consultas.pop(idx)
        print("Consulta cancelada.")
    elif opc == "R":
        nova_data = input("Nova data (dd/mm/aaaa): ")
        try:
            nova_data_validada = datetime.datetime.strptime(nova_data, "%d/%m/%Y").date()
            if nova_data_validada < datetime.date.today():
                print("Data no passado.")
                return
        except ValueError:
            print("Data inválida.")
            return

        novo_horario = input("Novo horário (hh:mm): ")
        try:
            datetime.datetime.strptime(novo_horario, "%H:%M")
        except ValueError:
            print("Horário inválido.")
            return

        consultas[idx]["data"] = nova_data
        consultas[idx]["horario"] = novo_horario
        print("Consulta remarcada com sucesso.")
    else:
        print("Opção inválida.")


def listar_especialidades():
    print("\nEspecialidades disponíveis:")
    for codigo, esp in especialidades.items():
        print(f"{codigo} - {esp}")
    
    escolha = input("Digite o número da especialidade para ver a orientação: ").strip()
    
    especialidade = especialidades.get(escolha)
    if especialidade:
        chave_orientacao = f"{escolha} : {especialidade}"
        orientacao = orientacoes.get(chave_orientacao)  
        if orientacao:
            print(f"\nVocê escolheu: {especialidade}")
            print(f"Orientação: {orientacao}")
        else:
            print("Orientação não encontrada.")
    else:
        print("Código inválido.")

def mostrar_orientacoes_preconsulta():
    print("\nOrientações disponíveis:")
    for codigo, esp in especialidades.items():
        print(f"{codigo} - {esp}")
    
    escolha = input("Digite o número da especialidade para ver a orientação de pré-consulta: ").strip()
    
    especialidade = especialidades.get(escolha)
    if especialidade:
        orientacao = orientacao_de_preconsulta.get(escolha)
        if orientacao:
            print(f"\nVocê escolheu: {especialidade}")
            print(f"Orientação pré-consulta: {orientacao}")
        else:
            print("Orientação de pré-consulta não encontrada.")
    else:
        print("Código inválido.")

def mostrar_endereco():
    os.system("cls")
    print(f"\nEndereço da clínica: {endereco_clinica}")


def menu():
    while True:
        print("\n--- EaseHC ---")
        print("1 - Agendar Consulta")
        print("2 - Cancelar ou Remarcar Consulta")
        print("3 - Ver Especialidades Médicas")
        print("4 - Ver Orientações Pré-Consulta")
        print("5 - Endereço da Clínica")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            agendar_consulta()
        elif opcao == "2":
            cancelar_ou_remarcar()
        elif opcao == "3":
            listar_especialidades()
        elif opcao == "4":
            mostrar_orientacoes_preconsulta()
        elif opcao == "5":
            mostrar_endereco()
        elif opcao == "0":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
