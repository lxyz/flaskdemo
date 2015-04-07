### Installation


nginx配置一个server
```
server {
        listen 80;
        server_name flaskdemo.jpretty.net;

        location / {
                include uwsgi_params;
                uwsgi_pass 127.0.0.1:5001;
        }

        error_log /var/log/nginx/flaskdemo.jpretty.net.error.log;
        access_log /var/log/nginx/flaskdemo.jpretty.net.access.log;
}
```

uwsgi


```
<uwsgi>

     <pythonpath>/home/adam/webapp/pyapp/flaskdemo</pythonpath>

     <module>run</module>

     <callable>app</callable>

     <socket>127.0.0.1:5001</socket>
     <plugins>python</plugins>
     <master/>

     <processes>4</processes>

     <memory-report/>

</uwsgi>
```
