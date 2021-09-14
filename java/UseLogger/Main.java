import java.util.logging.*;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());


    public static void main(String[] args) {
        LOGGER.setLevel(Level.WARNING);
	    LOGGER.log(Level.INFO, "Hi");

	    Handler consoleHandler = new ConsoleHandler();
	    consoleHandler.setFormatter(new XMLFormatter());
	    consoleHandler.setLevel(Level.ALL);

        Logger loga = Logger.getLogger("org.stepic.java.logging.ClassA");
        loga.setLevel(Level.ALL);

        Logger logb = Logger.getLogger("org.stepic.java.logging.ClassB");
        logb.setLevel(Level.WARNING);

        Logger logmain = Logger.getLogger("org.stepic.java");
        logmain.setLevel(Level.ALL);
        logmain.setUseParentHandlers(false);
        logmain.addHandler(consoleHandler);
        logmain.setFilter((LogRecord logRecord) -> false);
    }


}
