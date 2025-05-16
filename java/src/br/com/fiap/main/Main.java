import br.com.fiap.bean.*;
import br.com.fiap.repositorio.RepositorioAgendamento;
import br.com.fiap.servico.ServicoAgendamento;

import java.time.LocalDateTime;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o nome do paciente: ");
        String nomePaciente = scanner.nextLine();

        System.out.print("Digite o CPF do paciente: ");
        String cpfPaciente = scanner.nextLine();

        System.out.print("Digite o número de telefone para contato: ");
        String telefone = scanner.nextLine();

        System.out.print("Digite a especialidade médica necessária (ex: fisioterapia, fonoaudiologia): ");
        String especialidade = scanner.nextLine();

        Usuario paciente = new Usuario(nomePaciente, cpfPaciente, "paciente");

        Unidade unidade = new Unidade("Hospital das Clínicas de SP", "Rua Dr. Ovídio Pires de Campos, 225 - Cerqueira César, São Paulo - SP");

        System.out.print("Digite a data do agendamento (formato: dd/MM/yyyy): ");
        String dataStr = scanner.nextLine();

        System.out.print("Você prefere agendar na manhã ou tarde? (Digite 'manhã' ou 'tarde'): ");
        String turno = scanner.nextLine().toLowerCase();
        String hora = turno.equals("manhã") ? "09:00" : "14:00";

        String[] dataPartes = dataStr.split("/");
        String dataFormatada = dataPartes[2] + "-" + dataPartes[1] + "-" + dataPartes[0];
        LocalDateTime dataHora = LocalDateTime.parse(dataFormatada + "T" + hora);

        Agendamento agendamento = new Agendamento(paciente, dataHora, especialidade);

        AssistenteVirtual assistente = new AssistenteVirtual();
        RepositorioAgendamento repo = new RepositorioAgendamento();
        ServicoAgendamento servico = new ServicoAgendamento(repo, assistente);

        servico.agendar(agendamento);

        Notificacao notificacao = new Notificacao(paciente.getNome(), "Olá " + paciente.getNome() + "! Seu atendimento de " + especialidade + " está agendado para " + agendamento.getDataHora(), "WhatsApp");

        notificacao.exibirResumo();

        servico.confirmar(agendamento);

        System.out.println("Orientações pré-consulta: " + Orientacao.gerar(especialidade));
        System.out.println("Local do atendimento: " + unidade.getResumo());

        Mensagem msgFinal = new Mensagem("Esperamos que seu atendimento tenha sido positivo!", "agradecimento");
        System.out.println(msgFinal);

        System.out.print("\nDeseja remarcar a consulta? (sim/não): ");
        String resposta = scanner.nextLine();

        if (resposta.equalsIgnoreCase("sim")) {
            System.out.println("\n--- Reagendamento ---");

            System.out.print("Digite o novo DIA da consulta: ");
            int novoDia = scanner.nextInt();

            System.out.print("Digite o novo MÊS da consulta: ");
            int novoMes = scanner.nextInt();

            System.out.print("Digite o novo ANO da consulta: ");
            int novoAno = scanner.nextInt();

            System.out.print("Digite a nova HORA da consulta: ");
            int novaHora = scanner.nextInt();

            System.out.print("Digite os novos MINUTOS da consulta: ");
            int novoMinuto = scanner.nextInt();
            scanner.nextLine(); // limpa o buffer

            LocalDateTime novaDataHora = LocalDateTime.of(novoAno, novoMes, novoDia, novaHora, novoMinuto);
            agendamento.reagendar(novaDataHora);

            System.out.println("Consulta remarcada com sucesso!");
            System.out.println("Novo agendamento: " + agendamento);
        } else {
            System.out.println("Consulta mantida. Obrigado!");
        }
    }
}
