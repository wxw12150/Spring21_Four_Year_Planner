npm intall

npm run build


in build/index.html:

  change:

    href="/FYP-Interface-Prototype/static/css/main.8cf0611e.chunk.css"
  
  to:
  
    href=“{% static 'css/main.8cf0611e.chunk.css' %}"
  
  change scripts:
   
   script src="{% static 'js/2.6ff07e24.chunk.js' %}"></script>
   
   script src="{% static 'js/main.685661ab.chunk.js' %}"></script>


add the main.685661ab.chunk.js file

python manage.py runserver
