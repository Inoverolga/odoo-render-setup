FROM odoo:16
COPY odoo.conf /etc/odoo/
CMD ["python3", "/usr/bin/odoo"]