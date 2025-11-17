FROM odoo:16.0
USER root

COPY odoo_inventory_integration /mnt/extra-addons/inventory_integration
COPY odoo.conf /etc/odoo/odoo.conf

# ПРОВЕРЯЕМ что конфиг скопировался
RUN cat /etc/odoo/odoo.conf && \
    echo "=== Current config ===" && \
    ls -la /etc/odoo/

RUN chown -R odoo:odoo /mnt/extra-addons/ /etc/odoo/

USER odoo
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]