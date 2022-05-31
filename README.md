Hello to CHUCK NORRIS JOKES!

Chuck norris app consist of two components. First one is the application where the chuck norris jokes are  retrieved, and the second one is basic Dash web server run behind the nginx reverse proxy. 

Local testing: 

I've added gunicorn&wsgi for local testing in case needed '''CMD: gunicorn wsgi:application''' (consider using --bind option if you want to run it in a specific port)

Application: 

How to deploy the application, nginx, and container: ''' ansible-playbook -v deploy_backend.yml --tags install,container,start,deploy_nginx --diff ''', make sure you are in the ansible directory in order to run the deployment. 

Nginx is used as a reverse proxy, and it's RHEL compatible only. In case you will deploy it to ubuntu, deployment will most likely fail, and ansible package installations will not take place. 

To view the chuck norris jokes, cat the jokes.txt file. I used it as a workaround, therefore web application looks up to this file. !! In case jokes are not showing up in the browser, make sure web application is looking up the correct directory(main dir)

Application tested locally through browser, and made sure that jokes are flowing in the browser. However, if you are going to deploy it to the host where you can't have browser confired(How I tested it), curl command will return dash configs, not jokes. Dash application simply isn't compatible with curl, so you wont be seeing any jokes in the browser unless you open it through a browser. 

How to test web application working file: "curl localhost" -> this will redirect all connections to the application running in the container.