FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
USER odoo
COPY ./odoo_inventory_integration /mnt/extra-addons/odoo_inventory_integration
CMD ["/bin/bash", "-c", "sleep 10 && python3 /usr/bin/odoo -d $DB_NAME --db_host=$DB_HOST --db_port=$DB_PORT --db_user=$DB_USER --db_password=$DB_PASSWORD -i base --without-demo=all --stop-after-init && exec python3 /usr/bin/odoo --db_host=$DB_HOST --db_port=$DB_PORT --db_user=$DB_USER --db_password=$DB_PASSWORD"]