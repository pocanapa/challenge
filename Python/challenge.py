import datetime
import os

consultas = []

especialidades = {
    "1": "Arritmologia", "2": "Cardiologia", "3": "Cardiologia Pediátrica", "4": "Endocrinologia",
    "5": "Gastroenterologia", "6": "Ginecologia", "7": "Infectologia", "8": "Mastologia",
    "9": "Nefrologia", "10": "Neurologia", "11": "Oftalmologia", "12": "Oncologia",
    "13": "Oncologia Pediátrica", "14": "Ortopedia", "15": "Otorrinolaringologia", "16": "Patologia Clínica",
    "17": "Pediatria Geral", "18": "Pneumologia", "19": "Pronto-Socorro", "20": "Psicologia Clínica",
    "21": "Psiquiatria", "22": "Quimioterapia", "23": "Radiologia", "24": "Reabilitação",
    "25": "Tocoginecologia", "26": "Transplantes", "27": "Urologia",
}

orientacoes = {
    "1 : Arritmologia": "Trata distúrbios do ritmo cardíaco, como taquicardia e fibrilação atrial.",
    "2 : Cardiologia": "Cuida do diagnóstico e tratamento de doenças do coração e vasos sanguíneos.",
    "3 : Cardiologia Pediátrica": "Foca em doenças cardíacas congênitas ou adquiridas em crianças.",
    "4 : Endocrinologia": "Trata doenças hormonais, como diabetes, tireoide e obesidade.",
    "5 : Gastroenterologia": "Lida com doenças do sistema digestivo, como gastrite, refluxo e fígado.",
    "6 : Ginecologia": "Cuida da saúde do sistema reprodutor feminino.",
    "7 : Infectologia": "Diagnostica e trata infecções causadas por vírus, bactérias e outros agentes.",
    "8 : Mastologia": "Especializa-se na saúde das mamas, incluindo prevenção e tratamento do câncer de mama.",
    "9 : Nefrologia": "Trata doenças dos rins, como insuficiência renal e nefrites.",
    "10 : Neurologia": "Cuida de distúrbios do sistema nervoso, como AVC, epilepsia e esclerose múltipla.",
    "11 : Oftalmologia": "Trata doenças dos olhos e problemas de visão.",
    "12 : Oncologia": "Diagnostica e trata o câncer em adultos.",
    "13 : Oncologia Pediátrica": "Cuida do tratamento de câncer em crianças.",
    "14 : Ortopedia": "Trata lesões e doenças dos ossos, músculos e articulações.",
    "15 : Otorrinolaringologia": "Cuida do ouvido, nariz e garganta.",
    "16 : Patologia Clínica": "Analisa exames laboratoriais para ajudar no diagnóstico de doenças.",
    "17 : Pediatria Geral": "Acompanha a saúde e desenvolvimento de crianças e adolescentes",
    "18 : Pneumologia": "Trata doenças dos pulmões e vias respiratórias, como asma e DPOC.",
    "19 : Pronto-Socorro": "Atende emergências médicas de forma imediata.",
    "20 : Psicologia Clínica": "Oferece acompanhamento psicológico e tratamento de transtornos emocionais.",
    "21 : Psiquiatria": "Diagnostica e trata transtornos mentais com uso de medicamentos, se necessário.",
    "22 : Quimioterapia": "Realiza tratamento medicamentoso contra o câncer.",
    "23 : Radiologia": "Usa exames de imagem (como raio-X e tomografia) para diagnóstico.",
    "24 : Reabilitação": "Promove a recuperação funcional de pacientes com deficiências ou após traumas.",
    "25 : Tocoginecologia": "Junta obstetrícia e ginecologia, cuidando da gravidez e saúde feminina.",
    "26 : Transplantes": "Realiza e acompanha pacientes submetidos a transplantes de órgãos.",
    "27 : Urologia": "Trata doenças do sistema urinário e do aparelho reprodutor masculino.",
}

orientacoes_preconsulta = {
"1": "Alergologia:" "Leve exames antigos, evite antialérgicos e liste substâncias que causam reação.", "2": "Anestesiologia:" "Leve exames, informe reações anteriores e siga jejum orientado.",
"3": "Cardiologia:" "Leve exames cardíacos, descreva sintomas e informe medicações em uso.", "4": "Cardiologia Pediátrica:" "Leve exames e histórico da criança, jejum se necessário e histórico familiar.",
"5": "Endocrinologia:" "Leve exames hormonais, relate sintomas e uso de hormônios ou suplementos", "6": "Gastroenterologia:" "Jejum se for fazer exame, leve exames prévios e descreva sintomas digestivos.",
"7": "Ginecologia:" "Leve exames ginecológicos, evite relação sexual antes e informe ciclo menstrual.", "8": "Infectologia:" "Leve exames, informe histórico de infecções, viagens e sintomas atuais.",
"9": "Mastologia:" "Leve exames das mamas, informe histórico familiar e não use cremes no dia.", "10": "Nefrologia:" "Leve exames de sangue/urina e informe doenças crônicas ou medicamentos.",
"11": "Neurologia:" "Leve exames de imagem, relate sintomas neurológicos e, se possível, diário de sintomas.", "12": "Neurologia" "Pediátrica: Leve histórico da criança, vídeos de crises e itens para acalmá-la.",
"13": "Oncologia:" "Leve biópsias e exames, informe histórico familiar e tratamentos feitos.", "14": "Oncologia Pediátrica:" "Leve todos os exames da criança, esteja acompanhado e leve anotações.",
"15": "Ortopedia:" "Leve exames de imagem, vista roupas adequadas e relate quedas ou dores.", "16": "Otorrinolaringologia:" "Evite descongestionantes, leve exames e relate sintomas respiratórios.",
"17": "Pediatria:" "Leve cartão de vacinas, exames e informe rotina da criança.", "18":  "Pediatria Geral:" "Siga mesmo preparo da pediatria com exames, vacinas e histórico.",
"19": "Pneumologia:" "Leve exames respiratórios, relate sintomas e evite broncodilatadores.", "20": "Pronto Socorro:" "Leve documentos, exames e informe histórico e medicamentos.",
"21": "Psicologia Clínica:" "Reflita sobre a queixa, leve documentos e esteja aberto ao diálogo.", "22": "Psiquiatria:" "Leve exames/relatórios, informe uso de substâncias e relate emoções com clareza.",
"23": "Radiologia:" "Leve pedido médico e exames anteriores, confirme preparo e informe alergias.", "24": "Reumatologia:" "Leve exames, descreva dores articulares e informe histórico familiar.",
"25": "Terapia Ocupacional:" "Leve laudos, informe dificuldades e objetivos de melhoria.", "26": "Transplantes:" "Leve todos os exames do órgão, informe histórico e vá acompanhado.",
"27": "Urologia:" "Leve exames urinários, evite relações antes e relate sintomas genitais/urinários.",
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
        chave_orientacao = f"{escolha} : {especialidade}"
        orientacao = orientacoes.get(chave_orientacao)
        if orientacao:
            print(f"\nVocê escolheu: {especialidade}")
            print(f"Orientação pré-consulta: {orientacao}")
        else:
            print("Orientação não encontrada.")
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
