package br.com.fiap.application;
import br.com.fiap.domain.*;
import br.com.fiap.repository.AgendamentoRepository;
import br.com.fiap.service.AgendamentoService;
import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        Usuario paciente = new Usuario("João da Silva", "12345678900", "paciente");
        Dispositivo celular = new Dispositivo("Samsung A10", true);
        Agendamento agendamento = new Agendamento(paciente, LocalDateTime.now().plusDays(1));

        AssistenteVirtual assistente = new AssistenteVirtual();
        AgendamentoRepository repo = new AgendamentoRepository();
        AgendamentoService service = new AgendamentoService(repo, assistente);

        service.agendar(agendamento);
        service.confirmar(agendamento);

        System.out.println("Dispositivo: " + celular);
        System.out.println("Agendamentos:");
        repo.buscarTodos();
    }
}
