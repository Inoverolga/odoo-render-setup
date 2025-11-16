FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
USER odoo

# Простая команда без сложной логики
CMD ["python3", "/usr/bin/odoo", "--without-demo=all"]