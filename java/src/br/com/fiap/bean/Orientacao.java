package br.com.fiap.bean;

public class Orientacao {

    public static String gerar(String especialidade) {
        return switch (especialidade.toLowerCase()) {
            case "fisioterapeuta" -> "Use roupas confortáveis para facilitar os movimentos.";
            case "fonoaudiólogo" -> "Evite alimentos pesados antes da consulta.";
            case "cardiologista" -> "Leve exames anteriores e lista de medicamentos.";
            case "arritmologista" -> "Trata distúrbios do ritmo cardíaco, como taquicardia e fibrilação atrial.";
            case "cardiologista pediátrico" -> "Foca em doenças cardíacas congênitas ou adquiridas em crianças.";
            case "endocrinologista" -> "Trata doenças hormonais, como diabetes, tireoide e obesidade.";
            case "gastroenterologista" -> "Lida com doenças do sistema digestivo, como gastrite, refluxo e fígado.";
            case "ginecologista" -> "Cuida da saúde do sistema reprodutor feminino.";
            case "infectologista" -> "Diagnostica e trata infecções causadas por vírus, bactérias e outros agentes.";
            case "mastologista" -> "Especializa-se na saúde das mamas, incluindo prevenção e tratamento do câncer de mama.";
            case "nefrologista" -> "Trata doenças dos rins, como insuficiência renal e nefrites.";
            case "neurologista" -> "Cuida de distúrbios do sistema nervoso, como AVC, epilepsia e esclerose múltipla.";
            case "oftalmologista" -> "Trata doenças dos olhos e problemas de visão.";
            case "oncologista" -> "Diagnostica e trata o câncer em adultos.";
            case "oncologista pediátrico" -> "Cuida do tratamento de câncer em crianças.";
            case "ortopedista" -> "Trata lesões e doenças dos ossos, músculos e articulações.";
            case "otorrinolaringologista" -> "Cuida do ouvido, nariz e garganta.";
            case "patologista clínico" -> "Analisa exames laboratoriais para ajudar no diagnóstico de doenças.";
            case "pediatra" -> "Acompanha a saúde e desenvolvimento de crianças e adolescentes.";
            case "pneumologista" -> "Trata doenças dos pulmões e vias respiratórias, como asma e DPOC.";
            case "médico do pronto-socorro" -> "Atende emergências médicas de forma imediata.";
            case "psicólogo clínico" -> "Oferece acompanhamento psicológico e tratamento de transtornos emocionais.";
            case "psiquiatra" -> "Diagnostica e trata transtornos mentais com uso de medicamentos, se necessário.";
            case "especialista em quimioterapia" -> "Realiza tratamento medicamentoso contra o câncer.";
            case "radiologista" -> "Usa exames de imagem (como raio-X e tomografia) para diagnóstico.";
            case "especialista em reabilitação" -> "Promove a recuperação funcional de pacientes com deficiências ou após traumas.";
            case "tocoginecologista" -> "Junta obstetrícia e ginecologia, cuidando da gravidez e saúde feminina.";
            case "especialista em transplantes" -> "Realiza e acompanha pacientes submetidos a transplantes de órgãos.";
            case "urologista" -> "Trata doenças do sistema urinário e do aparelho reprodutor masculino.";
            default -> "Compareça com 15 minutos de antecedência e leve seus documentos.";
        };
    }
}