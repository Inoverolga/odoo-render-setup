FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
USER odoo

# Явная инициализация базы
CMD ["/bin/bash", "-c", "sleep 10 && python3 /usr/bin/odoo -d odoo -i base --without-demo=all --stop-after-init && exec python3 /usr/bin/odoo"]