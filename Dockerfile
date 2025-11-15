FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
USER odoo

# Используем переменные окружения для подключения к базе
CMD ["/bin/bash", "-c", "sleep 10 && python3 /usr/bin/odoo -d $DATABASE --db_host=$HOST --db_port=$PORT --db_user=$USER --db_password=$PASSWORD -i base --without-demo=all --stop-after-init && exec python3 /usr/bin/odoo --db_host=$HOST --db_port=$PORT --db_user=$USER --db_password=$PASSWORD"]