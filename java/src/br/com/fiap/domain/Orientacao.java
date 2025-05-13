package br.com.fiap.domain;

public class Orientacao {

    public static String gerar(String especialidade) {
        return switch (especialidade.toLowerCase()) {
            case "fisioterapia" -> "Use roupas confortáveis para facilitar os movimentos.";
            case "fonoaudiologia" -> "Evite alimentos pesados antes da consulta.";
            case "cardiologia" -> "Leve exames anteriores e lista de medicamentos.";
            case "arritmologia" -> "Trata distúrbios do ritmo cardíaco, como taquicardia e fibrilação atrial.";
            case "cardiologia pediátrica" -> "Foca em doenças cardíacas congênitas ou adquiridas em crianças.";
            case "endocrinologia" -> "Trata doenças hormonais, como diabetes, tireoide e obesidade.";
            case "gastroenterologia" -> "Lida com doenças do sistema digestivo, como gastrite, refluxo e fígado.";
            case "ginecologia" -> "Cuida da saúde do sistema reprodutor feminino.";
            case "infectologia" -> "Diagnostica e trata infecções causadas por vírus, bactérias e outros agentes.";
            case "mastologia" -> "Especializa-se na saúde das mamas, incluindo prevenção e tratamento do câncer de mama.";
            case "nefrologia" -> "Trata doenças dos rins, como insuficiência renal e nefrites.";
            case "neurologia" -> "Cuida de distúrbios do sistema nervoso, como AVC, epilepsia e esclerose múltipla.";
            case "oftalmologia" -> "Trata doenças dos olhos e problemas de visão.";
            case "oncologia" -> "Diagnostica e trata o câncer em adultos.";
            case "oncologia pediátrica" -> "Cuida do tratamento de câncer em crianças.";
            case "ortopedia" -> "Trata lesões e doenças dos ossos, músculos e articulações.";
            case "otorrinolaringologia" -> "Cuida do ouvido, nariz e garganta.";
            case "patologia clínica" -> "Analisa exames laboratoriais para ajudar no diagnóstico de doenças.";
            case "pediatria geral" -> "Acompanha a saúde e desenvolvimento de crianças e adolescentes.";
            case "pneumologia" -> "Trata doenças dos pulmões e vias respiratórias, como asma e DPOC.";
            case "pronto-socorro" -> "Atende emergências médicas de forma imediata.";
            case "psicologia clínica" -> "Oferece acompanhamento psicológico e tratamento de transtornos emocionais.";
            case "psiquiatria" -> "Diagnostica e trata transtornos mentais com uso de medicamentos, se necessário.";
            case "quimioterapia" -> "Realiza tratamento medicamentoso contra o câncer.";
            case "radiologia" -> "Usa exames de imagem (como raio-X e tomografia) para diagnóstico.";
            case "reabilitação" -> "Promove a recuperação funcional de pacientes com deficiências ou após traumas.";
            case "tocoginecologia" -> "Junta obstetrícia e ginecologia, cuidando da gravidez e saúde feminina.";
            case "transplantes" -> "Realiza e acompanha pacientes submetidos a transplantes de órgãos.";
            case "urologia" -> "Trata doenças do sistema urinário e do aparelho reprodutor masculino.";
            default -> "Compareça com 15 minutos de antecedência e leve seus documentos.";
        };
    }
}
