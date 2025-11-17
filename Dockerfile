FROM odoo:16.0
USER root

# Копируем папку модуля в Odoo
COPY odoo_inventory_integration /mnt/extra-addons/inventory_integration

# Даем права
RUN chown -R odoo:odoo /mnt/extra-addons/

USER odoo