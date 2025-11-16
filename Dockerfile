FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
COPY ./odoo_integration /mnt/extra-addons/odoo_integration
RUN chown -R odoo:odoo /mnt/extra-addons/
USER odoo

CMD ["/bin/bash", "-c", "sleep 10 && python3 /usr/bin/odoo -d $DB_NAME --db_host=$DB_HOST --db_port=$DB_PORT --db_user=$DB_USER --db_password=$DB_PASSWORD --update=odoo_integration --without-demo=all --stop-after-init && exec python3 /usr/bin/odoo --db_host=$DB_HOST --db_port=$DB_PORT --db_user=$DB_USER --db_password=$DB_PASSWORD"]