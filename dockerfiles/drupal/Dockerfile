FROM    debian:jessie
MAINTAINER "curtis@serverascode.com"
# orig from https://github.com/ricardoamaro/docker-drupal

RUN apt-get update

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install git mysql-client \
    mysql-server apache2 libapache2-mod-php5 pwgen python-setuptools \
    vim-tiny php5-mysql php-apc php5-gd php5-curl php5-memcache memcached \
    drush mc
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean

# Make mysql listen on the outside
RUN sed -i "s/^bind-address/#bind-address/" /etc/mysql/my.cnf

RUN easy_install supervisor
ADD ./start.sh /start.sh
ADD ./foreground.sh /etc/apache2/foreground.sh
ADD ./supervisord.conf /etc/supervisord.conf
# this was for drush, mbstring
ADD ./php.ini /etc/php5/cli/php.ini

# Retrieve drupal
RUN rm -rf /var/www/html/ ; cd /var ; drush dl drupal-7.31 ; mv /var/drupal*/ /var/www/html/
RUN chmod a+w /var/www/html/sites/default ; mkdir /var/www/html/sites/default/files ; chown -R www-data:www-data /var/www/html/

RUN chmod 755 /start.sh /etc/apache2/foreground.sh
EXPOSE 80
CMD ["/bin/bash", "/start.sh"]
