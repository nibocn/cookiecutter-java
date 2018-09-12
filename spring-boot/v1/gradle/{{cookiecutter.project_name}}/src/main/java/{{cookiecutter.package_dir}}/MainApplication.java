package {{ cookiecutter.package }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Spring Boot App Main Class
 *
 * @author {{ cookiecutter.full_name }}
 */
@SuppressWarnings({"PMD.UseUtilityClass", "PMD.ClassNamingConventions"})
@SpringBootApplication
public class MainApplication {

    // CSOFF: Javadoc
    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }
    // CSON: Javadoc
}
