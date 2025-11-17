FROM odoo:16.0
USER root
COPY odoo_inventory_integration /mnt/extra-addons/inventory_integration
COPY odoo.conf /etc/odoo/
RUN chown -R odoo:odoo /mnt/extra-addons/ /etc/odoo/
USER odoo