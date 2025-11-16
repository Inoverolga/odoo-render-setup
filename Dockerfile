FROM odoo:16

USER root
RUN apt-get update && apt-get install -y postgresql-client
USER odoo

# Явно передаем переменные в команду
CMD ["python3", "/usr/bin/odoo", "--without-demo=all", "--db_host=${DB_HOST}", "--db_port=${DB_PORT}", "--db_user=${DB_USER}", "--db_password=${DB_PASSWORD}", "--database=${DB_NAME}"]