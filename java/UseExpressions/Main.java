public class Main {

    public static void main(String[] args) {
        String[] roles= {
                "Городничий","Аммос Федорович",
                "Dmitry",
                "Артемий Филиппович",
                "Лука Лукич"
        };
        String[] textLines = {
                "Городничий: Я пригласил вас, господа, с тем, чтобы сообщить вам пренеприятное известие: к нам едет ревизор.",
                "Аммос Федорович: Как ревизор?",
                "Артемий Филиппович: Как ревизор?",
                "Городничий: Ревизор из Петербурга, инкогнито. И еще с секретным предписаньем.",
                "Аммос Федорович: Вот те на!",
                "Артемий Филиппович: Вот не было заботы, так подай!",
                "Лука Лукич: Господи боже! еще и с секретным предписаньем!"
        };

        System.out.println(printTextPerRole(roles, textLines));
    }

    public static String printTextPerRole(String[] roles, String[] textLines) {
        int countRoles = roles.length;
        int countLines = textLines.length;
        StringBuilder resultList = new StringBuilder();

        for (int i = 0; i < countRoles; ++i) {
            resultList.append(roles[i] + ":\n");
            for(int j = 0; j < countLines; ++j) {
                if(textLines[j].indexOf(roles[i] + ":") == 0)
                    resultList.append( (j + 1) + ") " + textLines[j].replaceAll("^.+?:\\s","") + '\n');
            }
            resultList.append('\n');
        }

        return resultList.toString();
    }
}
