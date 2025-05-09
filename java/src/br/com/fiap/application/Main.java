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

        // Criando paciente e cuidador
        Usuario paciente = new Usuario(nomePaciente, cpfPaciente, "paciente");
        Cuidador cuidador = new Cuidador("Cuidador Responsável", telefone);

        // Dispositivo do paciente
        Dispositivo celular = new Dispositivo("Samsung A10", true);

        // Entrada da data do agendamento
        System.out.print("Digite a data do agendamento (formato: dd/MM/yyyy): ");
        String dataStr = scanner.nextLine();

        // Perguntar se prefere manhã ou tarde
        System.out.print("Você prefere agendar na manhã ou tarde? (Digite 'manhã' ou 'tarde'): ");
        String periodo = scanner.nextLine().toLowerCase();

        // Definir o horário com base na escolha (manhã ou tarde)
        String horaStr = "";
        if ("manhã".equals(periodo)) {
            horaStr = "08:00";  // Agendamento para as 08:00
        } else if ("tarde".equals(periodo)) {
            horaStr = "14:00";  // Agendamento para as 14:00
        } else {
            System.out.println("Período inválido, por padrão o horário será a tarde às 14:00.");
            horaStr = "14:00";
        }

        // Corrigindo a formatação da data de dd/MM/yyyy para yyyy-MM-dd
        String[] dataPartes = dataStr.split("/");  // Dividindo a data em partes (dia, mês, ano)
        String dataFormatada = dataPartes[2] + "-" + dataPartes[1] + "-" + dataPartes[0];  // Formato yyyy-MM-dd

        // Corrigindo a formatação da data e hora para LocalDateTime
        String dataHoraStr = dataFormatada + "T" + horaStr;  // Garantir que "T" separe a data da hora
        LocalDateTime dataHora = LocalDateTime.parse(dataHoraStr);

        // Agendamento com especialidade
        Agendamento agendamento = new Agendamento(paciente, dataHora, especialidade);

        // Componentes de sistema
        AssistenteVirtual assistente = new AssistenteVirtual();
        AgendamentoRepository repo = new AgendamentoRepository();
        AgendamentoService service = new AgendamentoService(repo, assistente);

        // Execução do agendamento
        service.agendar(agendamento);

        // Notificação
        Notificacao notificacao = new Notificacao(
                paciente.getNome(),
                "Olá " + paciente.getNome() + "! Seu atendimento de " + especialidade +
                        " está agendado para " + agendamento.getDataHora(),
                "WhatsApp"
        );
        notificacao.exibirResumo();

        // Cuidador recebe alerta
        cuidador.receberNotificacao("Lembrete: acompanhar " + paciente.getNome() +
                " na consulta de " + especialidade + ".");

        // Confirmação
        service.confirmar(agendamento);

        // Mensagem final
        Mensagem msgFinal = new Mensagem("Esperamos que seu atendimento tenha sido positivo!", "agradecimento");
        System.out.println(msgFinal);

        // Exibir dispositivo
        System.out.println("Dispositivo utilizado: " + celular);
    }
}
