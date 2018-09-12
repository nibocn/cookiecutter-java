package {{ cookiecutter.package }};
{% if cookiecutter.enabled_lombok == 'yes' %}
import lombok.extern.slf4j.Slf4j;
{%- else %}
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
{%- endif %}

/**
 * Hello World
 *
 * @author {{ cookiecutter.full_name }}
 */
{%- if cookiecutter.enabled_lombok == 'yes' %}
@Slf4j
{%- endif %}
@SuppressWarnings({"PMD.UseUtilityClass", "PMD.ClassNamingConventions"})
public class App {
    {%- if cookiecutter.enabled_lombok == 'no' %}
    private static final Logger LOGGER = LoggerFactory.getLogger(App.class);
    {%- endif %}

    // CSOFF: Javadoc
    @SuppressWarnings("PMD.UnusedFormalParameter")
    public static void main(String[] args) {
        {%- if cookiecutter.enabled_lombok == 'yes' %}
        log.debug("Hello World!");
        {%- else %}
        LOGGER.debug("Hello World!");
        {%- endif %}

    }
    // CSON: Javadoc
}
