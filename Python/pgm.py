import datetime

consultas = []
especialidades = {
    "1": "Arritmologia",
    "2": "Cardiologia",
    "3": "Cardiologia Pediátrica",
    "4": "Gastroenterologia",
    "5": "Hematologia",
    "6": "Infectologia",
    "7": "Mastologia",
    "8": "Nefrologia",
    "10": "Oncologia",
    "11": "Ortopedia",
    "12": "Pediatria",
    "13": "Proctologia",
}

orientacoes = {
    "Arritmologia": "Trata batimentos cardíacos irregulares (arritmias).",
    "Cardiologia": "Cuida do coração e circulação.",
    "Cardiologia Pediátrica": "Cuida do coração de crianças.",
    "Gastroenterologia": "Trata o sistema digestivo.",
    "Hematologia": "Trata doenças do sangue.",
    "Infectologia": "Trata infecções causadas por vírus, bactérias etc.",
    "Mastologia": "Cuida da saúde das mamas.",
    "Nefrologia": "Trata doenças dos rins.",
    "Oncologia": "Cuida do tratamento do câncer.",
    "Ortopedia": "Trata ossos, músculos e articulações.",
    "Pediatria": "Cuida da saúde de crianças e adolescentes.",
    "Proctologia": "Trata doenças do reto, ânus e intestino grosso."
}

endereco_clinica = "R. Dr. Ovídio Pires de Campos, 225 - Cerqueira César, São Paulo - SP"

while True:
    print("\n--- MENU ---")
    print("1 - Agendar Consulta")
    print("2 - Cancelar ou Remarcar Consulta")
    print("3 - Ver Especialidades Médicas")
    print("4 - Ver Orientações Pré-Consulta")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        if not nome:
            print("Nome não pode ser vazio.")
            continue

        print("\nEspecialidades disponíveis:")
        for codigo, esp in especialidades.items():
            print(f"{codigo} - {esp}")

        escolha = input("Escolha uma especialidade (número): ")
        especialidade = especialidades.get(escolha)
        if not especialidade:
            print("Especialidade inválida.")
            continue

        data = input("Informe a data da consulta (dd/mm/aaaa): ")
        try:
            data_validada = datetime.datetime.strptime(data, "%d/%m/%Y").date()
            if data_validada < datetime.date.today():
                print("Data no passado.")
                continue
        except ValueError:
            print("Data inválida.")
            continue

        horario = input("Informe o horário da consulta (hh:mm): ")
        try:
            datetime.datetime.strptime(horario, "%H:%M")
        except ValueError:
            print("Horário inválido.")
            continue

        consultas.append({
            "nome": nome,
            "especialidade": especialidade,
            "data": data,
            "horario": horario
        })

        print(f"Consulta agendada com sucesso para {nome} em {data} às {horario} ({especialidade}).")

    elif opcao == "2":
        if not consultas:
            print("Nenhuma consulta agendada.")
            continue

        print("\nConsultas Agendadas:")
        for i, c in enumerate(consultas, 1):
            print(f"{i}. {c['nome']} - {c['especialidade']} - {c['data']} às {c['horario']}")

        try:
            idx = int(input("Digite o número da consulta para cancelar/remarcar: ")) - 1
            if idx < 0 or idx >= len(consultas):
                print("Consulta não encontrada.")
                continue
        except ValueError:
            print("Entrada inválida.")
            continue

        opc = input("Deseja [C]ancelar ou [R]emarcar? ").strip().upper()
        if opc == "C":
            consultas.pop(idx)
            print("Consulta cancelada.")
        elif opc == "R":
            nova_data = input("Nova data (dd/mm/aaaa): ")
            try:
                nova_data_validada = datetime.datetime.strptime(nova_data, "%d/%m/%Y").date()1
                if nova_data_validada < datetime.date.today():
                    print("Data no passado.")
                    continue
            except ValueError:
                print("Data inválida.")
                continue

            novo_horario = input("Novo horário (hh:mm): ")
            try:
                datetime.datetime.strptime(novo_horario, "%H:%M")
            except ValueError:
                print("Horário inválido.")
                continue

            consultas[idx]["data"] = nova_data
            consultas[idx]["horario"] = novo_horario
            print("Consulta remarcada com sucesso.")
        else:
            print("Opção inválida.")

    elif opcao == "3":
        print("\nEspecialidades disponíveis:")
        for esp in especialidades.values():
            print(f"- {esp}")

    elif opcao == "4":
        print("\nOrientações pré-consulta:")
        for esp, orientacao in orientacoes.items():
            print(f"{esp}: {orientacao}")

    elif opcao == "5":
        print(f"\nEndereço da clínica: {endereco_clinica}")

    elif opcao == "0":
        print("Encerrando programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
