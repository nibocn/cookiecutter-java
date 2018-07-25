package {{ cookiecutter.package }};

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Hello World
 *
 * @author {{ cookiecutter.full_name }}
 */
@SuppressWarnings({"PMD.UseUtilityClass", "PMD.ClassNamingConventions"})
public class App {
    private static final Logger LOGGER = LoggerFactory.getLogger(App.class);

    // CSOFF: Javadoc
    @SuppressWarnings("PMD.UnusedFormalParameter")
    public static void main(String[] args) {
        LOGGER.debug("Hello World!");
    }
    // CSON: Javadoc
}
