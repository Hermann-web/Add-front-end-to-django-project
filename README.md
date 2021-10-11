# Add-front-end-to-django-project

## requirements
- python >=6
- django >= 3.1.2

## [html_to_template](https://github.com/Hermann-web/Web-development-Add-front-end-to-django-project/tree/main/html_to_template)
<p style='font-size:25px'>A project that allow to take any html file and to transform it into a template</p>

### exemples

- ce code remplace <code>href="panier.html">Pani-link" href="panier.html">Pani</code> par <code>href={% static "panier.html" %}>Pani-link" href={% static "panier.html" %}>Pani</code>
- ce code remplace <code>href="panier.html"</code> par <code>href={% url "panier" %}</code>
- ce code remplace <code>href="mm.png"</code> par <code>href={% static "mm.png" %}</code>
- ce code remplace <code>href="contact.html"</code> par <code>src={% url "contact" %}</code>
- ce code remplace <code>href="panier.png"</code> par <code>src={% static "panier.png" %}</code>
- ce code evite de faire ces operations sur <code>href={</code>, <code>href="#</code>, <code>href=""</code>,<code>href={</code> 
- Après ces operations, il crée un nouveau fichier 


## [Starter_project](https://github.com/Hermann-web/Web-development-Add-front-end-to-django-project/tree/main/Starter_project)
A basic django project already set up with static dirs 
