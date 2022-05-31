FROM ubuntu:18.04
# LABEL para la imagen
LABEL version="1.0"
LABEL description="Imagen del servicio de Gestion de Logs"
# Actualizacion del repositorio de Ubuntu
RUN apt update
#Mongo
RUN apt-get install -y mongodb
RUN cd / && mkdir data && cd /data && mkdir db
# Definicion de variables ENV
ENV supervisor_conf /etc/supervisor/supervisord.conf
# Supervidord
RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisord.conf
# Puerto donde apuntaran los subsistemas
EXPOSE 8087
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]