package br.com.fiap.application;
import br.com.fiap.domain.*;
import br.com.fiap.repository.AgendamentoRepository;
import br.com.fiap.service.AgendamentoService;
import java.time.LocalDateTime;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada de dados do paciente
        System.out.print("Digite o nome do paciente: ");
        String nomePaciente = scanner.nextLine();

        System.out.print("Digite o CPF do paciente: ");
        String cpfPaciente = scanner.nextLine();

        System.out.print("Digite o número de telefone para contato: ");
        String telefone = scanner.nextLine();

        System.out.print("Digite a especialidade médica necessária (ex: fisioterapia, fonoaudiologia): ");
        String especialidade = scanner.nextLine();

        // Criando paciente
        Usuario paciente = new Usuario(nomePaciente, cpfPaciente, "paciente");

        // Criando unidade (localização)
        Unidade unidade = new Unidade("Hospital das Clínicas de SP", "Rua Dr. Ovídio Pires de Campos, 225 - Cerqueira César, São Paulo - SP");

        // Entrada da data
        System.out.print("Digite a data do agendamento (formato: dd/MM/yyyy): ");
        String dataStr = scanner.nextLine();

        System.out.print("Você prefere agendar na manhã ou tarde? (Digite 'manhã' ou 'tarde'): ");
        String turno = scanner.nextLine().toLowerCase();
        String hora = turno.equals("manhã") ? "09:00" : "14:00";

        // Converter data/hora
        String[] dataPartes = dataStr.split("/");
        String dataFormatada = dataPartes[2] + "-" + dataPartes[1] + "-" + dataPartes[0];
        LocalDateTime dataHora = LocalDateTime.parse(dataFormatada + "T" + hora);

        // Criando agendamento
        Agendamento agendamento = new Agendamento(paciente, dataHora, especialidade);

        // Serviços
        AssistenteVirtual assistente = new AssistenteVirtual();
        AgendamentoRepository repo = new AgendamentoRepository();
        AgendamentoService service = new AgendamentoService(repo, assistente);

        // Agendar
        service.agendar(agendamento);

        // Notificação
        Notificacao notificacao = new Notificacao(
                paciente.getNome(),
                "Olá " + paciente.getNome() + "! Seu atendimento de " + especialidade +
                        " está agendado para " + agendamento.getDataHora(),
                "WhatsApp"
        );
        notificacao.exibirResumo();

        // Confirmar
        service.confirmar(agendamento);

        // Exibir orientações de pré-consulta
        System.out.println("Orientações pré-consulta: " + Orientacao.gerar(especialidade));

        // Exibir localização da unidade
        System.out.println("Local do atendimento: " + unidade.getResumo());

        // Mensagem final
        Mensagem msgFinal = new Mensagem("Esperamos que seu atendimento tenha sido positivo!", "agradecimento");
        System.out.println(msgFinal);

    }
}
